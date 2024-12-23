#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string.h>
#include <stdlib.h>
#include <string>
#include <GL/glew.h>
#include <GLFW/glfw3.h>

#include "file_utils.h"
#include "math_utils.h"
#include "vtk_filereader.h"
#include <glm/glm.hpp>
#include <glm/gtc/type_ptr.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>
#include <glm/gtx/string_cast.hpp>

struct vt {
    glm::vec3 position;  
    float scalarValue;   
    glm::vec3 color;    
};

VTKFileReader vtk_file;
std::vector<glm::vec3> gridPoints;
std::vector<glm::vec3> boundingBoxVertices;
std::vector<vt> planeVertices;
std::vector<unsigned int> planeIndices;
std::vector<unsigned int> boundingBoxIndices = {
	0, 1, 1, 2, 2, 3, 3, 0,
	4, 5, 5, 6, 6, 7, 7, 4,
	0, 4, 1, 5, 2, 6, 3, 7
};
float minValue = INT_MAX, maxValue = INT_MIN;
GLuint boundingBoxVAO, boundingBoxVBO, boundingBoxEBO;
GLuint isoVAO = 0, isoVBO = 0, isoColorVBO = 0;

glm::vec3 cameraFront, cameraUp, viewDirection, cameraPos, center;
glm::vec3 minPoint, maxPoint;
float offset = 30;

std::string selectedField = "SALT";
int prevAxis = -1;
float prevOffset = offset;

std::string theProgramTitle = "Sample";
int theWindowWidth = 700, theWindowHeight = 700;
int theWindowPositionX = 40, theWindowPositionY = 40;
bool isFullScreen = false;
bool isAnimating = true;
float rotation = 0.0f;


GLuint VBO, VAO;
GLuint modelLoc, viewLoc, projLoc, useVertexColorLoc, solidColorLoc;

const int ANIMATION_DELAY = 20; 
const char* pVSFileName = "shader.vs";
const char* pFSFileName = "shader.fs";

void computeFPS(GLFWwindow* window) {
    static int frameCount = 0;
    static double lastTime = 0.0;
    static std::string title;

    frameCount++;
    double currentTime = glfwGetTime(); 

    if (currentTime - lastTime >= 1.0) { // If one second has passed
        double fps = frameCount / (currentTime - lastTime);

        title = theProgramTitle + " [ FPS: " + std::to_string(fps) + " ]";
        glfwSetWindowTitle(window, title.c_str());

        lastTime = currentTime;
        frameCount = 0;
    }
}

static void CreateVertexBuffer() {
	glGenVertexArrays(1, &boundingBoxVAO);
	glBindVertexArray(boundingBoxVAO);

	glGenBuffers(1, &boundingBoxVBO);
	glBindBuffer(GL_ARRAY_BUFFER, boundingBoxVBO);
	glBufferData(GL_ARRAY_BUFFER, boundingBoxVertices.size() * sizeof(glm::vec3), boundingBoxVertices.data(), GL_STATIC_DRAW);

	glGenBuffers(1, &boundingBoxEBO);
	glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, boundingBoxEBO);
	glBufferData(GL_ELEMENT_ARRAY_BUFFER, boundingBoxIndices.size() * sizeof(unsigned int), boundingBoxIndices.data(), GL_STATIC_DRAW);

	glEnableVertexAttribArray(0);
	glVertexAttribPointer(
		0,                  
		3,                
		GL_FLOAT,           
		GL_FALSE,           
		sizeof(glm::vec3),  
		(void*)0            
	);

	glBindVertexArray(0);

}

static void AddShader(GLuint ShaderProgram, const char* pShaderText, GLenum ShaderType) {
	GLuint ShaderObj = glCreateShader(ShaderType);

	if (ShaderObj == 0) {
		fprintf(stderr, "Error creating shader type %d\n", ShaderType);
		exit(0);
	}

	const GLchar * p[1];
	p[0] = pShaderText;
	GLint Lengths[1];
	Lengths[0] = strlen(pShaderText);
	glShaderSource(ShaderObj, 1, p, Lengths);
	glCompileShader(ShaderObj);
	GLint success;
	glGetShaderiv(ShaderObj, GL_COMPILE_STATUS, &success);
	if (!success) {
		GLchar InfoLog[1024];
		glGetShaderInfoLog(ShaderObj, 1024, NULL, InfoLog);
		fprintf(stderr, "Error compiling shader type %d: '%s'\n", ShaderType, InfoLog);
		exit(1);
	}

	glAttachShader(ShaderProgram, ShaderObj);
}

using namespace std;

static void CompileShaders() {
	GLuint ShaderProgram = glCreateProgram();

	if (ShaderProgram == 0) {
		fprintf(stderr, "Error creating shader program\n");
		exit(1);
	}

	string vs, fs;

	if (!ReadFile(pVSFileName, vs)) {
		exit(1);
	}

	if (!ReadFile(pFSFileName, fs)) {
		exit(1);
	}

	AddShader(ShaderProgram, vs.c_str(), GL_VERTEX_SHADER);
	AddShader(ShaderProgram, fs.c_str(), GL_FRAGMENT_SHADER);

	GLint Success = 0;
	GLchar ErrorLog[1024] = {0};

	glLinkProgram(ShaderProgram);
	glGetProgramiv(ShaderProgram, GL_LINK_STATUS, &Success);
	if (Success == 0) {
		glGetProgramInfoLog(ShaderProgram, sizeof (ErrorLog), NULL, ErrorLog);
		fprintf(stderr, "Error linking shader program: '%s'\n", ErrorLog);
		exit(1);
	}

	glValidateProgram(ShaderProgram);
	glGetProgramiv(ShaderProgram, GL_VALIDATE_STATUS, &Success);
	if (!Success) {
		glGetProgramInfoLog(ShaderProgram, sizeof (ErrorLog), NULL, ErrorLog);
		fprintf(stderr, "Invalid shader program: '%s'\n", ErrorLog);
		exit(1);
	}

	glUseProgram(ShaderProgram);
	modelLoc = glGetUniformLocation(ShaderProgram, "model");
	viewLoc = glGetUniformLocation(ShaderProgram, "view");
	projLoc = glGetUniformLocation(ShaderProgram, "projection");
	useVertexColorLoc = glGetUniformLocation(ShaderProgram, "useVertexColor");
	solidColorLoc= glGetUniformLocation(ShaderProgram, "solidColor");

}

float GetScalarValue(int i, int j, int k) {
    if (i < 0 || i >= vtk_file.dimensions.x || 
        j < 0 || j >= vtk_file.dimensions.y || 
        k < 0 || k >= vtk_file.dimensions.z) {
        throw std::out_of_range("Indices are out of range");
    }

    int index = i + vtk_file.dimensions.x * (j + vtk_file.dimensions.y * k);
    return vtk_file.fieldData[selectedField][index];
}

std::vector<glm::vec3> isoVertices;
std::vector<glm::vec3> isoColors;

const int ETIndices[12][2] = {
    {0, 1}, {1, 3}, {3, 2}, {2, 0},
    {4, 5}, {5, 7}, {7, 6}, {6, 4},
    {0, 4}, {1, 5}, {3, 7}, {2, 6}
};

const int ETs[] = {
	0x0, 0x109, 0x203, 0x30a, 0x80c, 0x905, 0xa0f, 0xb06, 
	0x406, 0x50f, 0x605, 0x70c, 0xc0a, 0xd03, 0xe09, 0xf00, 
	0x190, 0x99, 0x393, 0x29a, 0x99c, 0x895, 0xb9f, 0xa96, 
	0x596, 0x49f, 0x795, 0x69c, 0xd9a, 0xc93, 0xf99, 0xe90, 
	0x230, 0x339, 0x33, 0x13a, 0xa3c, 0xb35, 0x83f, 0x936, 
	0x636, 0x73f, 0x435, 0x53c, 0xe3a, 0xf33, 0xc39, 0xd30, 
	0x3a0, 0x2a9, 0x1a3, 0xaa, 0xbac, 0xaa5, 0x9af, 0x8a6, 
	0x7a6, 0x6af, 0x5a5, 0x4ac, 0xfaa, 0xea3, 0xda9, 0xca0, 
	0x8c0, 0x9c9, 0xac3, 0xbca, 0xcc, 0x1c5, 0x2cf, 0x3c6, 
	0xcc6, 0xdcf, 0xec5, 0xfcc, 0x4ca, 0x5c3, 0x6c9, 0x7c0, 
	0x950, 0x859, 0xb53, 0xa5a, 0x15c, 0x55, 0x35f, 0x256, 
	0xd56, 0xc5f, 0xf55, 0xe5c, 0x55a, 0x453, 0x759, 0x650, 
	0xaf0, 0xbf9, 0x8f3, 0x9fa, 0x2fc, 0x3f5, 0xff, 0x1f6, 
	0xef6, 0xfff, 0xcf5, 0xdfc, 0x6fa, 0x7f3, 0x4f9, 0x5f0, 
	0xb60, 0xa69, 0x963, 0x86a, 0x36c, 0x265, 0x16f, 0x66, 
	0xf66, 0xe6f, 0xd65, 0xc6c, 0x76a, 0x663, 0x569, 0x460, 
	0x460, 0x569, 0x663, 0x76a, 0xc6c, 0xd65, 0xe6f, 0xf66, 
	0x66, 0x16f, 0x265, 0x36c, 0x86a, 0x963, 0xa69, 0xb60, 
	0x5f0, 0x4f9, 0x7f3, 0x6fa, 0xdfc, 0xcf5, 0xfff, 0xef6, 
	0x1f6, 0xff, 0x3f5, 0x2fc, 0x9fa, 0x8f3, 0xbf9, 0xaf0, 
	0x650, 0x759, 0x453, 0x55a, 0xe5c, 0xf55, 0xc5f, 0xd56, 
	0x256, 0x35f, 0x55, 0x15c, 0xa5a, 0xb53, 0x859, 0x950, 
	0x7c0, 0x6c9, 0x5c3, 0x4ca, 0xfcc, 0xec5, 0xdcf, 0xcc6, 
	0x3c6, 0x2cf, 0x1c5, 0xcc, 0xbca, 0xac3, 0x9c9, 0x8c0, 
	0xca0, 0xda9, 0xea3, 0xfaa, 0x4ac, 0x5a5, 0x6af, 0x7a6, 
	0x8a6, 0x9af, 0xaa5, 0xbac, 0xaa, 0x1a3, 0x2a9, 0x3a0, 
	0xd30, 0xc39, 0xf33, 0xe3a, 0x53c, 0x435, 0x73f, 0x636, 
	0x936, 0x83f, 0xb35, 0xa3c, 0x13a, 0x33, 0x339, 0x230, 
	0xe90, 0xf99, 0xc93, 0xd9a, 0x69c, 0x795, 0x49f, 0x596, 
	0xa96, 0xb9f, 0x895, 0x99c, 0x29a, 0x393, 0x99, 0x190, 
	0xf00, 0xe09, 0xd03, 0xc0a, 0x70c, 0x605, 0x50f, 0x406, 
	0xb06, 0xa0f, 0x905, 0x80c, 0x30a, 0x203, 0x109, 0x0, 
};

const int TT[256][16] = {
	{ -1 },
	{ 0, 3, 8, -1 },
	{ 0, 9, 1, -1 },
	{ 3, 8, 1, 1, 8, 9, -1 },
	{ 2, 11, 3, -1 },
	{ 8, 0, 11, 11, 0, 2, -1 },
	{ 3, 2, 11, 1, 0, 9, -1 },
	{ 11, 1, 2, 11, 9, 1, 11, 8, 9, -1 },
	{ 1, 10, 2, -1 },
	{ 0, 3, 8, 2, 1, 10, -1 },
	{ 10, 2, 9, 9, 2, 0, -1 },
	{ 8, 2, 3, 8, 10, 2, 8, 9, 10, -1 },
	{ 11, 3, 10, 10, 3, 1, -1 },
	{ 10, 0, 1, 10, 8, 0, 10, 11, 8, -1 },
	{ 9, 3, 0, 9, 11, 3, 9, 10, 11, -1 },
	{ 8, 9, 11, 11, 9, 10, -1 },
	{ 4, 8, 7, -1 },
	{ 7, 4, 3, 3, 4, 0, -1 },
	{ 4, 8, 7, 0, 9, 1, -1 },
	{ 1, 4, 9, 1, 7, 4, 1, 3, 7, -1 },
	{ 8, 7, 4, 11, 3, 2, -1 },
	{ 4, 11, 7, 4, 2, 11, 4, 0, 2, -1 },
	{ 0, 9, 1, 8, 7, 4, 11, 3, 2, -1 },
	{ 7, 4, 11, 11, 4, 2, 2, 4, 9, 2, 9, 1, -1 },
	{ 4, 8, 7, 2, 1, 10, -1 },
	{ 7, 4, 3, 3, 4, 0, 10, 2, 1, -1 },
	{ 10, 2, 9, 9, 2, 0, 7, 4, 8, -1 },
	{ 10, 2, 3, 10, 3, 4, 3, 7, 4, 9, 10, 4, -1 },
	{ 1, 10, 3, 3, 10, 11, 4, 8, 7, -1 },
	{ 10, 11, 1, 11, 7, 4, 1, 11, 4, 1, 4, 0, -1 },
	{ 7, 4, 8, 9, 3, 0, 9, 11, 3, 9, 10, 11, -1 },
	{ 7, 4, 11, 4, 9, 11, 9, 10, 11, -1 },
	{ 9, 4, 5, -1 },
	{ 9, 4, 5, 8, 0, 3, -1 },
	{ 4, 5, 0, 0, 5, 1, -1 },
	{ 5, 8, 4, 5, 3, 8, 5, 1, 3, -1 },
	{ 9, 4, 5, 11, 3, 2, -1 },
	{ 2, 11, 0, 0, 11, 8, 5, 9, 4, -1 },
	{ 4, 5, 0, 0, 5, 1, 11, 3, 2, -1 },
	{ 5, 1, 4, 1, 2, 11, 4, 1, 11, 4, 11, 8, -1 },
	{ 1, 10, 2, 5, 9, 4, -1 },
	{ 9, 4, 5, 0, 3, 8, 2, 1, 10, -1 },
	{ 2, 5, 10, 2, 4, 5, 2, 0, 4, -1 },
	{ 10, 2, 5, 5, 2, 4, 4, 2, 3, 4, 3, 8, -1 },
	{ 11, 3, 10, 10, 3, 1, 4, 5, 9, -1 },
	{ 4, 5, 9, 10, 0, 1, 10, 8, 0, 10, 11, 8, -1 },
	{ 11, 3, 0, 11, 0, 5, 0, 4, 5, 10, 11, 5, -1 },
	{ 4, 5, 8, 5, 10, 8, 10, 11, 8, -1 },
	{ 8, 7, 9, 9, 7, 5, -1 },
	{ 3, 9, 0, 3, 5, 9, 3, 7, 5, -1 },
	{ 7, 0, 8, 7, 1, 0, 7, 5, 1, -1 },
	{ 7, 5, 3, 3, 5, 1, -1 },
	{ 5, 9, 7, 7, 9, 8, 2, 11, 3, -1 },
	{ 2, 11, 7, 2, 7, 9, 7, 5, 9, 0, 2, 9, -1 },
	{ 2, 11, 3, 7, 0, 8, 7, 1, 0, 7, 5, 1, -1 },
	{ 2, 11, 1, 11, 7, 1, 7, 5, 1, -1 },
	{ 8, 7, 9, 9, 7, 5, 2, 1, 10, -1 },
	{ 10, 2, 1, 3, 9, 0, 3, 5, 9, 3, 7, 5, -1 },
	{ 7, 5, 8, 5, 10, 2, 8, 5, 2, 8, 2, 0, -1 },
	{ 10, 2, 5, 2, 3, 5, 3, 7, 5, -1 },
	{ 8, 7, 5, 8, 5, 9, 11, 3, 10, 3, 1, 10, -1 },
	{ 5, 11, 7, 10, 11, 5, 1, 9, 0, -1 },
	{ 11, 5, 10, 7, 5, 11, 8, 3, 0, -1 },
	{ 5, 11, 7, 10, 11, 5, -1 },
	{ 6, 7, 11, -1 },
	{ 7, 11, 6, 3, 8, 0, -1 },
	{ 6, 7, 11, 0, 9, 1, -1 },
	{ 9, 1, 8, 8, 1, 3, 6, 7, 11, -1 },
	{ 3, 2, 7, 7, 2, 6, -1 },
	{ 0, 7, 8, 0, 6, 7, 0, 2, 6, -1 },
	{ 6, 7, 2, 2, 7, 3, 9, 1, 0, -1 },
	{ 6, 7, 8, 6, 8, 1, 8, 9, 1, 2, 6, 1, -1 },
	{ 11, 6, 7, 10, 2, 1, -1 },
	{ 3, 8, 0, 11, 6, 7, 10, 2, 1, -1 },
	{ 0, 9, 2, 2, 9, 10, 7, 11, 6, -1 },
	{ 6, 7, 11, 8, 2, 3, 8, 10, 2, 8, 9, 10, -1 },
	{ 7, 10, 6, 7, 1, 10, 7, 3, 1, -1 },
	{ 8, 0, 7, 7, 0, 6, 6, 0, 1, 6, 1, 10, -1 },
	{ 7, 3, 6, 3, 0, 9, 6, 3, 9, 6, 9, 10, -1 },
	{ 6, 7, 10, 7, 8, 10, 8, 9, 10, -1 },
	{ 11, 6, 8, 8, 6, 4, -1 },
	{ 6, 3, 11, 6, 0, 3, 6, 4, 0, -1 },
	{ 11, 6, 8, 8, 6, 4, 1, 0, 9, -1 },
	{ 1, 3, 9, 3, 11, 6, 9, 3, 6, 9, 6, 4, -1 },
	{ 2, 8, 3, 2, 4, 8, 2, 6, 4, -1 },
	{ 4, 0, 6, 6, 0, 2, -1 },
	{ 9, 1, 0, 2, 8, 3, 2, 4, 8, 2, 6, 4, -1 },
	{ 9, 1, 4, 1, 2, 4, 2, 6, 4, -1 },
	{ 4, 8, 6, 6, 8, 11, 1, 10, 2, -1 },
	{ 1, 10, 2, 6, 3, 11, 6, 0, 3, 6, 4, 0, -1 },
	{ 11, 6, 4, 11, 4, 8, 10, 2, 9, 2, 0, 9, -1 },
	{ 10, 4, 9, 6, 4, 10, 11, 2, 3, -1 },
	{ 4, 8, 3, 4, 3, 10, 3, 1, 10, 6, 4, 10, -1 },
	{ 1, 10, 0, 10, 6, 0, 6, 4, 0, -1 },
	{ 4, 10, 6, 9, 10, 4, 0, 8, 3, -1 },
	{ 4, 10, 6, 9, 10, 4, -1 },
	{ 6, 7, 11, 4, 5, 9, -1 },
	{ 4, 5, 9, 7, 11, 6, 3, 8, 0, -1 },
	{ 1, 0, 5, 5, 0, 4, 11, 6, 7, -1 },
	{ 11, 6, 7, 5, 8, 4, 5, 3, 8, 5, 1, 3, -1 },
	{ 3, 2, 7, 7, 2, 6, 9, 4, 5, -1 },
	{ 5, 9, 4, 0, 7, 8, 0, 6, 7, 0, 2, 6, -1 },
	{ 3, 2, 6, 3, 6, 7, 1, 0, 5, 0, 4, 5, -1 },
	{ 6, 1, 2, 5, 1, 6, 4, 7, 8, -1 },
	{ 10, 2, 1, 6, 7, 11, 4, 5, 9, -1 },
	{ 0, 3, 8, 4, 5, 9, 11, 6, 7, 10, 2, 1, -1 },
	{ 7, 11, 6, 2, 5, 10, 2, 4, 5, 2, 0, 4, -1 },
	{ 8, 4, 7, 5, 10, 6, 3, 11, 2, -1 },
	{ 9, 4, 5, 7, 10, 6, 7, 1, 10, 7, 3, 1, -1 },
	{ 10, 6, 5, 7, 8, 4, 1, 9, 0, -1 },
	{ 4, 3, 0, 7, 3, 4, 6, 5, 10, -1 },
	{ 10, 6, 5, 8, 4, 7, -1 },
	{ 9, 6, 5, 9, 11, 6, 9, 8, 11, -1 },
	{ 11, 6, 3, 3, 6, 0, 0, 6, 5, 0, 5, 9, -1 },
	{ 11, 6, 5, 11, 5, 0, 5, 1, 0, 8, 11, 0, -1 },
	{ 11, 6, 3, 6, 5, 3, 5, 1, 3, -1 },
	{ 9, 8, 5, 8, 3, 2, 5, 8, 2, 5, 2, 6, -1 },
	{ 5, 9, 6, 9, 0, 6, 0, 2, 6, -1 },
	{ 1, 6, 5, 2, 6, 1, 3, 0, 8, -1 },
	{ 1, 6, 5, 2, 6, 1, -1 },
	{ 2, 1, 10, 9, 6, 5, 9, 11, 6, 9, 8, 11, -1 },
	{ 9, 0, 1, 3, 11, 2, 5, 10, 6, -1 },
	{ 11, 0, 8, 2, 0, 11, 10, 6, 5, -1 },
	{ 3, 11, 2, 5, 10, 6, -1 },
	{ 1, 8, 3, 9, 8, 1, 5, 10, 6, -1 },
	{ 6, 5, 10, 0, 1, 9, -1 },
	{ 8, 3, 0, 5, 10, 6, -1 },
	{ 6, 5, 10, -1 },
	{ 10, 5, 6, -1 },
	{ 0, 3, 8, 6, 10, 5, -1 },
	{ 10, 5, 6, 9, 1, 0, -1 },
	{ 3, 8, 1, 1, 8, 9, 6, 10, 5, -1 },
	{ 2, 11, 3, 6, 10, 5, -1 },
	{ 8, 0, 11, 11, 0, 2, 5, 6, 10, -1 },
	{ 1, 0, 9, 2, 11, 3, 6, 10, 5, -1 },
	{ 5, 6, 10, 11, 1, 2, 11, 9, 1, 11, 8, 9, -1 },
	{ 5, 6, 1, 1, 6, 2, -1 },
	{ 5, 6, 1, 1, 6, 2, 8, 0, 3, -1 },
	{ 6, 9, 5, 6, 0, 9, 6, 2, 0, -1 },
	{ 6, 2, 5, 2, 3, 8, 5, 2, 8, 5, 8, 9, -1 },
	{ 3, 6, 11, 3, 5, 6, 3, 1, 5, -1 },
	{ 8, 0, 1, 8, 1, 6, 1, 5, 6, 11, 8, 6, -1 },
	{ 11, 3, 6, 6, 3, 5, 5, 3, 0, 5, 0, 9, -1 },
	{ 5, 6, 9, 6, 11, 9, 11, 8, 9, -1 },
	{ 5, 6, 10, 7, 4, 8, -1 },
	{ 0, 3, 4, 4, 3, 7, 10, 5, 6, -1 },
	{ 5, 6, 10, 4, 8, 7, 0, 9, 1, -1 },
	{ 6, 10, 5, 1, 4, 9, 1, 7, 4, 1, 3, 7, -1 },
	{ 7, 4, 8, 6, 10, 5, 2, 11, 3, -1 },
	{ 10, 5, 6, 4, 11, 7, 4, 2, 11, 4, 0, 2, -1 },
	{ 4, 8, 7, 6, 10, 5, 3, 2, 11, 1, 0, 9, -1 },
	{ 1, 2, 10, 11, 7, 6, 9, 5, 4, -1 },
	{ 2, 1, 6, 6, 1, 5, 8, 7, 4, -1 },
	{ 0, 3, 7, 0, 7, 4, 2, 1, 6, 1, 5, 6, -1 },
	{ 8, 7, 4, 6, 9, 5, 6, 0, 9, 6, 2, 0, -1 },
	{ 7, 2, 3, 6, 2, 7, 5, 4, 9, -1 },
	{ 4, 8, 7, 3, 6, 11, 3, 5, 6, 3, 1, 5, -1 },
	{ 5, 0, 1, 4, 0, 5, 7, 6, 11, -1 },
	{ 9, 5, 4, 6, 11, 7, 0, 8, 3, -1 },
	{ 11, 7, 6, 9, 5, 4, -1 },
	{ 6, 10, 4, 4, 10, 9, -1 },
	{ 6, 10, 4, 4, 10, 9, 3, 8, 0, -1 },
	{ 0, 10, 1, 0, 6, 10, 0, 4, 6, -1 },
	{ 6, 10, 1, 6, 1, 8, 1, 3, 8, 4, 6, 8, -1 },
	{ 9, 4, 10, 10, 4, 6, 3, 2, 11, -1 },
	{ 2, 11, 8, 2, 8, 0, 6, 10, 4, 10, 9, 4, -1 },
	{ 11, 3, 2, 0, 10, 1, 0, 6, 10, 0, 4, 6, -1 },
	{ 6, 8, 4, 11, 8, 6, 2, 10, 1, -1 },
	{ 4, 1, 9, 4, 2, 1, 4, 6, 2, -1 },
	{ 3, 8, 0, 4, 1, 9, 4, 2, 1, 4, 6, 2, -1 },
	{ 6, 2, 4, 4, 2, 0, -1 },
	{ 3, 8, 2, 8, 4, 2, 4, 6, 2, -1 },
	{ 4, 6, 9, 6, 11, 3, 9, 6, 3, 9, 3, 1, -1 },
	{ 8, 6, 11, 4, 6, 8, 9, 0, 1, -1 },
	{ 11, 3, 6, 3, 0, 6, 0, 4, 6, -1 },
	{ 8, 6, 11, 4, 6, 8, -1 },
	{ 10, 7, 6, 10, 8, 7, 10, 9, 8, -1 },
	{ 3, 7, 0, 7, 6, 10, 0, 7, 10, 0, 10, 9, -1 },
	{ 6, 10, 7, 7, 10, 8, 8, 10, 1, 8, 1, 0, -1 },
	{ 6, 10, 7, 10, 1, 7, 1, 3, 7, -1 },
	{ 3, 2, 11, 10, 7, 6, 10, 8, 7, 10, 9, 8, -1 },
	{ 2, 9, 0, 10, 9, 2, 6, 11, 7, -1 },
	{ 0, 8, 3, 7, 6, 11, 1, 2, 10, -1 },
	{ 7, 6, 11, 1, 2, 10, -1 },
	{ 2, 1, 9, 2, 9, 7, 9, 8, 7, 6, 2, 7, -1 },
	{ 2, 7, 6, 3, 7, 2, 0, 1, 9, -1 },
	{ 8, 7, 0, 7, 6, 0, 6, 2, 0, -1 },
	{ 7, 2, 3, 6, 2, 7, -1 },
	{ 8, 1, 9, 3, 1, 8, 11, 7, 6, -1 },
	{ 11, 7, 6, 1, 9, 0, -1 },
	{ 6, 11, 7, 0, 8, 3, -1 },
	{ 11, 7, 6, -1 },
	{ 7, 11, 5, 5, 11, 10, -1 },
	{ 10, 5, 11, 11, 5, 7, 0, 3, 8, -1 },
	{ 7, 11, 5, 5, 11, 10, 0, 9, 1, -1 },
	{ 7, 11, 10, 7, 10, 5, 3, 8, 1, 8, 9, 1, -1 },
	{ 5, 2, 10, 5, 3, 2, 5, 7, 3, -1 },
	{ 5, 7, 10, 7, 8, 0, 10, 7, 0, 10, 0, 2, -1 },
	{ 0, 9, 1, 5, 2, 10, 5, 3, 2, 5, 7, 3, -1 },
	{ 9, 7, 8, 5, 7, 9, 10, 1, 2, -1 },
	{ 1, 11, 2, 1, 7, 11, 1, 5, 7, -1 },
	{ 8, 0, 3, 1, 11, 2, 1, 7, 11, 1, 5, 7, -1 },
	{ 7, 11, 2, 7, 2, 9, 2, 0, 9, 5, 7, 9, -1 },
	{ 7, 9, 5, 8, 9, 7, 3, 11, 2, -1 },
	{ 3, 1, 7, 7, 1, 5, -1 },
	{ 8, 0, 7, 0, 1, 7, 1, 5, 7, -1 },
	{ 0, 9, 3, 9, 5, 3, 5, 7, 3, -1 },
	{ 9, 7, 8, 5, 7, 9, -1 },
	{ 8, 5, 4, 8, 10, 5, 8, 11, 10, -1 },
	{ 0, 3, 11, 0, 11, 5, 11, 10, 5, 4, 0, 5, -1 },
	{ 1, 0, 9, 8, 5, 4, 8, 10, 5, 8, 11, 10, -1 },
	{ 10, 3, 11, 1, 3, 10, 9, 5, 4, -1 },
	{ 3, 2, 8, 8, 2, 4, 4, 2, 10, 4, 10, 5, -1 },
	{ 10, 5, 2, 5, 4, 2, 4, 0, 2, -1 },
	{ 5, 4, 9, 8, 3, 0, 10, 1, 2, -1 },
	{ 2, 10, 1, 4, 9, 5, -1 },
	{ 8, 11, 4, 11, 2, 1, 4, 11, 1, 4, 1, 5, -1 },
	{ 0, 5, 4, 1, 5, 0, 2, 3, 11, -1 },
	{ 0, 11, 2, 8, 11, 0, 4, 9, 5, -1 },
	{ 5, 4, 9, 2, 3, 11, -1 },
	{ 4, 8, 5, 8, 3, 5, 3, 1, 5, -1 },
	{ 0, 5, 4, 1, 5, 0, -1 },
	{ 5, 4, 9, 3, 0, 8, -1 },
	{ 5, 4, 9, -1 },
	{ 11, 4, 7, 11, 9, 4, 11, 10, 9, -1 },
	{ 0, 3, 8, 11, 4, 7, 11, 9, 4, 11, 10, 9, -1 },
	{ 11, 10, 7, 10, 1, 0, 7, 10, 0, 7, 0, 4, -1 },
	{ 3, 10, 1, 11, 10, 3, 7, 8, 4, -1 },
	{ 3, 2, 10, 3, 10, 4, 10, 9, 4, 7, 3, 4, -1 },
	{ 9, 2, 10, 0, 2, 9, 8, 4, 7, -1 },
	{ 3, 4, 7, 0, 4, 3, 1, 2, 10, -1 },
	{ 7, 8, 4, 10, 1, 2, -1 },
	{ 7, 11, 4, 4, 11, 9, 9, 11, 2, 9, 2, 1, -1 },
	{ 1, 9, 0, 4, 7, 8, 2, 3, 11, -1 },
	{ 7, 11, 4, 11, 2, 4, 2, 0, 4, -1 },
	{ 4, 7, 8, 2, 3, 11, -1 },
	{ 9, 4, 1, 4, 7, 1, 7, 3, 1, -1 },
	{ 7, 8, 4, 1, 9, 0, -1 },
	{ 3, 4, 7, 0, 4, 3, -1 },
	{ 7, 8, 4, -1 },
	{ 11, 10, 8, 8, 10, 9, -1 },
	{ 0, 3, 9, 3, 11, 9, 11, 10, 9, -1 },
	{ 1, 0, 10, 0, 8, 10, 8, 11, 10, -1 },
	{ 10, 3, 11, 1, 3, 10, -1 },
	{ 3, 2, 8, 2, 10, 8, 10, 9, 8, -1 },
	{ 9, 2, 10, 0, 2, 9, -1 },
	{ 8, 3, 0, 10, 1, 2, -1 },
	{ 2, 10, 1, -1 },
	{ 2, 1, 11, 1, 9, 11, 9, 8, 11, -1 },
	{ 11, 2, 3, 9, 0, 1, -1 },
	{ 11, 0, 8, 2, 0, 11, -1 },
	{ 3, 11, 2, -1 },
	{ 1, 8, 3, 9, 8, 1, -1 },
	{ 1, 9, 0, -1 },
	{ 8, 3, 0, -1 },
	{ -1 },
};


glm::vec3 interpolate(glm::vec3 p1, glm::vec3 p2, float valP1, float valP2, float isoValue) {
    float t = (isoValue - valP1) / (valP2 - valP1);
    return p1 + t * (p2 - p1);
}

void renderIsoSurface() {
	glUniform1i(useVertexColorLoc, 1);
    glBindVertexArray(isoVAO);
    glDrawArrays(GL_TRIANGLES, 0, isoVertices.size());
    glBindVertexArray(0);
}

void marchingCubes(float isoValue) {
    isoVertices.clear();
    isoColors.clear();

    glm::vec3 vertexList[12];

    for (int z = 0; z < vtk_file.dimensions.z - 1; ++z) {
        for (int y = 0; y < vtk_file.dimensions.y - 1; ++y) {
            for (int x = 0; x < vtk_file.dimensions.x - 1; ++x) {

                // 1. Compute the cube index
                int cubeIndex = 0;
                float cubeValues[8];
                glm::vec3 cubePos[8];

                for (int i = 0; i < 8; ++i) {
                    int dx = (i & 1) ? 1 : 0;
                    int dy = (i & 2) ? 1 : 0;
                    int dz = (i & 4) ? 1 : 0;

                    cubePos[i] = glm::vec3(
                        (x + dx) * vtk_file.spacing.x + vtk_file.origin.x,
                        (y + dy) * vtk_file.spacing.y + vtk_file.origin.y,
                        (z + dz) * vtk_file.spacing.z + vtk_file.origin.z
                    );
                    cubeValues[i] = GetScalarValue(x + dx, y + dy, z + dz);

                    if (cubeValues[i] < isoValue) cubeIndex |= (1 << i);
                }

                int ET = ETs[cubeIndex];
                if (ET == 0) continue;

                for (int i = 0; i < 12; ++i) {
                    if (ET & (1 << i)) {
                        int v1 = ETIndices[i][0];
                        int v2 = ETIndices[i][1];
                        vertexList[i] = interpolate(cubePos[v1], cubePos[v2], cubeValues[v1], cubeValues[v2], isoValue);
                    }
                }

                for (int i = 0; TT[cubeIndex][i] != -1; i += 3) {
                    isoVertices.push_back(vertexList[TT[cubeIndex][i]]);
                    isoVertices.push_back(vertexList[TT[cubeIndex][i + 1]]);
                    isoVertices.push_back(vertexList[TT[cubeIndex][i + 2]]);

                    glm::vec3 color = glm::vec3(0.5f, 0.0f, 0.1f);
                    isoColors.push_back(color);
                    isoColors.push_back(color);
                    isoColors.push_back(color);
                }
            }
        }
    }

	for(long unsigned int i = 0; i < isoColors.size(); i ++) {
		isoColors[i] = glm::mix(glm::vec3(1.0f, 0.0f, 0.0f), glm::vec3(0.0f, 1.0f, 0.0f), i/(float)isoColors.size());
	}
	std::cout << isoVertices.size() << std::endl;
}

void loadISOBuffer() {

    if (isoVAO != 0) {
        glDeleteVertexArrays(1, &isoVAO);
        isoVAO = 0;
    }
    if (isoVBO != 0) {
        glDeleteBuffers(1, &isoVBO);
        isoVBO = 0;
    }
    if (isoColorVBO != 0) {
        glDeleteBuffers(1, &isoColorVBO);
        isoColorVBO = 0;
    }

    glGenVertexArrays(1, &isoVAO);
    glBindVertexArray(isoVAO);

    glGenBuffers(1, &isoVBO);
    glBindBuffer(GL_ARRAY_BUFFER, isoVBO);
    glBufferData(GL_ARRAY_BUFFER, isoVertices.size() * sizeof(glm::vec3), isoVertices.data(), GL_STATIC_DRAW);
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, (void*)0);
    glEnableVertexAttribArray(0);

    glGenBuffers(1, &isoColorVBO);
    glBindBuffer(GL_ARRAY_BUFFER, isoColorVBO);
    glBufferData(GL_ARRAY_BUFFER, isoColors.size() * sizeof(glm::vec3), isoColors.data(), GL_STATIC_DRAW);
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, (void*)0);
    glEnableVertexAttribArray(1);

    glBindVertexArray(0);
}


void onInit(int argc, char * argv[], GLFWwindow* window){

	GLuint errorCode = glGetError();
	if (errorCode != GL_NO_ERROR) {
		fprintf(stderr, "onInit Start: OpenGL rendering error %d\n", errorCode);
	}

	glClearColor(0.0f, 0.0f, 0.0f, 0.0f);

	for (int k = 0; k < vtk_file.dimensions.z; ++k) {
		for (int j = 0; j < vtk_file.dimensions.y; ++j) {
			for (int i = 0; i < vtk_file.dimensions.x; ++i) {
				glm::vec3 point = vtk_file.origin + glm::vec3(i * vtk_file.spacing.x, j * vtk_file.spacing.y, k * vtk_file.spacing.z);
				gridPoints.push_back(point);
				minValue = std::min(minValue, GetScalarValue(i, j, k));
				maxValue = std::max(maxValue, GetScalarValue(i, j, k));
			}
		}
	}
	minPoint = vtk_file.origin;
	maxPoint = vtk_file.origin + glm::vec3((vtk_file.dimensions.x - 1) * vtk_file.spacing.x,
                                        (vtk_file.dimensions.y - 1) * vtk_file.spacing.y,
                                        (vtk_file.dimensions.z - 1) * vtk_file.spacing.z);

	center = (minPoint + maxPoint) * 0.5f;
	
	glm::vec3 size = maxPoint - minPoint; 
	float boundingRadius = glm::length(size) * 0.5f; 

	float distanceFactor = 1.5f; 

	viewDirection = glm::vec3(0.0f, 0.0f, -1.0f);

	cameraPos = center - viewDirection * boundingRadius * distanceFactor;

	cameraFront = glm::normalize(center - cameraPos);

	cameraUp = glm::vec3(0.0f, 1.0f, 0.0f);

	boundingBoxVertices = {
		{minPoint.x, minPoint.y, minPoint.z},
		{maxPoint.x, minPoint.y, minPoint.z},
		{maxPoint.x, maxPoint.y, minPoint.z},
		{minPoint.x, maxPoint.y, minPoint.z},
		{minPoint.x, minPoint.y, maxPoint.z},
		{maxPoint.x, minPoint.y, maxPoint.z},
		{maxPoint.x, maxPoint.y, maxPoint.z},
		{minPoint.x, maxPoint.y, maxPoint.z}
	};

	marchingCubes(offset);
	loadISOBuffer();

	CreateVertexBuffer();

	CompileShaders();

	glEnable(GL_DEPTH_TEST); 
	errorCode = glGetError();
	if (errorCode != GL_NO_ERROR) {
		fprintf(stderr, "onInit: OpenGL rendering error %d\n", errorCode);
	}
}



static void onDisplay(GLFWwindow* window) {

	if(prevOffset != offset) {
		prevOffset = offset;
		marchingCubes(offset);
		loadISOBuffer();
	}
	static float rotateX = 0.0f;
	static float rotateY = 0.0f;
	static float rotateZ = 0.0f;

	glm::mat4 model = glm::translate(glm::mat4(1.0f), -center);

	model = glm::rotate(model, glm::radians(rotateX), glm::vec3(1, 0, 0));
	model = glm::rotate(model, glm::radians(rotateY), glm::vec3(0, 1, 0));
	model = glm::rotate(model, glm::radians(rotateZ), glm::vec3(0, 0, 1));

	model = glm::translate(model, center);

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glm::mat4 view = glm::lookAt(cameraPos, center, cameraUp);
	glm::mat4 projection = glm::perspective(
		glm::radians(60.0f),
		(float)theWindowWidth / (float)theWindowHeight,
		0.1f,
		1000.0f
	);
	renderIsoSurface();

	glBindVertexArray(boundingBoxVAO);

	glUniformMatrix4fv(modelLoc, 1, GL_FALSE, glm::value_ptr(model));
	glUniformMatrix4fv(viewLoc, 1, GL_FALSE, glm::value_ptr(view));
	glUniformMatrix4fv(projLoc, 1, GL_FALSE, glm::value_ptr(projection));
	glUniform1i(useVertexColorLoc, 0);
	glm::vec3 boundingBoxColor = glm::vec3(1.0f, 1.0f, 1.0f); 
	glUniform3fv(solidColorLoc, 1, glm::value_ptr(boundingBoxColor));
	
	glLineWidth(4.0f); 

	glDrawElements(
		GL_LINES,                             
		boundingBoxIndices.size(),           
		GL_UNSIGNED_INT,                       
		0                                      
	);

	glBindVertexArray(0);

}

static void onIdle() {
    if (isAnimating) {
        rotation += 0.001; 
		offset += 0.01;
		if(offset > maxValue) {
			offset = minValue;
		}
    }
}


void framebuffer_size_callback(GLFWwindow* window, int width, int height) {
    glViewport(0, 0, width, height);
}

void onFramebufferSize(GLFWwindow* window, int width, int height) {
    glViewport(0, 0, width, height);
    theWindowWidth = width;
    theWindowHeight = height;
}

int main(int argc, char** argv) {
    if (!glfwInit()) {
        fprintf(stderr, "Failed to initialize GLFW\n");
        return -1;
    }
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 6);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    GLFWwindow* window = glfwCreateWindow(theWindowWidth, theWindowHeight, theProgramTitle.c_str(), NULL, NULL);
    if (!window) {
        fprintf(stderr, "Failed to create GLFW window\n");
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window);
	glfwSwapInterval( 0 );
    glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);

		if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <filename>" << std::endl;
        return 1;
    }

    std::string filename = argv[1];

    if (!vtk_file.readFile(filename)) {
        std::cerr << "Failed to read the file: " << filename << std::endl;
        return 1;
	}

    glewExperimental = GL_TRUE;
    GLenum res = glewInit();
    if (res != GLEW_OK) {
        fprintf(stderr, "Error initializing GLEW: '%s'\n", glewGetErrorString(res));
        glfwTerminate();
        return -1;
    }

    printf("GL version: %s\n", glGetString(GL_VERSION));

    glViewport(0, 0, theWindowWidth, theWindowHeight);
    onInit(argc, argv, window);

    while (!glfwWindowShouldClose(window)) {
        glfwPollEvents();
        onIdle();

		computeFPS(window);

        onDisplay(window);

        glfwSwapBuffers(window);
    }

    glfwTerminate();
    return 0;
}
