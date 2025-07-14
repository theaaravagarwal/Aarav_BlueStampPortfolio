import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
import seaborn as sns
from scipy.stats import zscore, pearsonr, spearmanr, kurtosis, skew
from scipy import signal
from scipy.integrate import cumulative_trapezoid
from scipy.fft import fft, fftfreq
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')
columns = ["time", "roll", "pitch", "yaw", "steps", "stride", "dist", "fsr", "fsrvar", "ax", "ay", "az", "linmag", "gravx", "gravy", "gravz", "gx", "gy", "gz", "temp"]
try:
    df = pd.read_csv("data.csv")
    print(f"Loaded {len(df)} data points with {len(df.columns)} columns")
except Exception as e:
    print(f"Error loading data: {e}")
    exit(1)
run_num = 1
while os.path.exists(f"run{run_num}"):
    run_num+=1
out_dir = f"run{run_num}"
os.makedirs(out_dir, exist_ok=True)
def save_plot(x, ys, labels, title, ylabel, filename):
    plt.figure(figsize=(12, 6))
    colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
    for i, (y, label) in enumerate(zip(ys, labels)):
        color = colors[i % len(colors)]
        plt.plot(x, y, label=label, linewidth=1.5, color=color, alpha=0.8)
    plt.xlabel("Time (s)")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, filename), dpi=300, bbox_inches='tight')
    plt.close()
summary_lines = []
analysis_results = {}
summary_lines.append("=== ENHANCED PHYSICS-BASED ANALYSIS ===\n")
dt = np.diff(df["time"])
if len(dt) > 0:
    dt = np.append(dt, dt[-1])
    sampling_rate = 1.0 / np.mean(dt)
    summary_lines.append(f"Average sampling rate: {sampling_rate:.2f} Hz")
    summary_lines.append(f"Total recording time: {df['time'].max() - df['time'].min():.2f} seconds")
    vx = cumulative_trapezoid(df["ax"], df["time"], initial=0)
    vy = cumulative_trapezoid(df["ay"], df["time"], initial=0)
    vz = cumulative_trapezoid(df["az"], df["time"], initial=0)
    v_mag = np.sqrt(vx**2 + vy**2 + vz**2)
    dx = cumulative_trapezoid(vx, df["time"], initial=0)
    dy = cumulative_trapezoid(vy, df["time"], initial=0)
    dz = cumulative_trapezoid(vz, df["time"], initial=0)
    d_mag = np.sqrt(dx**2 + dy**2 + dz**2)
    ke_linear = 0.5 * v_mag**2
    pe_gravitational = 9.81 * dz
    total_mechanical_energy = ke_linear + pe_gravitational
    save_plot(df["time"], [vx, vy, vz, v_mag], ["Vx", "Vy", "Vz", "|V|"], "Velocity Components", "Velocity (m/s)", "velocity.png")
    save_plot(df["time"], [dx, dy, dz, d_mag], ["Dx", "Dy", "Dz", "|D|"], "Displacement Components", "Displacement (m)", "displacement.png")
    save_plot(df["time"], [ke_linear, pe_gravitational, total_mechanical_energy], ["Kinetic Energy", "Potential Energy", "Total Mechanical Energy"], "Energy Analysis", "Energy per Unit Mass (J/kg)", "mechanical_energy.png")
    summary_lines.append(f"Max velocity magnitude: {v_mag.max():.3f} m/s")
    summary_lines.append(f"Max displacement magnitude: {d_mag.max():.3f} m")
    summary_lines.append(f"Max kinetic energy: {ke_linear.max():.3f} J/kg")
    summary_lines.append(f"Energy efficiency (min/max KE ratio): {ke_linear.min()/ke_linear.max():.3f}")
    analysis_results['velocity_stats'] = {
        'max_v': v_mag.max(),
        'mean_v': v_mag.mean(),
        'std_v': v_mag.std(),
        'max_displacement': d_mag.max()
    }
gyro_mag = np.sqrt(df["gx"]**2 + df["gy"]**2 + df["gz"]**2)
gyro_energy = 0.5 * gyro_mag**2
angular_momentum = gyro_mag * 0.1
save_plot(df["time"], [gyro_mag, gyro_energy, angular_momentum], ["|ω|", "Rotational Energy", "Angular Momentum"], "Angular Motion Analysis", "Angular Velocity (rad/s) / Energy (J) / Momentum (kg⋅m²/s)", "gyro_energy.png")
summary_lines.append(f"Max angular velocity: {gyro_mag.max():.3f} rad/s")
summary_lines.append(f"Max rotational energy: {gyro_energy.max():.3f} J")
summary_lines.append(f"Angular motion stability (1/var): {1/np.var(gyro_mag):.3f}")
if "fsr" in df.columns:
    fsr_pressure = df["fsr"] / 4095.0
    fsr_contact = fsr_pressure > 0.1
    contact_changes = np.diff(fsr_contact.astype(int))
    contact_starts = np.where(contact_changes == 1)[0]
    contact_ends = np.where(contact_changes == -1)[0]
    if len(contact_starts) > 0 and len(contact_ends) > 0:
        contact_durations = []
        contact_pressures = []
        for start, end in zip(contact_starts, contact_ends):
            if end > start:
                duration = df["time"].iloc[end] - df["time"].iloc[start]
                contact_durations.append(duration)
                avg_pressure = fsr_pressure.iloc[start:end].mean()
                contact_pressures.append(avg_pressure)
        if contact_durations:
            summary_lines.append(f"Average contact duration: {np.mean(contact_durations):.3f} s")
            summary_lines.append(f"Contact duration CV: {np.std(contact_durations)/np.mean(contact_durations):.3f}")
            summary_lines.append(f"Number of contacts: {len(contact_durations)}")
            summary_lines.append(f"Average contact pressure: {np.mean(contact_pressures):.3f}")
            summary_lines.append(f"Contact pressure variability: {np.std(contact_pressures):.3f}")
            if len(contact_durations) > 5:
                stance_phase = np.mean(contact_durations) / (np.mean(contact_durations) + np.mean(np.diff(contact_starts)))
                summary_lines.append(f"Estimated stance phase: {stance_phase:.2%}")
    save_plot(df["time"], [fsr_pressure, fsr_contact], 
              ["FSR Pressure", "Contact"], 
              "FSR Pressure and Contact Detection", 
              "Pressure / Contact", "fsr_contact.png")
def enhanced_psd_analysis(data, time, title, filename):
    data_detrend = signal.detrend(data - np.mean(data))
    fs = 1.0 / np.mean(np.diff(time))
    f, psd = signal.welch(data_detrend, fs, nperseg=min(256, len(data)//4))
    fft_vals = fft(data_detrend)
    fft_freq = fftfreq(len(data_detrend), 1/fs)
    plt.figure(figsize=(15, 10))
    plt.subplot(2, 2, 1)
    plt.semilogy(f, psd)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power Spectral Density')
    plt.title(f'{title} - PSD')
    plt.grid(True)
    plt.subplot(2, 2, 2)
    plt.plot(fft_freq[:len(fft_freq)//2], np.abs(fft_vals[:len(fft_freq)//2]))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('FFT Magnitude')
    plt.title(f'{title} - FFT')
    plt.grid(True)
    plt.subplot(2, 2, 3)
    plt.plot(time, data_detrend, label='Signal')
    analytic_signal = signal.hilbert(data_detrend)
    envelope = np.abs(analytic_signal)
    plt.plot(time, envelope, label='Envelope', alpha=0.7)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title(f'{title} - Signal and Envelope')
    plt.legend()
    plt.grid(True)
    plt.subplot(2, 2, 4)
    f_spec, t_spec, Sxx = signal.spectrogram(data_detrend, fs, nperseg=64, noverlap=32)
    plt.pcolormesh(t_spec, f_spec, 10 * np.log10(Sxx))
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (s)')
    plt.title(f'{title} - Spectrogram')
    plt.colorbar(label='Power (dB)')
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, filename))
    plt.close()
    dominant_freq = f[np.argmax(psd)]
    bandwidth = f[np.where(psd > 0.1 * psd.max())[0]]
    bandwidth_width = bandwidth.max() - bandwidth.min() if len(bandwidth) > 0 else 0
    summary_lines.append(f"{title} dominant frequency: {dominant_freq:.2f} Hz")
    summary_lines.append(f"{title} bandwidth: {bandwidth_width:.2f} Hz")
    summary_lines.append(f"{title} spectral centroid: {np.sum(f * psd) / np.sum(psd):.2f} Hz")
    return dominant_freq, bandwidth_width
enhanced_psd_analysis(df["linmag"], df["time"], "Linear Acceleration PSD", "psd_linmag.png")
enhanced_psd_analysis(gyro_mag, df["time"], "Angular Velocity PSD", "psd_gyro.png")
summary_lines.append("\n=== ENHANCED GAIT ANALYSIS ===\n")
if "steps" in df.columns:
    try:
        step_diffs = df["steps"].diff().fillna(0)
        step_events = df[step_diffs > 0]["time"]
        if len(step_events) > 2:
            step_intervals = step_events.diff().dropna()
            cv_step = np.std(step_intervals) / np.mean(step_intervals)
            step_freq = 1 / step_intervals.mean()
            step_freq_var = np.var(step_intervals)
            symmetry_index = 1 - cv_step
            stability_index = 1.0 / step_freq_var if step_freq_var > 0 else 0
            step_regularity = np.corrcoef(step_intervals[:-1], step_intervals[1:])[0, 1]
            summary_lines.append(f"Step frequency: {step_freq:.2f} Hz")
            summary_lines.append(f"Step frequency CV: {cv_step:.3f}")
            summary_lines.append(f"Gait symmetry index: {symmetry_index:.3f}")
            summary_lines.append(f"Gait stability index: {stability_index:.3f}")
            summary_lines.append(f"Step regularity: {step_regularity:.3f}")
            if len(step_intervals) > 10:
                avg_step_time = step_intervals.mean()
                if avg_step_time < 0.5:
                    gait_type = "Running"
                elif avg_step_time < 1.0:
                    gait_type = "Fast Walking"
                else:
                    gait_type = "Slow Walking"
                summary_lines.append(f"Gait type: {gait_type}")
                summary_lines.append(f"Average step time: {avg_step_time:.3f} s")
            plt.figure(figsize=(12, 4))
            plt.eventplot(step_events, orientation='horizontal', colors='b', linewidth=2)
            plt.title("Step Events Over Time")
            plt.xlabel("Time (s)")
            plt.ylabel("Steps")
            plt.tight_layout()
            plt.savefig(os.path.join(out_dir, "step_events.png"))
            plt.close()
            analysis_results['gait_stats'] = {
                'step_freq': step_freq,
                'symmetry': symmetry_index,
                'stability': stability_index,
                'regularity': step_regularity
            }
    except Exception as e:
        summary_lines.append(f"Error in step analysis: {str(e)}")
summary_lines.append("\n=== ENHANCED STATISTICAL ANALYSIS ===\n")
def comprehensive_statistics(data, name):
    stats = {}
    stats['mean'] = np.mean(data)
    stats['std'] = np.std(data)
    stats['skewness'] = skew(data)
    stats['kurtosis'] = kurtosis(data)
    stats['min'] = np.min(data)
    stats['max'] = np.max(data)
    stats['range'] = stats['max'] - stats['min']
    stats['cv'] = stats['std'] / stats['mean'] if stats['mean'] != 0 else 0
    stats['iqr'] = np.percentile(data, 75) - np.percentile(data, 25)
    z_scores = zscore(data)
    outliers = np.where(np.abs(z_scores) > 3)[0]
    stats['outlier_count'] = len(outliers)
    stats['outlier_percentage'] = len(outliers) / len(data) * 100
    stats['normality_test'] = "Normal" if abs(stats['skewness']) < 1 and abs(stats['kurtosis']) < 2 else "Non-normal"
    return stats
key_vars = ["ax", "ay", "az", "linmag", "stride", "dist", "fsr", "fsrvar", "temp", "gx", "gy", "gz"]
for var in key_vars:
    if var in df.columns:
        stats = comprehensive_statistics(df[var].dropna(), var)
        summary_lines.append(f"\n{var.upper()} Statistics:")
        summary_lines.append(f"  Mean: {stats['mean']:.3f}")
        summary_lines.append(f"  Std: {stats['std']:.3f}")
        summary_lines.append(f"  Skewness: {stats['skewness']:.3f}")
        summary_lines.append(f"  Kurtosis: {stats['kurtosis']:.3f}")
        summary_lines.append(f"  CV: {stats['cv']:.3f}")
        summary_lines.append(f"  Outliers: {stats['outlier_count']} ({stats['outlier_percentage']:.1f}%)")
        summary_lines.append(f"  Distribution: {stats['normality_test']}")
summary_lines.append("\n=== ENHANCED CORRELATION ANALYSIS ===\n")
numeric_cols = df.select_dtypes(include=[np.number]).columns
correlation_matrix = df[numeric_cols].corr()
corr_pairs = []
for i in range(len(correlation_matrix.columns)):
    for j in range(i+1, len(correlation_matrix.columns)):
        corr_val = correlation_matrix.iloc[i, j]
        if abs(corr_val) > 0.5:
            corr_pairs.append((correlation_matrix.columns[i], correlation_matrix.columns[j], corr_val))
corr_pairs.sort(key=lambda x: abs(x[2]), reverse=True)
summary_lines.append("Strongest Correlations (|r| > 0.5):")
for var1, var2, corr_val in corr_pairs[:10]:
    summary_lines.append(f"  {var1} vs {var2}: {corr_val:.3f}")
summary_lines.append("\n=== ENHANCED ACTIVITY ANALYSIS ===\n")
linmag_mean = df["linmag"].mean()
linmag_std = df["linmag"].std()
activity_levels = {
    'low': df["linmag"] < (linmag_mean - linmag_std),
    'medium': (df["linmag"] >= (linmag_mean - linmag_std)) & (df["linmag"] <= (linmag_mean + linmag_std)),
    'high': df["linmag"] > (linmag_mean + linmag_std)
}
for level, mask in activity_levels.items():
    percentage = mask.sum() / len(df) * 100
    summary_lines.append(f"{level.capitalize()} activity: {percentage:.1f}% of time")
activity_sequence = np.where(activity_levels['low'], 0, np.where(activity_levels['medium'], 1, 2))
activity_changes = np.diff(activity_sequence)
transition_count = np.sum(activity_changes != 0)
summary_lines.append(f"Activity transitions: {transition_count}")
summary_lines.append("\n=== PATTERN RECOGNITION ===\n")
def detect_cycles(data, min_cycle_length=10):
    autocorr = np.correlate(data, data, mode='full')
    autocorr = autocorr[len(autocorr)//2:]
    peaks, _ = signal.find_peaks(autocorr, height=0.1*autocorr.max())
    if len(peaks) > 1:
        cycle_lengths = np.diff(peaks)
        return np.mean(cycle_lengths), np.std(cycle_lengths)
    return None, None
for var in ["linmag", "ax", "ay", "az"]:
    if var in df.columns:
        mean_cycle, std_cycle = detect_cycles(df[var].values)
        if mean_cycle is not None:
            summary_lines.append(f"{var} cycle length: {mean_cycle:.1f} ± {std_cycle:.1f} samples")
summary_lines.append("\n=== ANOMALY DETECTION ===\n")
def detect_anomalies(data, window_size=100):
    rolling_mean = data.rolling(window=window_size, center=True).mean()
    rolling_std = data.rolling(window=window_size, center=True).std()
    z_scores = (data - rolling_mean) / rolling_std
    anomalies = np.abs(z_scores) > 3
    return anomalies, z_scores
for var in ["linmag", "ax", "ay", "az", "temp"]:
    if var in df.columns:
        anomalies, z_scores = detect_anomalies(df[var])
        anomaly_count = anomalies.sum()
        summary_lines.append(f"{var} anomalies: {anomaly_count} ({anomaly_count/len(df)*100:.1f}%)")
def create_enhanced_histograms():
    fig, axes = plt.subplots(3, 4, figsize=(20, 15))
    axes = axes.flatten()
    hist_vars = ["ax", "ay", "az", "linmag", "stride", "fsr", "temp", "gx", "gy", "gz", "roll", "pitch"]
    for i, var in enumerate(hist_vars):
        if var in df.columns and i < len(axes):
            axes[i].hist(df[var], bins=40, color='skyblue', edgecolor='black', alpha=0.7)
            axes[i].set_title(f"Histogram of {var}")
            axes[i].set_xlabel(var)
            axes[i].set_ylabel("Frequency")
            axes[i].grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "enhanced_histograms.png"), dpi=300, bbox_inches='tight')
    plt.close()
def create_rolling_analysis():
    window = 100
    for var in ["ax", "ay", "az", "linmag", "temp"]:
        if var in df.columns:
            roll_mean = df[var].rolling(window).mean()
            roll_std = df[var].rolling(window).std()
            plt.figure(figsize=(12, 6))
            plt.plot(df["time"], df[var], label=f"{var}", alpha=0.6)
            plt.plot(df["time"], roll_mean, label=f"{var} rolling mean", linewidth=2)
            plt.fill_between(df["time"], roll_mean - roll_std, roll_mean + roll_std, alpha=0.3, label=f"{var} ±1σ")
            plt.legend()
            plt.title(f"{var} with Rolling Statistics")
            plt.xlabel("Time (s)")
            plt.ylabel(var)
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.savefig(os.path.join(out_dir, f"enhanced_roll_{var}.png"))
            plt.close()
def create_3d_analysis():
    if all(col in df.columns for col in ["ax", "ay", "az"]):
        fig = plt.figure(figsize=(15, 5))
        ax1 = fig.add_subplot(131, projection='3d')
        scatter = ax1.scatter(df["ax"], df["ay"], df["az"], c=df["time"], cmap='viridis', s=10, alpha=0.6)
        ax1.set_xlabel('Acceleration X (m/s²)')
        ax1.set_ylabel('Acceleration Y (m/s²)')
        ax1.set_zlabel('Acceleration Z (m/s²)')
        ax1.set_title('3D Acceleration Space')
        plt.colorbar(scatter, ax=ax1, label='Time (s)')
        ax2 = fig.add_subplot(132, projection='3d')
        ax2.plot(df["ax"], df["ay"], df["az"], alpha=0.7, linewidth=1)
        ax2.set_xlabel('Acceleration X (m/s²)')
        ax2.set_ylabel('Acceleration Y (m/s²)')
        ax2.set_zlabel('Acceleration Z (m/s²)')
        ax2.set_title('3D Acceleration Trajectory')
        if all(col in df.columns for col in ["roll", "pitch", "yaw"]):
            ax3 = fig.add_subplot(133, projection='3d')
            ax3.scatter(df["roll"], df["pitch"], df["yaw"], c=df["time"], cmap='plasma', s=10, alpha=0.6)
            ax3.set_xlabel('Roll (deg)')
            ax3.set_ylabel('Pitch (deg)')
            ax3.set_zlabel('Yaw (deg)')
            ax3.set_title('3D Orientation Space')
        plt.tight_layout()
        plt.savefig(os.path.join(out_dir, "enhanced_3d_analysis.png"), dpi=300, bbox_inches='tight')
        plt.close()
def perform_ml_analysis():
    try:
        ml_vars = ["ax", "ay", "az", "linmag", "temp"]
        ml_data = df[ml_vars].dropna()
        if len(ml_data) > 10:
            scaler = StandardScaler()
            ml_data_scaled = scaler.fit_transform(ml_data)
            pca = PCA(n_components=2)
            pca_result = pca.fit_transform(ml_data_scaled)
            kmeans = KMeans(n_clusters=3, random_state=42)
            clusters = kmeans.fit_predict(ml_data_scaled)
            plt.figure(figsize=(15, 5))
            plt.subplot(131)
            scatter = plt.scatter(pca_result[:, 0], pca_result[:, 1], c=clusters, cmap='viridis', alpha=0.6)
            plt.xlabel('PCA Component 1')
            plt.ylabel('PCA Component 2')
            plt.title('PCA Analysis')
            plt.colorbar(scatter, label='Cluster')
            plt.subplot(132)
            cluster_counts = np.bincount(clusters)
            plt.bar(range(len(cluster_counts)), cluster_counts)
            plt.xlabel('Cluster')
            plt.ylabel('Count')
            plt.title('Cluster Distribution')
            plt.subplot(133)
            feature_importance = np.abs(pca.components_[0])
            plt.bar(ml_vars, feature_importance)
            plt.xlabel('Features')
            plt.ylabel('Importance')
            plt.title('Feature Importance (PCA)')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(os.path.join(out_dir, "ml_analysis.png"), dpi=300, bbox_inches='tight')
            plt.close()
            summary_lines.append(f"\nML Analysis Results:")
            summary_lines.append(f"  Explained variance ratio: {pca.explained_variance_ratio_.sum():.3f}")
            summary_lines.append(f"  Cluster sizes: {cluster_counts.tolist()}")
    except Exception as e:
        summary_lines.append(f"ML analysis error: {str(e)}")
def perform_biomechanical_analysis():
    summary_lines.append("\n=== ADVANCED BIOMECHANICAL ANALYSIS ===\n")
    try:
        if all(col in df.columns for col in ["ax", "ay", "az"]):
            com_x = cumulative_trapezoid(cumulative_trapezoid(df["ax"], df["time"], initial=0), df["time"], initial=0)
            com_y = cumulative_trapezoid(cumulative_trapezoid(df["ay"], df["time"], initial=0), df["time"], initial=0)
            com_z = cumulative_trapezoid(cumulative_trapezoid(df["az"], df["time"], initial=0), df["time"], initial=0)
            com_magnitude = np.sqrt(com_x**2 + com_y**2 + com_z**2)
            com_stability = 1.0 / np.var(com_magnitude) if np.var(com_magnitude) > 0 else 0
            summary_lines.append(f"Movement stability (1/variance): {com_stability:.3f}")
            plt.figure(figsize=(12, 8))
            ax = plt.axes(projection='3d')
            ax.plot(com_x, com_y, com_z, alpha=0.7, linewidth=1)
            ax.set_xlabel('Cumulative X Movement (m)')
            ax.set_ylabel('Cumulative Y Movement (m)')
            ax.set_zlabel('Cumulative Z Movement (m)')
            ax.set_title('Cumulative Movement Trajectory')
            plt.tight_layout()
            plt.savefig(os.path.join(out_dir, "movement_trajectory.png"), dpi=300, bbox_inches='tight')
            plt.close()
        if "fsr" in df.columns:
            pressure_estimate = df["fsr"] / 4095.0
            pressure_mean = pressure_estimate.mean()
            pressure_peak = pressure_estimate.max()
            pressure_area = np.trapz(pressure_estimate, df["time"])
            summary_lines.append(f"Mean pressure: {pressure_mean:.3f} (normalized)")
            summary_lines.append(f"Peak pressure: {pressure_peak:.3f} (normalized)")
            summary_lines.append(f"Pressure-time integral: {pressure_area:.3f}")
            plt.figure(figsize=(12, 6))
            plt.plot(df["time"], pressure_estimate, linewidth=1.5, color='red', alpha=0.8)
            plt.xlabel("Time (s)")
            plt.ylabel("Pressure (normalized)")
            plt.title("Pressure Over Time")
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.savefig(os.path.join(out_dir, "pressure_analysis.png"), dpi=300, bbox_inches='tight')
            plt.close()
        if all(col in df.columns for col in ["roll", "pitch", "yaw"]):
            roll_range = df["roll"].max() - df["roll"].min()
            pitch_range = df["pitch"].max() - df["pitch"].min()
            yaw_range = df["yaw"].max() - df["yaw"].min()
            summary_lines.append(f"Roll range: {roll_range:.1f}°")
            summary_lines.append(f"Pitch range: {pitch_range:.1f}°")
            summary_lines.append(f"Yaw range: {yaw_range:.1f}°")
            roll_velocity = np.gradient(df["roll"], df["time"])
            pitch_velocity = np.gradient(df["pitch"], df["time"])
            yaw_velocity = np.gradient(df["yaw"], df["time"])
            summary_lines.append(f"Max roll velocity: {np.max(np.abs(roll_velocity)):.1f}°/s")
            summary_lines.append(f"Max pitch velocity: {np.max(np.abs(pitch_velocity)):.1f}°/s")
            summary_lines.append(f"Max yaw velocity: {np.max(np.abs(yaw_velocity)):.1f}°/s")
            plt.figure(figsize=(12, 6))
            plt.plot(df["time"], df["roll"], label="Roll", linewidth=1.5)
            plt.plot(df["time"], df["pitch"], label="Pitch", linewidth=1.5)
            plt.plot(df["time"], df["yaw"], label="Yaw", linewidth=1.5)
            plt.xlabel("Time (s)")
            plt.ylabel("Angle (°)")
            plt.title("Orientation Angles Over Time")
            plt.legend()
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.savefig(os.path.join(out_dir, "orientation_analysis.png"), dpi=300, bbox_inches='tight')
            plt.close()
    except Exception as e:
        summary_lines.append(f"Movement analysis error: {str(e)}")
def perform_advanced_signal_analysis():
    summary_lines.append("\n=== ADVANCED SIGNAL PROCESSING ===\n")
    try:
        from scipy import signal
        for var in ["linmag", "ax", "ay", "az"]:
            if var in df.columns:
                data = df[var].values
                widths = np.arange(1, 31)
                cwtmatr = signal.cwt(data, signal.ricker, widths)
                plt.figure(figsize=(12, 8))
                plt.imshow(np.abs(cwtmatr), extent=[df["time"].min(), df["time"].max(), 1, 30], aspect='auto', cmap='viridis')
                plt.colorbar(label='Wavelet Power')
                plt.xlabel('Time (s)')
                plt.ylabel('Scale')
                plt.title(f'{var} Wavelet Analysis')
                plt.tight_layout()
                plt.savefig(os.path.join(out_dir, f"wavelet_{var}.png"), dpi=300, bbox_inches='tight')
                plt.close()
                scale_power = np.sum(np.abs(cwtmatr), axis=1)
                dominant_scale = widths[np.argmax(scale_power)]
                summary_lines.append(f"{var} dominant wavelet scale: {dominant_scale}")
        if "linmag" in df.columns:
            data = df["linmag"].values
            analytic_signal = signal.hilbert(data)
            instantaneous_phase = np.unwrap(np.angle(analytic_signal))
            instantaneous_frequency = np.diff(instantaneous_phase) / (2.0 * np.pi) / np.mean(np.diff(df["time"]))
            plt.figure(figsize=(12, 8))
            plt.subplot(2, 1, 1)
            plt.plot(df["time"], data, label='Original Signal')
            plt.plot(df["time"], np.abs(analytic_signal), label='Envelope', alpha=0.7)
            plt.xlabel('Time (s)')
            plt.ylabel('Amplitude')
            plt.title('Hilbert Transform Analysis')
            plt.legend()
            plt.grid(True, alpha=0.3)
            plt.subplot(2, 1, 2)
            plt.plot(df["time"][1:], instantaneous_frequency, color='red')
            plt.xlabel('Time (s)')
            plt.ylabel('Instantaneous Frequency (Hz)')
            plt.title('Instantaneous Frequency')
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.savefig(os.path.join(out_dir, "hilbert_analysis.png"), dpi=300, bbox_inches='tight')
            plt.close()
            summary_lines.append(f"Mean instantaneous frequency: {np.mean(instantaneous_frequency):.2f} Hz")
    except Exception as e:
        summary_lines.append(f"Advanced signal processing error: {str(e)}")
def perform_predictive_analysis():
    summary_lines.append("\n=== PREDICTIVE MODELING ===\n")
    try:
        from sklearn.linear_model import LinearRegression
        from sklearn.model_selection import train_test_split
        from sklearn.metrics import mean_squared_error, r2_score
        feature_vars = ["ax", "ay", "az", "linmag", "temp", "gx", "gy", "gz"]
        target_vars = ["steps", "stride", "dist"]
        for target in target_vars:
            if target in df.columns:
                features = df[feature_vars].dropna()
                target_data = df[target].dropna()
                common_idx = features.index.intersection(target_data.index)
                if len(common_idx) > 50:
                    X = features.loc[common_idx]
                    y = target_data.loc[common_idx]
                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
                    model = LinearRegression()
                    model.fit(X_train, y_train)
                    y_pred = model.predict(X_test)
                    mse = mean_squared_error(y_test, y_pred)
                    r2 = r2_score(y_test, y_pred)
                    summary_lines.append(f"{target} prediction - MSE: {mse:.4f}, R²: {r2:.3f}")
                    feature_importance = np.abs(model.coef_)
                    feature_names = X.columns
                    plt.figure(figsize=(10, 6))
                    plt.bar(feature_names, feature_importance)
                    plt.xlabel('Features')
                    plt.ylabel('Coefficient Magnitude')
                    plt.title(f'{target} Prediction - Feature Importance')
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    plt.savefig(os.path.join(out_dir, f"prediction_{target}.png"), dpi=300, bbox_inches='tight')
                    plt.close()
    except Exception as e:
        summary_lines.append(f"Predictive modeling error: {str(e)}")
def perform_time_series_analysis():
    summary_lines.append("\n=== ADVANCED TIME SERIES ANALYSIS ===\n")
    try:
        from statsmodels.tsa.stattools import adfuller, kpss
        from statsmodels.tsa.seasonal import seasonal_decompose
        for var in ["linmag", "ax", "ay", "az"]:
            if var in df.columns:
                data = df[var].dropna()
                if len(data) > 100:
                    adf_result = adfuller(data)
                    kpss_result = kpss(data)
                    summary_lines.append(f"{var} - ADF p-value: {adf_result[1]:.4f}")
                    summary_lines.append(f"{var} - KPSS p-value: {kpss_result[1]:.4f}")
                    try:
                        decomposition = seasonal_decompose(data, period=min(50, len(data)//4), extrapolate_trend='freq')
                        plt.figure(figsize=(12, 10))
                        plt.subplot(411)
                        plt.plot(data.index, data, label='Original')
                        plt.legend()
                        plt.title(f'{var} Time Series Decomposition')
                        plt.subplot(412)
                        plt.plot(data.index, decomposition.trend, label='Trend')
                        plt.legend()
                        plt.subplot(413)
                        plt.plot(data.index, decomposition.seasonal, label='Seasonal')
                        plt.legend()
                        plt.subplot(414)
                        plt.plot(data.index, decomposition.resid, label='Residual')
                        plt.legend()
                        plt.tight_layout()
                        plt.savefig(os.path.join(out_dir, f"decomposition_{var}.png"), dpi=300, bbox_inches='tight')
                        plt.close()
                    except Exception as e:
                        summary_lines.append(f"Decomposition failed for {var}: {str(e)}")
    except Exception as e:
        summary_lines.append(f"Time series analysis error: {str(e)}")
def perform_advanced_gait_analysis():
    summary_lines.append("\n=== ADVANCED GAIT QUALITY ANALYSIS ===\n")
    try:
        if "steps" in df.columns and "linmag" in df.columns:
            step_diffs = df["steps"].diff().fillna(0)
            step_events = df[step_diffs > 0]["time"]            
            if len(step_events) > 5:
                step_intervals = step_events.diff().dropna()
                cv_step = np.std(step_intervals) / np.mean(step_intervals)
                if len(step_intervals) % 2 == 0:
                    left_steps = step_intervals[::2]
                    right_steps = step_intervals[1::2]
                    asymmetry_index = abs(np.mean(left_steps) - np.mean(right_steps)) / np.mean(step_intervals)
                else:
                    asymmetry_index = 0
                regularity_index = np.corrcoef(step_intervals[:-1], step_intervals[1:])[0, 1]
                def sample_entropy(data, m=2, r=0.2):
                    n = len(data)
                    if n < m + 2:
                        return 0
                    matches_m = 0
                    matches_m1 = 0
                    for i in range(n - m):
                        for j in range(i + 1, n - m):
                            if max(abs(data[i:i+m] - data[j:j+m])) <= r * np.std(data):
                                matches_m += 1
                                if max(abs(data[i:i+m+1] - data[j:j+m+1])) <= r * np.std(data):
                                    matches_m1 += 1
                    if matches_m == 0:
                        return 0
                    return -np.log(matches_m1 / matches_m)
                complexity = sample_entropy(step_intervals.values)
                summary_lines.append(f"Gait variability (CV): {cv_step:.3f}")
                summary_lines.append(f"Gait asymmetry index: {asymmetry_index:.3f}")
                summary_lines.append(f"Gait regularity index: {regularity_index:.3f}")
                summary_lines.append(f"Gait complexity (SampEn): {complexity:.3f}")
                gait_quality_score = (1 - cv_step) * regularity_index * (1 - asymmetry_index)
                summary_lines.append(f"Composite gait quality score: {gait_quality_score:.3f}")
                if gait_quality_score > 0.8:
                    quality_level = "Excellent"
                elif gait_quality_score > 0.6:
                    quality_level = "Good"
                elif gait_quality_score > 0.4:
                    quality_level = "Fair"
                else:
                    quality_level = "Poor"
                summary_lines.append(f"Gait quality level: {quality_level}")
    except Exception as e:
        summary_lines.append(f"Advanced gait analysis error: {str(e)}")
def generate_enhanced_insights():
    insights = []
    if 'linmag' in df.columns:
        avg_activity = df['linmag'].mean()
        activity_std = df['linmag'].std()
        if avg_activity < 5:
            insights.append("Low overall acceleration magnitude - minimal movement detected")
        elif avg_activity < 10:
            insights.append("Moderate acceleration magnitude - typical movement levels")
        else:
            insights.append("High acceleration magnitude - vigorous movement detected")
        if activity_std < 2:
            insights.append("Consistent movement pattern - low variability")
        elif activity_std > 5:
            insights.append("Highly variable movement pattern - mixed activity types")
    if 'gait_stats' in analysis_results:
        gait = analysis_results['gait_stats']
        if gait['symmetry'] > 0.8:
            insights.append("Excellent step pattern consistency - very regular intervals")
        elif gait['symmetry'] > 0.6:
            insights.append("Good step pattern consistency - relatively regular intervals")
        else:
            insights.append("Irregular step pattern - inconsistent intervals")
    if 'temp' in df.columns:
        temp_mean = df['temp'].mean()
        temp_var = df['temp'].var()
        temp_range = df['temp'].max() - df['temp'].min()
        if temp_var < 1:
            insights.append("Stable temperature - consistent environmental conditions")
        else:
            insights.append("Variable temperature - changing environmental conditions")
        if temp_range > 10:
            insights.append("Large temperature range - significant environmental changes")
    if 'fsr' in df.columns:
        fsr_range = df['fsr'].max() - df['fsr'].min()
        fsr_std = df['fsr'].std()
        if fsr_range < 1000:
            insights.append("Limited FSR range - sensor may have restricted dynamic range")
        else:
            insights.append("Good FSR range - sensor utilizing full dynamic range")
        
        if fsr_std < 100:
            insights.append("Low FSR variability - consistent pressure readings")
        else:
            insights.append("High FSR variability - dynamic pressure changes")
    total_samples = len(df)
    missing_data = df.isnull().sum().sum()
    data_quality = (total_samples - missing_data) / total_samples * 100
    insights.append(f"Data completeness: {data_quality:.1f}%")
    if 'linmag' in df.columns and 'fsr' in df.columns:
        high_accel_threshold = df['linmag'].mean() + 2*df['linmag'].std()
        high_impact_events = df[df['linmag'] > high_accel_threshold]
        if len(high_impact_events) > 0:
            insights.append(f"Detected {len(high_impact_events)} high-acceleration events")
        if 'velocity_stats' in analysis_results:
            vel_stats = analysis_results['velocity_stats']
            if vel_stats['mean_v'] > 2:
                insights.append("High average movement velocity - rapid motion")
            elif vel_stats['mean_v'] < 0.5:
                insights.append("Low average movement velocity - slow motion")
    if 'temp' in df.columns:
        temp_trend = np.polyfit(df['time'], df['temp'], 1)[0]
        if abs(temp_trend) > 0.1:
            insights.append("Significant temperature trend - changing environment")
        else:
            insights.append("Stable temperature trend - consistent environment")
    if all(col in df.columns for col in ["ax", "ay", "az", "gx", "gy", "gz"]):
        accel_trend = np.polyfit(df['time'], df['linmag'], 1)[0]
        gyro_trend = np.polyfit(df['time'], gyro_mag, 1)[0]
        if abs(accel_trend) > 0.01:
            insights.append("Accelerometer shows linear trend - possible drift or systematic change")
        if abs(gyro_trend) > 0.01:
            insights.append("Gyroscope shows linear trend - possible drift or systematic change")
    if 'steps' in df.columns and 'dist' in df.columns:
        if len(df) > 0:
            total_steps = df['steps'].max()
            total_distance = df['dist'].max()
            if total_steps > 0 and total_distance > 0:
                avg_step_distance = total_distance / total_steps
                insights.append(f"Average step distance: {avg_step_distance:.2f} meters")
                
                if avg_step_distance > 1.5:
                    insights.append("Long average step distance - large movements")
                elif avg_step_distance < 0.8:
                    insights.append("Short average step distance - small movements")
    recording_duration = df['time'].max() - df['time'].min()
    if recording_duration > 3600:
        insights.append("Long recording session - comprehensive data collection")
    elif recording_duration < 300:
        insights.append("Short recording session - limited data collection")
    if len(df) > 1:
        avg_dt = np.mean(np.diff(df['time']))
        sampling_rate = 1.0 / avg_dt
        insights.append(f"Average sampling rate: {sampling_rate:.1f} Hz")
        if sampling_rate > 50:
            insights.append("High sampling rate - detailed temporal resolution")
        elif sampling_rate < 10:
            insights.append("Low sampling rate - limited temporal resolution")
    return insights
create_enhanced_histograms()
create_rolling_analysis()
create_3d_analysis()
perform_ml_analysis()
perform_biomechanical_analysis()
perform_advanced_signal_analysis()
perform_predictive_analysis()
perform_time_series_analysis()
perform_advanced_gait_analysis()
insights = generate_enhanced_insights()
for insight in insights:
    summary_lines.append(f"• {insight}")
sns.pairplot(df[["ax", "ay", "az", "linmag", "fsr", "temp"]].dropna())
plt.savefig(os.path.join(out_dir, "pairplot.png"))
plt.close()
window = 200
rolling_corr = df[["ax", "ay", "az", "linmag"]].rolling(window).corr().unstack().iloc[window::window]
sns.heatmap(rolling_corr, cmap="coolwarm", center=0)
plt.title("Rolling Correlation Heatmap")
plt.savefig(os.path.join(out_dir, "rolling_corr_heatmap.png"))
plt.close()
with open(os.path.join(out_dir, "enhanced_summary.txt"), "w") as f:
    f.write("\n".join(summary_lines))
print("Enhanced analysis complete! Check the 'res' directory for all visualizations and the enhanced_summary.txt file for comprehensive results.")