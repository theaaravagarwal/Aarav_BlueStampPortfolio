from scipy.spatial.transform import Rotation as R
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
import os
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
    run_num += 1
out_dir = f"run{run_num}"
os.makedirs(out_dir, exist_ok=True)
def plot_cube(ax, R_mat):
    r = [-0.5, 0.5]
    X, Y = np.meshgrid(r, r)
    ones = np.ones_like(X)
    zeros = np.zeros_like(X)
    faces = [
        np.stack([X, Y, 0.5*ones], axis=-1),  # top
        np.stack([X, Y, -0.5*ones], axis=-1), # bottom
        np.stack([X, 0.5*ones, Y], axis=-1),  # front
        np.stack([X, -0.5*ones, Y], axis=-1), # back
        np.stack([0.5*ones, X, Y], axis=-1),  # right
        np.stack([-0.5*ones, X, Y], axis=-1), # left
    ]
    for face in faces:
        face[:] = face @ R_mat.T
    for face in faces:
        ax.plot_surface(face[...,0], face[...,1], face[...,2], color='cyan', edgecolor='k', alpha=0.5)
N = len(df) #w/o subset cuz its only 2000 data points, to use subset just add a min and then the num u want for the subset len
rolls = df["roll"].values[:N]
pitches = df["pitch"].values[:N]
yaws = df["yaw"].values[:N]
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])
ax.set_box_aspect([1,1,1])
ax.set_title("Cube Orientation (Roll, Pitch, Yaw)")
cube_surfaces = []
def init():
    ax.cla()
    ax.set_xlim([-1,1])
    ax.set_ylim([-1,1])
    ax.set_zlim([-1,1])
    ax.set_box_aspect([1,1,1])
    ax.set_title("Cube Orientation (Roll, Pitch, Yaw)")
def animate(i):
    ax.cla()
    ax.set_xlim([-1,1])
    ax.set_ylim([-1,1])
    ax.set_zlim([-1,1])
    ax.set_box_aspect([1,1,1])
    current_time = df["time"].values[i]
    ax.set_title(f"Cube Orientation\nTime: {current_time:.2f} s")
    rot = R.from_euler('xyz', [rolls[i], pitches[i], yaws[i]], degrees=True)
    plot_cube(ax, rot.as_matrix())
    origin = np.zeros(3)
    axes = np.eye(3)
    axes_rot = rot.apply(axes)
    colors = ['r', 'g', 'b']
    for j in range(3):
        ax.quiver(*origin, *axes_rot[j], color=colors[j], length=0.7, linewidth=2)
ani = animation.FuncAnimation(fig, animate, frames=N, init_func=init, interval=100, blit=False)
gif_path = os.path.join(out_dir, "cube_orientation.gif")
ani.save(gif_path, writer='pillow')
print(f"Saved cube orientation animation to {gif_path}")
plt.show()
