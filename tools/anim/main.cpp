#include <GLFW/glfw3.h>
#define GLM_ENABLE_EXPERIMENTAL
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>
#include <glm/gtc/quaternion.hpp>
#include <glm/gtx/euler_angles.hpp>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <thread>
#include <chrono>
#include <atomic>
#ifdef __APPLE__
#define GL_SILENCE_DEPRECATION
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

struct DataRow {
    float time, roll, pitch, yaw, steps, stride, dist, fsr, fsrvar;
    float ax, ay, az, linmag, gravx, gravy, gravz, gx, gy, gz, temp;
};

template<typename T>
T clamp(T v, T lo, T hi) {
    return v < lo ? lo : (v > hi ? hi : v);
}

std::vector<DataRow> read_csv(const std::string& filename) {
    std::vector<DataRow> data;
    std::ifstream file(filename);
    std::string line;
    std::getline(file, line);
    while (std::getline(file, line)) {
        std::stringstream ss(line);
        std::string cell;
        DataRow row;
        std::getline(ss, cell, ','); row.time = std::stof(cell);
        std::getline(ss, cell, ','); row.roll = std::stof(cell);
        std::getline(ss, cell, ','); row.pitch = std::stof(cell);
        std::getline(ss, cell, ','); row.yaw = std::stof(cell);
        std::getline(ss, cell, ','); row.steps = std::stof(cell);
        std::getline(ss, cell, ','); row.stride = std::stof(cell);
        std::getline(ss, cell, ','); row.dist = std::stof(cell);
        std::getline(ss, cell, ','); row.fsr = std::stof(cell);
        std::getline(ss, cell, ','); row.fsrvar = std::stof(cell);
        std::getline(ss, cell, ','); row.ax = std::stof(cell);
        std::getline(ss, cell, ','); row.ay = std::stof(cell);
        std::getline(ss, cell, ','); row.az = std::stof(cell);
        std::getline(ss, cell, ','); row.linmag = std::stof(cell);
        std::getline(ss, cell, ','); row.gravx = std::stof(cell);
        std::getline(ss, cell, ','); row.gravy = std::stof(cell);
        std::getline(ss, cell, ','); row.gravz = std::stof(cell);
        std::getline(ss, cell, ','); row.gx = std::stof(cell);
        std::getline(ss, cell, ','); row.gy = std::stof(cell);
        std::getline(ss, cell, ','); row.gz = std::stof(cell);
        std::getline(ss, cell, ','); row.temp = std::stof(cell);
        data.push_back(row);
    }
    return data;
}

bool is_valley(const std::vector<DataRow>& data, size_t i, float threshold) {
    if (i == 0 || i+1 >= data.size()) return false;
    return (data[i-1].linmag > data[i].linmag) &&
           (data[i+1].linmag > data[i].linmag) &&
           (data[i].linmag < threshold);
}

void integrate(const std::vector<DataRow>& data, std::vector<glm::vec3>& positions, std::vector<glm::vec3>& velocities, std::vector<bool>& zupt_flags, std::vector<std::string>& zupt_reasons) {
    const float valley_threshold = -0.5f;
    const float acc_lp_alpha = 0.8f;
    const float velocity_decay = 0.99f;
    glm::vec3 velocity(0.0f);
    glm::vec3 position(0.0f);
    glm::vec3 acc_lp(0.0f);
    positions.clear();
    velocities.clear();
    zupt_flags.clear();
    zupt_reasons.clear();
    positions.reserve(data.size());
    velocities.reserve(data.size());
    zupt_flags.reserve(data.size());
    zupt_reasons.reserve(data.size());
    float prev_time = data[0].time;
    for (size_t i = 0; i < data.size(); ++i) {
        const auto& row = data[i];
        float dt = row.time - prev_time;
        prev_time = row.time;
        glm::vec3 acc(row.ax, row.ay, row.az);
        glm::vec3 grav(row.gravx, row.gravy, row.gravz);
        glm::vec3 acc_nograv = acc - grav;
        float roll = glm::radians(row.roll);
        float pitch = glm::radians(row.pitch);
        float yaw = glm::radians(row.yaw);
        glm::mat4 rot = glm::eulerAngleYXZ(yaw, pitch, roll);
        glm::vec3 acc_world = glm::vec3(rot * glm::vec4(acc_nograv, 0.0f));
        acc_lp = acc_lp_alpha * acc_lp + (1.0f - acc_lp_alpha) * acc_world;
        bool zupt_valley = is_valley(data, i, valley_threshold);
        bool zupt = zupt_valley;
        std::string reason = zupt ? "Valley" : "";
        if (zupt) velocity = glm::vec3(0.0f);
        else velocity += acc_lp * dt;
        velocity *= velocity_decay;
        position += velocity * dt;
        velocities.push_back(velocity);
        positions.push_back(position);
        zupt_flags.push_back(zupt);
        zupt_reasons.push_back(reason);
    }
}

glm::vec3 temp_to_color(float temp, float tmin, float tmax) {
    float norm = (temp - tmin) / (tmax - tmin);
    norm = clamp(norm, 0.0f, 1.0f);
    return glm::mix(glm::vec3(0,0,1), glm::vec3(1,0,0), norm);
}

float fsr_to_scale(float fsr, float fmin, float fmax) {
    float norm = (fsr - fmin) / (fmax - fmin);
    norm = clamp(norm, 0.5f, 2.0f);
    return norm;
}

void draw_axes() {
    glBegin(GL_LINES);
    glColor3f(1,0,0); glVertex3f(0,0,0); glVertex3f(1,0,0);
    glColor3f(0,1,0); glVertex3f(0,0,0); glVertex3f(0,1,0);
    glColor3f(0,0,1); glVertex3f(0,0,0); glVertex3f(0,0,1);
    glEnd();
}

void draw_cube(float scale) {
    glPushMatrix();
    glScalef(scale, scale, scale);
    glutSolidCube(1.0);
    glPopMatrix();
}

void find_min_max(const std::vector<glm::vec3>& positions, glm::vec3& min_pos, glm::vec3& max_pos) {
    if (positions.empty()) return;
    min_pos = max_pos = positions[0];
    for (const auto& p : positions) {
        min_pos.x = std::min(min_pos.x, p.x);
        min_pos.y = std::min(min_pos.y, p.y);
        min_pos.z = std::min(min_pos.z, p.z);
        max_pos.x = std::max(max_pos.x, p.x);
        max_pos.y = std::max(max_pos.y, p.y);
        max_pos.z = std::max(max_pos.z, p.z);
    }
}

glm::vec3 normalize_pos(const glm::vec3& pos, const glm::vec3& min_pos, const glm::vec3& max_pos) {
    glm::vec3 center = 0.5f * (min_pos + max_pos);
    glm::vec3 size = max_pos - min_pos;
    float max_extent = std::max({size.x, size.y, size.z, 1e-3f});
    return (pos - center) / max_extent * 4.0f;
}

void draw_trail(const std::vector<glm::vec3>& positions, size_t up_to, const glm::vec3& min_pos, const glm::vec3& max_pos) {
    glBegin(GL_LINE_STRIP);
    glColor3f(1,1,0);
    for (size_t i = 0; i <= up_to && i < positions.size(); ++i) {
        glm::vec3 p = normalize_pos(positions[i], min_pos, max_pos);
        glVertex3f(p.x, p.y, p.z);
    }
    glEnd();
}

void draw_arrow(const glm::vec3& from, const glm::vec3& to, float r, float g, float b, const char* label) {
    glColor3f(r, g, b);
    glBegin(GL_LINES);
    glVertex3f(from.x, from.y, from.z);
    glVertex3f(to.x, to.y, to.z);
    glEnd();
    glPushMatrix();
    glTranslatef(to.x, to.y, to.z);
    glutSolidCone(0.05, 0.15, 8, 2);
    glPopMatrix();
    glColor3f(1,1,1);
    glRasterPos3f(to.x, to.y, to.z);
    for (const char* c = label; *c; ++c) {
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, *c);
    }
}

void draw_overlay_text(float x, float y, const char* text) {
    glMatrixMode(GL_PROJECTION);
    glPushMatrix();
    glLoadIdentity();
    int viewport[4];
    glGetIntegerv(GL_VIEWPORT, viewport);
    gluOrtho2D(0, viewport[2], 0, viewport[3]);
    glMatrixMode(GL_MODELVIEW);
    glPushMatrix();
    glLoadIdentity();
    glColor3f(1,1,1);
    glRasterPos2f(x, viewport[3] - y);
    for (const char* c = text; *c; ++c) {
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, *c);
    }
    glPopMatrix();
    glMatrixMode(GL_PROJECTION);
    glPopMatrix();
    glMatrixMode(GL_MODELVIEW);
}

std::atomic<bool> paused{false};
std::atomic<bool> step_fwd{false};
std::atomic<bool> step_back{false};

void key_callback(GLFWwindow* window, int key, int scancode, int action, int mods) {
    if (action == GLFW_PRESS) {
        if (key == GLFW_KEY_SPACE) paused = !paused;
        if (key == GLFW_KEY_RIGHT) step_fwd = true;
        if (key == GLFW_KEY_LEFT) step_back = true;
    }
}

int main() {
    auto data = read_csv("data.csv");
    std::vector<glm::vec3> positions, velocities;
    std::vector<bool> zupt_flags;
    std::vector<std::string> zupt_reasons;
    integrate(data, positions, velocities, zupt_flags, zupt_reasons);
    float tmin = data[0].temp, tmax = data[0].temp;
    float fmin = data[0].fsr, fmax = data[0].fsr;
    for (const auto& row : data) {
        tmin = std::min(tmin, row.temp);
        tmax = std::max(tmax, row.temp);
        fmin = std::min(fmin, row.fsr);
        fmax = std::max(fmax, row.fsr);
    }
    glm::vec3 min_pos, max_pos;
    find_min_max(positions, min_pos, max_pos);
    int argc = 1;
    char* argv[1] = {(char*)""};
    glutInit(&argc, argv);
    if (!glfwInit()) return -1;
    GLFWwindow* window = glfwCreateWindow(800, 600, "SmartSole Animation", NULL, NULL);
    if (!window) { glfwTerminate(); return -1; }
    glfwMakeContextCurrent(window);
    glfwSetKeyCallback(window, key_callback);
    glEnable(GL_DEPTH_TEST);
    glClearColor(0.1f, 0.1f, 0.1f, 1.0f);
    size_t frame = 0;
    while (!glfwWindowShouldClose(window)) {
        int width, height;
        glfwGetFramebufferSize(window, &width, &height);
        glViewport(0, 0, width, height);
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        gluPerspective(45, (double)width/height, 0.1, 100);
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();
        gluLookAt(0,2,8, 0,0,0, 0,1,0);
        draw_axes();
        if (frame >= data.size()) frame = 0;
        const auto& row = data[frame];
        glm::vec3 color = temp_to_color(row.temp, tmin, tmax);
        float scale = 1.0f; // Fixed scale for debug
        // Draw trail
        draw_trail(positions, frame, min_pos, max_pos);
        // Draw moving cube at normalized position
        glm::vec3 pos = normalize_pos(positions[frame], min_pos, max_pos);
        glPushMatrix();
        glTranslatef(pos.x, pos.y, pos.z);
        glRotatef(row.yaw, 0,1,0);
        glRotatef(row.pitch, 1,0,0);
        glRotatef(row.roll, 0,0,1);
        if (tmax == tmin) glColor3f(0.8f, 0.8f, 0.8f);
        else glColor3f(color.r, color.g, color.b);
        draw_cube(scale);
        glPopMatrix();
        // Draw velocity and force vectors at current position
        glm::vec3 vel = velocities[frame];
        glm::vec3 force(row.ax, row.ay, row.az); // mass=1
        glm::vec3 grav(row.gravx, row.gravy, row.gravz);
        glm::vec3 linacc(row.ax, row.ay, row.az); // linear acc = ax,ay,az
        glm::vec3 omega(row.gx, row.gy, row.gz); // gyroscope
        glm::vec3 acc_nograv = linacc - grav;
        // Scale vectors for visibility
        float v_scale = 1.0f, f_scale = 1.0f, g_scale = 1.0f, a_scale = 1.0f, o_scale = 1.0f;
        if (glm::length(vel) > 1e-6f)
            draw_arrow(pos, pos + glm::normalize(vel) * v_scale * glm::length(vel), 0,1,1, "v"); // cyan
        if (glm::length(force) > 1e-6f)
            draw_arrow(pos, pos + glm::normalize(force) * f_scale * glm::length(force), 1,0,1, "F"); // magenta
        if (glm::length(grav) > 1e-6f)
            draw_arrow(pos, pos + glm::normalize(grav) * g_scale * glm::length(grav), 0,1,0, "g"); // green
        if (glm::length(linacc) > 1e-6f)
            draw_arrow(pos, pos + glm::normalize(linacc) * a_scale * glm::length(linacc), 1,0.5,0, "a_lin"); // orange
        if (glm::length(omega) > 1e-6f)
            draw_arrow(pos, pos + glm::normalize(omega) * o_scale * glm::length(omega), 0,0,1, "omega"); // blue
        // Draw temperature as floating label
        char tempbuf[64];
        snprintf(tempbuf, sizeof(tempbuf), "Temp: %.2f C", row.temp);
        glColor3f(1,1,1);
        glRasterPos3f(pos.x, pos.y + 0.5f, pos.z);
        for (const char* c = tempbuf; *c; ++c) glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, *c);
        // Draw overlay info (steps, stride, dist)
        char infobuf[128];
        snprintf(infobuf, sizeof(infobuf), "Step: %.0f  Stride: %.2f  Dist: %.2f", row.steps, row.stride, row.dist);
        draw_overlay_text(10, 30, infobuf);
        // Show ZUPT status
        if (zupt_flags[frame]) {
            std::string msg = "ZUPT: Velocity reset (" + zupt_reasons[frame] + ")";
            draw_overlay_text(10, 45, msg.c_str());
        }
        // Show vector magnitudes
        char magbuf[128];
        snprintf(magbuf, sizeof(magbuf), "v: %.2f (velocity, m/s) [gravity-compensated]", glm::length(vel));
        draw_overlay_text(10, 55, magbuf);
        snprintf(magbuf, sizeof(magbuf), "F: %.2f (force, N, = mass*acc)", glm::length(force));
        draw_overlay_text(10, 75, magbuf);
        snprintf(magbuf, sizeof(magbuf), "g: %.2f (gravity, m/s^2)", glm::length(grav));
        draw_overlay_text(10, 95, magbuf);
        snprintf(magbuf, sizeof(magbuf), "a_lin: %.2f (linear acc, m/s^2)", glm::length(linacc));
        draw_overlay_text(10, 115, magbuf);
        snprintf(magbuf, sizeof(magbuf), "a_nograv: %.2f (acc - gravity, m/s^2)", glm::length(acc_nograv));
        draw_overlay_text(10, 135, magbuf);
        snprintf(magbuf, sizeof(magbuf), "omega: %.2f (angular vel, deg/s)", glm::length(omega));
        draw_overlay_text(10, 155, magbuf);
        // Show warning
        draw_overlay_text(10, 180, "WARNING: Integrated velocity drifts due to IMU noise!");
        // Show legend
        draw_overlay_text(10, 210, "Legend:");
        draw_overlay_text(10, 230, "v = velocity vector (cyan, world frame, ZUPT)");
        draw_overlay_text(10, 250, "F = force/acceleration (magenta)");
        draw_overlay_text(10, 270, "g = gravity (green)");
        draw_overlay_text(10, 290, "a_lin = linear acceleration (orange)");
        draw_overlay_text(10, 310, "a_nograv = acc - gravity (yellow)");
        draw_overlay_text(10, 330, "omega = angular velocity (blue)");
        draw_overlay_text(10, 350, "ZUPT: Zero-Velocity Update (velocity reset when foot on ground)");
        // Show PAUSED overlay if paused
        if (paused) draw_overlay_text(10, 160, "PAUSED (space to resume, arrows to step)");
        glfwSwapBuffers(window);
        glfwPollEvents();
        // Playback control logic
        if (!paused) {
            frame++;
        } else if (step_fwd) {
            frame = (frame + 1) % data.size();
            step_fwd = false;
        } else if (step_back) {
            frame = (frame == 0 ? data.size() - 1 : frame - 1);
            step_back = false;
        }
        std::this_thread::sleep_for(std::chrono::milliseconds(16)); // ~60 FPS
    }
    glfwTerminate();
    return 0;
} 