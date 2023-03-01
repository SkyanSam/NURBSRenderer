#include "Renderer.h"
void GLClearError() {
    while (glGetError() != GL_NO_ERROR); // or !glGetError()
}
void GLCheckError() {
    while (GLenum error = glGetError()) {
        std::cout << "OpenGL Error [( " << error << " )]" << std::endl;
    }
}
bool GLLogCall(const char* function, const char* file, int line) {
    while (GLenum error = glGetError()) {
        std::cout << "OpenGL Error [( " << error << " )]" << function << " " << file << " Line " << line << std::endl;
        return false;
    }
    return true;
}