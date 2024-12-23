#version 460 core
layout(location = 0) in vec3 aPos;

out vec3 vPosition; // Pass the position to the fragment shader

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main() {
    vPosition = aPos;
    gl_Position = projection * view * model * vec4(aPos, 1.0);
}