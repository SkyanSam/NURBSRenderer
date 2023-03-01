#pragma once
class VertexBuffer {
private:
	unsigned int m_RendererID; //id for every object we allocate in opengl / internal renderer id
public:
	VertexBuffer(const void* data, unsigned int size);
	~VertexBuffer(); //destructor

	void Bind() const;
	void Unbind() const;
};