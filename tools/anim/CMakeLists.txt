cmake_minimum_required(VERSION 3.10)
project(SmartSoleAnim)
set(CMAKE_CXX_STANDARD 17)

find_package(OpenGL REQUIRED)
find_package(GLUT REQUIRED)

# Homebrew paths for Apple Silicon
include_directories(/opt/homebrew/include)
link_directories(/opt/homebrew/lib)

add_executable(main main.cpp)
target_link_libraries(main ${OPENGL_LIBRARIES} ${GLUT_LIBRARIES} glfw glm)