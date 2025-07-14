import re
from datetime import datetime
TIME_MODE = 'esp32'  # 'esp32' for ESP32 time, 'bt_log' for Bluetooth log time, 'relative' for session-relative time
columns = ["time", "roll", "pitch", "yaw", "steps", "stride", "dist", "fsr", "fsrvar", "ax", "ay", "az", "linmag", "gravx", "gravy", "gravz", "gx", "gy", "gz", "temp"]
input_file = "log.txt"
output_file = "data.csv"
data_line_regex = re.compile(r"^\[(\d{2}):(\d{2}):(\d{2})\]\s+([\d\-,.\s]+)$")
SESSION_GAP_THRESHOLD = 10
sessions = []
current_session = []
first_bt_time = None
last_bt_time = None
last_rel_time = 0
new_session_flag = False
def normalize_yaw(yaw_value, last_yaw):
    if last_yaw is None: return yaw_value
    diff = yaw_value - last_yaw
    if diff > 180: return yaw_value - 360
    elif diff < -180: return yaw_value + 360
    return yaw_value
with open(input_file, "r") as infile:
    last_yaw = None
    for line in infile:
        line = line.strip()
        if "Disconnected from ESP32" in line:
            new_session_flag = True
            continue
        match = data_line_regex.match(line)
        if match:
            h, m, s = map(int, match.group(1, 2, 3))
            bt_time = h * 3600 + m * 60 + s
            bt_time_str = f"{h:02d}:{m:02d}:{s:02d}"
            if first_bt_time is None or new_session_flag:
                if current_session: sessions.append(current_session)
                current_session = []
                first_bt_time = bt_time
                last_bt_time = bt_time
                rel_time = 0
                new_session_flag = False
                last_yaw = None
            else:
                if bt_time < last_bt_time or (bt_time - last_bt_time) > SESSION_GAP_THRESHOLD:
                    if current_session: sessions.append(current_session)
                    current_session = []
                    first_bt_time = bt_time
                    rel_time = 0
                    last_yaw = None
                else:
                    rel_time = last_rel_time + (bt_time - last_bt_time)
                last_bt_time = bt_time
            numbers = re.sub(r",\s+", ",", match.group(4))
            parts = numbers.split(",", 1)
            if len(parts) == 2:
                esp32_time = parts[0].strip()
                data_parts = parts[1].split(",")
                if len(data_parts) >= 3:
                    try:
                        yaw_value = float(data_parts[2])
                        normalized_yaw = normalize_yaw(yaw_value, last_yaw)
                        last_yaw = normalized_yaw
                        data_parts[2] = str(normalized_yaw)
                        modified_data = ",".join(data_parts)
                        # Choose time value based on TIME_MODE
                        if TIME_MODE == 'esp32':
                            time_value = esp32_time
                        elif TIME_MODE == 'bt_log':
                            time_value = bt_time_str
                        else:
                            time_value = rel_time
                        row = f"{time_value},{modified_data}"
                    except ValueError:
                        if TIME_MODE == 'esp32':
                            time_value = esp32_time
                        elif TIME_MODE == 'bt_log':
                            time_value = bt_time_str
                        else:
                            time_value = rel_time
                        row = f"{time_value},{parts[1]}"
                else:
                    if TIME_MODE == 'esp32':
                        time_value = esp32_time
                    elif TIME_MODE == 'bt_log':
                        time_value = bt_time_str
                    else:
                        time_value = rel_time
                    row = f"{time_value},{parts[1]}"
                current_session.append(row)
                last_rel_time = rel_time
if current_session:
    sessions.append(current_session)
largest_session = max(sessions, key=len) if sessions else []
with open(output_file, "w") as outfile:
    outfile.write(",".join(columns) + "\n")
    for row in largest_session:
        outfile.write(row + "\n")
print(f"Wrote {len(largest_session)} rows from the largest continuous session to {output_file}!")