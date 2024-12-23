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
};

VTKFileReader vtk_file;

GLuint ShaderProgram;

GLuint colormapTex;

GLuint minValLoc, maxValLoc;

void Initialize1DTexture() {
    glGenTextures(1, &colormapTex);
    glBindTexture(GL_TEXTURE_1D, colormapTex);

    std::vector<glm::vec3> colormap = {
        glm::vec3(0.0, 0.0, 1.0), // Blue
        glm::vec3(0.0, 1.0, 0.0)  // Red
    };

    glTexImage1D(GL_TEXTURE_1D, 0, GL_RGB, colormap.size(), 0, GL_RGB, GL_FLOAT, colormap.data());

    glTexParameteri(GL_TEXTURE_1D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_BORDER);
    glTexParameteri(GL_TEXTURE_1D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_1D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

    glBindTexture(GL_TEXTURE_1D, 0);
	GLuint errorCode = glGetError();
	if (errorCode != GL_NO_ERROR) {
		fprintf(stderr, "Initialize1DTexture: OpenGL rendering error %d\n", errorCode);
	}
}

std::vector<glm::vec3> gridPoints;
std::vector<glm::vec3> boundingBoxVertices;
std::vector<vt> planeVertices;
std::vector<unsigned int> planeIndices;
std::vector<unsigned int> boundingBoxIndices = {
	0, 1, 1, 2, 2, 3, 3, 0,
	4, 5, 5, 6, 6, 7, 7, 4,
	0, 4, 1, 5, 2, 6, 3, 7
};

GLuint boundingBoxVAO, boundingBoxVBO, boundingBoxEBO;
GLuint planeVAO, planeVBO, planeEBO;

glm::vec3 cameraFront, cameraUp, viewDirection, cameraPos, center;
glm::vec3 minPoint, maxPoint;
float offset = 0.9f;

int selectedAxis = 2;
std::string selectedField = "SALT";
float prevOffset = -1;
int prevAxis = -1;

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


float minValue = INT_MAX, maxValue = INT_MIN;

float GetScalarValue(int i, int j, int k) {
    if (i < 0 || i >= vtk_file.dimensions.x || 
        j < 0 || j >= vtk_file.dimensions.y || 
        k < 0 || k >= vtk_file.dimensions.z) {
        throw std::out_of_range("Indices are out of range");
    }

    int index = i + vtk_file.dimensions.x * (j + vtk_file.dimensions.y * k);
    return vtk_file.fieldData[selectedField][index];
}

GLuint scalarFieldTex;
void Initialize3DTexture() {
	glGenTextures(1, &scalarFieldTex);
	glBindTexture(GL_TEXTURE_3D, scalarFieldTex);

	glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
	glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
	glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_WRAP_R, GL_CLAMP_TO_EDGE);
	glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
	glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

	std::cout << "Field: " << selectedField << std::endl;
	std::cout << "Dimensions: " << vtk_file.dimensions.x << " " << vtk_file.dimensions.y << " " << vtk_file.dimensions.z << std::endl;
	std::cout << "Size: " << vtk_file.fieldData[selectedField].size() << std::endl;

	std::vector<float> reorderedData(vtk_file.dimensions.x * vtk_file.dimensions.y * vtk_file.dimensions.z);

	// Loop through data in the correct X, Y, Z order
	for (int z = 0; z < vtk_file.dimensions.z; ++z) {
		for (int y = 0; y < vtk_file.dimensions.y; ++y) {
			for (int x = 0; x < vtk_file.dimensions.x; ++x) {
				int sourceIndex = z * (vtk_file.dimensions.x * vtk_file.dimensions.y) + 
								y * vtk_file.dimensions.x + x;

				int targetIndex = x + 
								y * vtk_file.dimensions.x + 
								z * (vtk_file.dimensions.x * vtk_file.dimensions.y);

				reorderedData[targetIndex] = vtk_file.fieldData[selectedField][sourceIndex];
			}
		}
	}
	glTexImage3D(
		GL_TEXTURE_3D,
		0,                      
		GL_R32F,               
		vtk_file.dimensions.x,
		vtk_file.dimensions.y,
		vtk_file.dimensions.z,
		0,                      
		GL_RED,                 
		GL_FLOAT,              
		reorderedData.data()   
	);

	glBindTexture(GL_TEXTURE_3D, 0);
	GLuint errorCode = glGetError();
	if (errorCode != GL_NO_ERROR) {
		fprintf(stderr, "Initialize3DTexture: OpenGL rendering error %d\n", errorCode);
	}
}

void computeFPS(GLFWwindow* window) {
    static int frameCount = 0;
    static double lastTime = 0.0;
    static std::string title;

    frameCount++;
    double currentTime = glfwGetTime();

    if (currentTime - lastTime >= 1.0) { 
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

	std::cout << "boundingBoxVertices.size() = " << boundingBoxVertices.size() << std::endl;

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
	ShaderProgram = glCreateProgram();

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

	modelLoc = glGetUniformLocation(ShaderProgram, "model");
	viewLoc = glGetUniformLocation(ShaderProgram, "view");
	projLoc = glGetUniformLocation(ShaderProgram, "projection");
	useVertexColorLoc = glGetUniformLocation(ShaderProgram, "useVertexColor");
	solidColorLoc= glGetUniformLocation(ShaderProgram, "solidColor");
	minValLoc= glGetUniformLocation(ShaderProgram, "minVal");
	maxValLoc= glGetUniformLocation(ShaderProgram, "maxVal");

	GLuint errorCode = glGetError();
	if (errorCode != GL_NO_ERROR) {
		fprintf(stderr, "CompileShaders: OpenGL rendering error %d\n", errorCode);
	}
}



void onInit(int argc, char * argv[], GLFWwindow* window)
{
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

	CreateVertexBuffer();

	CompileShaders();

	Initialize1DTexture();
	Initialize3DTexture();
	glEnable(GL_DEPTH_TEST); 
	errorCode = glGetError();
	if (errorCode != GL_NO_ERROR) {
		fprintf(stderr, "onInit: OpenGL rendering error %d\n", errorCode);
	}
}

void sX(float offset) {
    float X0 = minPoint.x + (maxPoint.x - minPoint.x) * offset;

    int samplesY = vtk_file.dimensions.y;
    int samplesZ = vtk_file.dimensions.z;

    float deltaY = (maxPoint.y - minPoint.y) / (samplesY - 1);
    float deltaZ = (maxPoint.z - minPoint.z) / (samplesZ - 1);

    for (int j = 0; j < samplesY; j++) {
        float y = minPoint.y + j * deltaY;
        for (int i = 0; i < samplesZ; i++) {
            float z = minPoint.z + i * deltaZ;
            glm::vec3 point = glm::vec3(X0, y, z);
            vt vertex;
            vertex.position = point;
            planeVertices.push_back(vertex);
        }
    }

    for (int j = 0; j < samplesY - 1; ++j) {
        for (int i = 0; i < samplesZ - 1; ++i) {
            unsigned int topLeft = j * samplesZ + i;
            unsigned int topRight = topLeft + 1;
            unsigned int bottomLeft = (j + 1) * samplesZ + i;
            unsigned int bottomRight = bottomLeft + 1;

            planeIndices.push_back(topLeft);
            planeIndices.push_back(bottomLeft);
            planeIndices.push_back(topRight);

            planeIndices.push_back(topRight);
            planeIndices.push_back(bottomLeft);
            planeIndices.push_back(bottomRight);
        }
    }
		GLuint errorCode = glGetError();
	if (errorCode != GL_NO_ERROR) {
		fprintf(stderr, "sX: OpenGL rendering error %d\n", errorCode);
	}
}

void sY(float offset) {
    float Y0 = minPoint.y + (maxPoint.y - minPoint.y) * offset;

    int samplesX = vtk_file.dimensions.x;
    int samplesZ = vtk_file.dimensions.z;

    float deltaX = (maxPoint.x - minPoint.x) / (samplesX - 1);
    float deltaZ = (maxPoint.z - minPoint.z) / (samplesZ - 1);

    for (int j = 0; j < samplesX; j++) {
        float x = minPoint.x + j * deltaX;
        for (int i = 0; i < samplesZ; i++) {
            float z = minPoint.z + i * deltaZ;
            glm::vec3 point = glm::vec3(x, Y0, z);
            vt vertex;
            vertex.position = point;
            planeVertices.push_back(vertex);
        }
    }

    for (int j = 0; j < samplesX - 1; ++j) {
        for (int i = 0; i < samplesZ - 1; ++i) {
            unsigned int topLeft = j * samplesZ + i;
            unsigned int topRight = topLeft + 1;
            unsigned int bottomLeft = (j + 1) * samplesZ + i;
            unsigned int bottomRight = bottomLeft + 1;

            planeIndices.push_back(topLeft);
            planeIndices.push_back(bottomLeft);
            planeIndices.push_back(topRight);

            planeIndices.push_back(topRight);
            planeIndices.push_back(bottomLeft);
            planeIndices.push_back(bottomRight);
        }
    }
		GLuint errorCode = glGetError();
	if (errorCode != GL_NO_ERROR) {
		fprintf(stderr, "sY: OpenGL rendering error %d\n", errorCode);
	}
}

void sZ(float offset) {
    float Z0 = minPoint.z + (maxPoint.z - minPoint.z) * offset;

    int samplesX = vtk_file.dimensions.x;
    int samplesY = vtk_file.dimensions.y;

    float deltaX = (maxPoint.x - minPoint.x) / (samplesX - 1);
    float deltaY = (maxPoint.y - minPoint.y) / (samplesY - 1);

    for (int j = 0; j < samplesY; j++) {
        float y = minPoint.y + j * deltaY;
        for (int i = 0; i < samplesX; i++) {
            float x = minPoint.x + i * deltaX;
            glm::vec3 point = glm::vec3(x, y, Z0);
            vt vertex;
            vertex.position = point;
            planeVertices.push_back(vertex);
        }
    }

    for (int j = 0; j < samplesY - 1; ++j) {
        for (int i = 0; i < samplesX - 1; ++i) {
            unsigned int topLeft = j * samplesX + i;
            unsigned int topRight = topLeft + 1;
            unsigned int bottomLeft = (j + 1) * samplesX + i;
            unsigned int bottomRight = bottomLeft + 1;

            planeIndices.push_back(topLeft);
            planeIndices.push_back(bottomLeft);
            planeIndices.push_back(topRight);

            planeIndices.push_back(topRight);
            planeIndices.push_back(bottomLeft);
            planeIndices.push_back(bottomRight);
        }
    }
	GLuint errorCode = glGetError();
	if (errorCode != GL_NO_ERROR) {
		fprintf(stderr, "sZ: OpenGL rendering error %d\n", errorCode);
	}
}


void RenderSlicingPlane(int axis, float offset) {
	if(axis != prevAxis || offset != prevOffset) {
		prevAxis = axis;
		prevOffset = offset;
		planeVertices.clear();
		planeIndices.clear();

		if (axis == 0) {  
			sX(offset);
		} else if (axis == 1) {  
			sY(offset);
		} else if (axis == 2) {  
			sZ(offset);
		} else {
			std::cout << "invalid axis" << std::endl;
		}
		if (planeVAO != 0) {
			glDeleteVertexArrays(1, &planeVAO);
		}
		if (planeVBO != 0) {
			glDeleteBuffers(1, &planeVBO);
		}
		if (planeEBO != 0) {
			glDeleteBuffers(1, &planeEBO);
		}
		glGenVertexArrays(1, &planeVAO);
		glBindVertexArray(planeVAO);

		glGenBuffers(1, &planeVBO);
		glBindBuffer(GL_ARRAY_BUFFER, planeVBO);
		glBufferData(GL_ARRAY_BUFFER, planeVertices.size() * sizeof(vt), planeVertices.data(), GL_STATIC_DRAW);

		glGenBuffers(1, &planeEBO);
		glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, planeEBO);
		glBufferData(GL_ELEMENT_ARRAY_BUFFER, planeIndices.size() * sizeof(unsigned int), planeIndices.data(), GL_STATIC_DRAW);

		glEnableVertexAttribArray(0);
		glVertexAttribPointer(
			0,                              
			3,                              
			GL_FLOAT,                      
			GL_FALSE,                       
			sizeof(vt),                
			(void*)offsetof(vt, position) 
		);

		glBindVertexArray(0);
	}

    glBindVertexArray(planeVAO);
	glUniform1i(useVertexColorLoc, 1);
	glUniform1f(minValLoc, minValue);
	glUniform1f(maxValLoc, maxValue);

    glDrawElements(GL_TRIANGLES, planeIndices.size(), GL_UNSIGNED_INT, 0);
    glBindVertexArray(0);
	GLuint errorCode = glGetError();
	if (errorCode != GL_NO_ERROR) {
		fprintf(stderr, "RenderSlicingPlane: OpenGL rendering error %d\n", errorCode);
	}
}

static void onDisplay(GLFWwindow* window) {
   
	static float rotateX = 0.0f;
	static float rotateY = 0.0f;
	static float rotateZ = 0.0f;

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	glm::mat4 model = glm::translate(glm::mat4(1.0f), -center);

	model = glm::rotate(model, glm::radians(rotateX), glm::vec3(1, 0, 0));
	model = glm::rotate(model, glm::radians(rotateY), glm::vec3(0, 1, 0));
	model = glm::rotate(model, glm::radians(rotateZ), glm::vec3(0, 0, 1));

	model = glm::translate(model, center);

	glm::mat4 view = glm::lookAt(cameraPos, center, cameraUp);

	int width, height;
	glfwGetWindowSize(window, &width, &height);

	glm::mat4 projection = glm::perspective(
		glm::radians(60.0f),
		(float) width / (float)height,
		0.1f,
		1000.0f
	);
	
	glUseProgram(ShaderProgram);
	glUniformMatrix4fv(glGetUniformLocation(ShaderProgram, "model"), 1, GL_FALSE, glm::value_ptr(model));
	glUniformMatrix4fv(glGetUniformLocation(ShaderProgram, "view"), 1, GL_FALSE, glm::value_ptr(view));
	glUniformMatrix4fv(glGetUniformLocation(ShaderProgram, "projection"), 1, GL_FALSE, glm::value_ptr(projection));

	glUniform3fv(glGetUniformLocation(ShaderProgram, "minPoint"), 1, glm::value_ptr(minPoint));
	glUniform3fv(glGetUniformLocation(ShaderProgram, "maxPoint"), 1, glm::value_ptr(maxPoint));

	float scalarMin = minValue;
	float scalarMax = maxValue;
	glUniform1f(glGetUniformLocation(ShaderProgram, "scalarMin"), scalarMin);
	glUniform1f(glGetUniformLocation(ShaderProgram, "scalarMax"), scalarMax);

	glActiveTexture(GL_TEXTURE0);
	glBindTexture(GL_TEXTURE_3D, scalarFieldTex);
	glUniform1i(glGetUniformLocation(ShaderProgram, "scalarFieldTexture"), 0);

	glActiveTexture(GL_TEXTURE1);
	glBindTexture(GL_TEXTURE_1D, colormapTex);
	glUniform1i(glGetUniformLocation(ShaderProgram, "colormapTexture"), 1);

	RenderSlicingPlane(selectedAxis, offset);
	

	glBindVertexArray(boundingBoxVAO);
	glUniform1i(useVertexColorLoc, 0);
	glm::vec3 boundingBoxColor = glm::vec3(1.0f, 1.0f, 1.0f); // White color
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
        rotation += 0.001; // Update rotation
		// offset += 0.0001;
		if(offset > 1.f) {
			offset = 0.f;
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
    // Initialize GLFW
    if (!glfwInit()) {
        fprintf(stderr, "Failed to initialize GLFW\n");
        return -1;
    }

    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 6);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    // Create GLFW window
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
