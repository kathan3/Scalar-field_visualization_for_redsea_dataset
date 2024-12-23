#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <fstream>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include "file_utils.h"
#include "math_utils.h"
#include "vtk_filereader.h"
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>
#include <glm/gtx/string_cast.hpp>

struct vt {
  glm::vec3 position; 
};

VTKFileReader vtk_file;
std::vector<glm::ivec3> voxelPositions;

GLuint voxelVBO, voxelVAO;

GLuint ShaderProgram;

GLuint colormapTex;

GLuint minValLoc, maxValLoc;

std::vector<glm::vec3> gridPoints;
std::vector<glm::vec3> boundingBoxVertices;
std::vector<vt> planeVertices;
std::vector<unsigned int> planeIndices;
std::vector<unsigned int> boundingBoxIndices = {
    0, 1, 1, 2, 2, 3, 3, 0,
    4, 5, 5, 6, 6, 7, 7, 4,
    0, 4, 1, 5, 2, 6, 3, 7};
GLuint boundingBoxVAO, boundingBoxVBO, boundingBoxEBO;
GLuint planeVAO, planeVBO, planeEBO;

glm::vec3 cameraFront, cameraUp, viewDirection, cameraPos, center;
glm::vec3 minPoint, maxPoint;
float offset = 35;

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
GLint modelLoc, viewLoc, projLoc, useVertexColorLoc, solidColorLoc;
GLint loc_volumeData, loc_isoValue, loc_volumeOrigin, loc_volumeSpacing,
    loc_volumeDimensions;

const int ANIMATION_DELAY = 20; 
const char *pVSFileName = "shader.vs";
const char *pFSFileName = "shader.fs";
const char *pGSFileName = "shader.gs";

float minValue = INT_MAX, maxValue = INT_MIN;

float GetScalarValue(int i, int j, int k) {
  if (i < 0 || i >= vtk_file.dimensions.x || j < 0 ||
      j >= vtk_file.dimensions.y || k < 0 || k >= vtk_file.dimensions.z) {
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
  std::cout << "Dimensions: " << vtk_file.dimensions.x << " "
            << vtk_file.dimensions.y << " " << vtk_file.dimensions.z
            << std::endl;
  std::cout << "Size: " << vtk_file.fieldData[selectedField].size()
            << std::endl;

  std::vector<float> reorderedData(
      vtk_file.dimensions.x * vtk_file.dimensions.y * vtk_file.dimensions.z);

  for (int z = 0; z < vtk_file.dimensions.z; ++z) {
    for (int y = 0; y < vtk_file.dimensions.y; ++y) {
      for (int x = 0; x < vtk_file.dimensions.x; ++x) {
        int sourceIndex = z * (vtk_file.dimensions.x * vtk_file.dimensions.y) +
                          y * vtk_file.dimensions.x + x;
        int targetIndex = x + y * vtk_file.dimensions.x +
                          z * (vtk_file.dimensions.x * vtk_file.dimensions.y);

        reorderedData[targetIndex] =
            vtk_file.fieldData[selectedField][sourceIndex];
      }
    }
  }

  glTexImage3D(GL_TEXTURE_3D,
               0,       
               GL_R32F, 
               vtk_file.dimensions.x, vtk_file.dimensions.y,
               vtk_file.dimensions.z,
               0,                   
               GL_RED,              
               GL_FLOAT,          
               reorderedData.data() 
  );

  // Unbind the texture
  glBindTexture(GL_TEXTURE_3D, 0);
  GLuint errorCode = glGetError();
  if (errorCode != GL_NO_ERROR) {
    fprintf(stderr, "Initialize3DTexture: OpenGL rendering error %d\n",
            errorCode);
  }
}

void computeFPS(GLFWwindow *window) {
  static int frameCount = 0;
  static double lastTime = 0.0;
  static std::string title;

  frameCount++;
  double currentTime =
      glfwGetTime(); 

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
  glBufferData(GL_ARRAY_BUFFER, boundingBoxVertices.size() * sizeof(glm::vec3),
               boundingBoxVertices.data(), GL_STATIC_DRAW);

  glGenBuffers(1, &boundingBoxEBO);
  glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, boundingBoxEBO);
  glBufferData(GL_ELEMENT_ARRAY_BUFFER,
               boundingBoxIndices.size() * sizeof(unsigned int),
               boundingBoxIndices.data(), GL_STATIC_DRAW);

  std::cout << "boundingBoxVertices.size() = " << boundingBoxVertices.size()
            << std::endl;

  glEnableVertexAttribArray(0);
  glVertexAttribPointer(0,               
                        3,                 
                        GL_FLOAT,         
                        GL_FALSE,          
                        sizeof(glm::vec3), 
                        (void *)0         
  );

  glBindVertexArray(0);

  glGenVertexArrays(1, &voxelVAO);
  glGenBuffers(1, &voxelVBO);

  glBindVertexArray(voxelVAO);
  glBindBuffer(GL_ARRAY_BUFFER, voxelVBO);
  glBufferData(GL_ARRAY_BUFFER, voxelPositions.size() * sizeof(glm::ivec3),
               voxelPositions.data(), GL_STATIC_DRAW);
  glVertexAttribIPointer(0, 3, GL_INT, sizeof(glm::ivec3), (void *)0);
  glEnableVertexAttribArray(0);

  glBindBuffer(GL_ARRAY_BUFFER, 0);
  glBindVertexArray(0);
}

static void AddShader(GLuint ShaderProgram, const char *pShaderText,
                      GLenum ShaderType) {
  GLuint ShaderObj = glCreateShader(ShaderType);

  if (ShaderObj == 0) {
    fprintf(stderr, "Error creating shader type %d\n", ShaderType);
    exit(0);
  }

  const GLchar *p[1];
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
    fprintf(stderr, "Error compiling shader type %d: '%s'\n", ShaderType,
            InfoLog);
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

  string vs, fs, gs;

  if (!ReadFile(pVSFileName, vs)) {
    exit(1);
  }

  if (!ReadFile(pFSFileName, fs)) {
    exit(1);
  }

  if (!ReadFile(pGSFileName, gs)) {
    exit(1);
  }

  AddShader(ShaderProgram, vs.c_str(), GL_VERTEX_SHADER);
  AddShader(ShaderProgram, fs.c_str(), GL_FRAGMENT_SHADER);
  AddShader(ShaderProgram, gs.c_str(), GL_GEOMETRY_SHADER);

  GLint Success = 0;
  GLchar ErrorLog[1024] = {0};

  glLinkProgram(ShaderProgram);
  glGetProgramiv(ShaderProgram, GL_LINK_STATUS, &Success);
  if (Success == 0) {
    glGetProgramInfoLog(ShaderProgram, sizeof(ErrorLog), NULL, ErrorLog);
    fprintf(stderr, "Error linking shader program: '%s'\n", ErrorLog);
    exit(1);
  }

  // glUseProgram(ShaderProgram);
  modelLoc = glGetUniformLocation(ShaderProgram, "model");
  viewLoc = glGetUniformLocation(ShaderProgram, "view");
  projLoc = glGetUniformLocation(ShaderProgram, "projection");
  useVertexColorLoc = glGetUniformLocation(ShaderProgram, "useVertexColor");
  solidColorLoc = glGetUniformLocation(ShaderProgram, "solidColor");
  minValLoc = glGetUniformLocation(ShaderProgram, "minVal");
  maxValLoc = glGetUniformLocation(ShaderProgram, "maxVal");
  loc_volumeData = glGetUniformLocation(ShaderProgram, "volumeData");
  loc_isoValue = glGetUniformLocation(ShaderProgram, "isoValue");
  loc_volumeOrigin = glGetUniformLocation(ShaderProgram, "volumeOrigin");
  loc_volumeSpacing = glGetUniformLocation(ShaderProgram, "volumeSpacing");
  loc_volumeDimensions =
      glGetUniformLocation(ShaderProgram, "volumeDimensions");

  GLuint errorCode = glGetError();
  if (errorCode != GL_NO_ERROR) {
    fprintf(stderr, "CompileShaders: OpenGL rendering error %d\n", errorCode);
  }
}

void onInit(int argc, char *argv[], GLFWwindow *window){
  GLuint errorCode = glGetError();
  if (errorCode != GL_NO_ERROR) {
    fprintf(stderr, "onInit Start: OpenGL rendering error %d\n", errorCode);
  }

  glClearColor(0.0f, 0.0f, 0.0f, 0.0f);

  // get the grid points.
  for (int k = 0; k < vtk_file.dimensions.z; ++k) {
    for (int j = 0; j < vtk_file.dimensions.y; ++j) {
      for (int i = 0; i < vtk_file.dimensions.x; ++i) {
        glm::vec3 point = vtk_file.origin + glm::vec3(i * vtk_file.spacing.x,
                                                      j * vtk_file.spacing.y,
                                                      k * vtk_file.spacing.z);
        gridPoints.push_back(point);
        minValue = std::min(minValue, GetScalarValue(i, j, k));
        maxValue = std::max(maxValue, GetScalarValue(i, j, k));
		voxelPositions.emplace_back(i, j, k);
      }
    }
  }
  offset = minValue + (maxValue - minValue) * 0.5;

  minPoint = vtk_file.origin;
  maxPoint = vtk_file.origin +
             glm::vec3((vtk_file.dimensions.x - 1) * vtk_file.spacing.x,
                       (vtk_file.dimensions.y - 1) * vtk_file.spacing.y,
                       (vtk_file.dimensions.z - 1) * vtk_file.spacing.z);

  center = (minPoint + maxPoint) * 0.5f;

  glm::vec3 size = maxPoint - minPoint; 
  float boundingRadius =
      glm::length(size) * 0.5f; 

  float distanceFactor = 1.5f; 

  viewDirection = glm::vec3(0.0f, 0.0f, -1.0f);

  cameraPos = center - viewDirection * boundingRadius * distanceFactor;

  cameraFront = glm::normalize(center - cameraPos);

  cameraUp = glm::vec3(0.0f, 1.0f, 0.0f);

  boundingBoxVertices = {{minPoint.x, minPoint.y, minPoint.z},
                         {maxPoint.x, minPoint.y, minPoint.z},
                         {maxPoint.x, maxPoint.y, minPoint.z},
                         {minPoint.x, maxPoint.y, minPoint.z},
                         {minPoint.x, minPoint.y, maxPoint.z},
                         {maxPoint.x, minPoint.y, maxPoint.z},
                         {maxPoint.x, maxPoint.y, maxPoint.z},
                         {minPoint.x, maxPoint.y, maxPoint.z}};

  CreateVertexBuffer();

  CompileShaders();

  Initialize3DTexture();

  glEnable(GL_DEPTH_TEST);
  errorCode = glGetError();
  if (errorCode != GL_NO_ERROR) {
    fprintf(stderr, "onInit: OpenGL rendering error %d\n", errorCode);
  }
}

static void onDisplay(GLFWwindow *window) {

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
      glm::radians(60.0f), (float)width / (float)height, 0.1f, 1000.0f);

  glUseProgram(ShaderProgram);
  glUniformMatrix4fv(glGetUniformLocation(ShaderProgram, "model"), 1, GL_FALSE,
                     glm::value_ptr(model));
  glUniformMatrix4fv(glGetUniformLocation(ShaderProgram, "view"), 1, GL_FALSE,
                     glm::value_ptr(view));
  glUniformMatrix4fv(glGetUniformLocation(ShaderProgram, "projection"), 1,
                     GL_FALSE, glm::value_ptr(projection));

  glUniform3fv(glGetUniformLocation(ShaderProgram, "minPoint"), 1,
               glm::value_ptr(minPoint));
  glUniform3fv(glGetUniformLocation(ShaderProgram, "maxPoint"), 1,
               glm::value_ptr(maxPoint));

  float scalarMin = minValue;
  float scalarMax = maxValue;
  glUniform1f(glGetUniformLocation(ShaderProgram, "scalarMin"), scalarMin);
  glUniform1f(glGetUniformLocation(ShaderProgram, "scalarMax"), scalarMax);

  glActiveTexture(GL_TEXTURE0);
  glBindTexture(GL_TEXTURE_3D, scalarFieldTex);
  glUniform1i(loc_volumeData, 0); 

  glUniform1f(loc_isoValue, offset);
  glUniform3f(loc_volumeOrigin, vtk_file.origin.x, vtk_file.origin.y,
              vtk_file.origin.z);
  glUniform3f(loc_volumeSpacing, vtk_file.spacing.x, vtk_file.spacing.y,
              vtk_file.spacing.z);
  glUniform3i(loc_volumeDimensions, vtk_file.dimensions.x,
              vtk_file.dimensions.y, vtk_file.dimensions.z);

  glActiveTexture(GL_TEXTURE0);
  glBindTexture(GL_TEXTURE_3D, scalarFieldTex);
	glBindVertexArray(voxelVAO);
	glDrawArrays(GL_POINTS, 0, voxelPositions.size());
	glBindVertexArray(0);
}

static void onIdle() {
  if (isAnimating) {
    rotation += 0.001;
    // offset += 0.1;
  }
}

void onMouseButton(GLFWwindow *window, int button, int action, int mods) {

  if (button == GLFW_MOUSE_BUTTON_LEFT) {
    if (action == GLFW_PRESS) {
    } else if (action == GLFW_RELEASE) {
    }
  }
}
void framebuffer_size_callback(GLFWwindow *window, int width, int height) {
  glViewport(0, 0, width, height);
}

void onKey(GLFWwindow *window, int key, int scancode, int action, int mods) {

  if (action == GLFW_PRESS) {
    switch (key) {
    case GLFW_KEY_A:
      isAnimating = !isAnimating;
      break;
    case GLFW_KEY_R:
      rotation = 0.0f;
      break;
    case GLFW_KEY_Q:
    case GLFW_KEY_ESCAPE:
      glfwSetWindowShouldClose(window, GLFW_TRUE);
      break;
    }
  }
}

void onFramebufferSize(GLFWwindow *window, int width, int height) {
  glViewport(0, 0, width, height);
  theWindowWidth = width;
  theWindowHeight = height;
}

int main(int argc, char **argv) {
  if (!glfwInit()) {
    fprintf(stderr, "Failed to initialize GLFW\n");
    return -1;
  }

  glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
  glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 6);
  glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);


  GLFWwindow *window = glfwCreateWindow(theWindowWidth, theWindowHeight,
                                        theProgramTitle.c_str(), NULL, NULL);
  if (!window) {
    fprintf(stderr, "Failed to create GLFW window\n");
    glfwTerminate();
    return -1;
  }
  glfwMakeContextCurrent(window);
  glfwSwapInterval(0);
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
