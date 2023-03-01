#include "VertexArray.h"
#include "Renderer.h"

VertexArray::VertexArray()
{
}

VertexArray::~VertexArray()
{
}

void VertexArray::AddBuffer(const VertexBuffer& vb, const VertexBufferLayout& layout)
{
	vb.Bind();
	const auto& elements = layout.GetElements();
	for (unsigned int i = 0; i < elements.size(); i++) {
		const auto& element = elements[i];
		GLCall(glVertexAttribPointer(i, element.count, element.type, element.normalized, sizeof(float) * 2, 0));
		GLCall(glEnableVertexAttribArray(i));
	}
}
