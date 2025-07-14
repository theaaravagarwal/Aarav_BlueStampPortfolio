# SmartSole C++ Animation

## Dependencies (macOS)

Install dependencies with Homebrew:

```sh
brew install glfw glm cmake
```

GLUT and OpenGL are included with macOS.

## Build

```sh
cmake -B build
cmake --build build
```

## Run

Place your `data.csv` in the same directory as the executable (or edit the path in `main.cpp`).

```sh
./build/main
```

## What it does
- Reads your CSV data
- Integrates acceleration to estimate velocity/displacement
- Animates a cube in 3D using OpenGL
- Cube orientation = roll, pitch, yaw
- Cube position = integrated displacement
- Cube color = temperature
- Cube scale = fsr
- Axes are shown for reference

---

If you want to change how data is visualized, edit `main.cpp` as needed. 