#version 460 core
layout(location = 0) in ivec3 aVoxelPos;

void main() {
    gl_Position = vec4(aVoxelPos, 1);
}
