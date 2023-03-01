#pragma once
class IndexBuffer {
private:
	unsigned int m_RendererID; //id for every object we allocate in opengl / internal renderer id
	unsigned int m_Count;
public:
	IndexBuffer(const unsigned int* data, unsigned int count);
	~IndexBuffer(); //destructor

	void Bind() const;
	void Unbind() const;

	inline unsigned int GetCount() const { return m_Count; }
};