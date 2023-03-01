#pragma once

#include <iostream>
#include <GL/glew.h>
#include <GLFW/glfw3.h>

#include <fstream>
#include <sstream>

#define ASSERT(x) if (!(x)) __debugbreak(); // specific to MSVC
#define GLCall(x) GLClearError();\
    x;\
    ASSERT(GLLogCall(#x, __FILE__, __LINE__))

void GLClearError();
void GLCheckError();
bool GLLogCall(const char* function, const char* file, int line);