def hex_to_str(hex_str):
    hex_str = hex_str.strip()
    if hex_str.startswith("0x") or hex_str.startswith("0X"):
        hex_str = hex_str[2:]
    hex_str = hex_str.replace(" ", "")
    try:
        return bytes.fromhex(hex_str).decode('utf-8')
    except Exception as e:
        raise ValueError(f"Invalid hex string: {e}")

def str_to_hex(s, with_prefix=False):
    hexed = s.encode('utf-8').hex()
    if with_prefix:
        return "0x" + hexed
    return hexed

def main():
    print("Hex/Text Converter")
    print("Choose mode:")
    print("1. Hex to Text")
    print("2. Text to Hex")
    mode = input("Enter 1 or 2: ").strip()
    if mode == "1":
        hex_input = input("Enter hex string: ")
        try:
            text = hex_to_str(hex_input)
            print("Decoded text:", text)
        except Exception as e:
            print("Error:", e)
    elif mode == "2":
        text_input = input("Enter text to convert to hex: ")
        prefix = input("Add 0x prefix? (y/n): ").strip().lower() == "y"
        hexed = str_to_hex(text_input, with_prefix=prefix)
        print("Hex string:", hexed)
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    while (True): main()
