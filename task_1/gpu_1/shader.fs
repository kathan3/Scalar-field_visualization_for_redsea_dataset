#version 460 core
in vec3 vPosition;
out vec4 FragColor;

uniform sampler3D scalarFieldTexture;
uniform sampler1D colormapTexture;

uniform vec3 minPoint;
uniform vec3 maxPoint;

uniform float scalarMin;
uniform float scalarMax;

void main() {
    vec3 texCoord = (vPosition - minPoint) / (maxPoint - minPoint);
    if(texCoord.x < 0.0 || texCoord.x > 1.0 || texCoord.y < 0.0 || texCoord.y > 1.0 || texCoord.z < 0.0 || texCoord.z > 1.0){
        FragColor = vec4(1.0, 0.0, 0.0, 1.0);
        return;
    }
    float scalarValue = texture(scalarFieldTexture, texCoord).r;
    float normalizedScalar = (scalarValue - scalarMin) / (scalarMax - scalarMin);
    normalizedScalar = clamp(normalizedScalar, 0.0, 1.0);
    vec3 color = texture(colormapTexture, normalizedScalar).rgb;
    FragColor = vec4(color, 1.0);
}