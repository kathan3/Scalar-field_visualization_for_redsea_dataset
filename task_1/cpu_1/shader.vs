#version 460 core
layout(location = 0) in vec3 aPos;
layout(location = 1) in vec3 aColor; // For plane vertices; not used by bounding box

out vec3 vColor;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

uniform bool useVertexColor; // Determines whether to use vertex colors
uniform vec3 solidColor;     // Color to use when not using vertex colors

void main() {
    if (useVertexColor) {
        vColor = aColor;
    } else {
        vColor = solidColor;
    }
    gl_Position = projection * view * model * vec4(aPos, 1.0);
}
