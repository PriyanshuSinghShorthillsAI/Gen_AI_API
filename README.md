# ChatGPT-like Text Generation with Local Llama 3.1

This project demonstrates a simple implementation of **text-to-text generation** using the **Llama 3.1** model, running locally. Additionally, the project will include a future enhancement for generating valuable insights from PDF files.

---

## **Objective**

- **Task 1**: Build a local text generation tool that accepts user input and generates contextually relevant responses using the **Llama 3.1** model.
- **Task 2**: Implement PDF insight extraction, which will analyze and extract key information from uploaded PDF documents, such as summaries, tables, and valuable insights.

---

## **Features**

### **1. Text-to-Text Generation**
- Local execution of the **Llama 3.1** model for enhanced privacy and control.
- Generates human-like, context-aware text responses based on user input.

### **2. PDF Insights Extraction (Future Feature)**
- Extract and analyze key insights from PDF documents:
  - Generate summaries of the content.
  - Extract tables, images, figures, and URLs.
  - Identify and present actionable insights from document analysis.

---

## **Tech Stack**

- **Programming Language**: Python
- **Large Language Model**: Llama 3.1 (running locally)
- **Library**: Ollama (for interacting with Llama locally)

---

## **Setup Instructions**

### **1. Prerequisites**
- Ensure **Python 3.7+** is installed.
- Install **Ollama** (which allows you to run the Llama 3.1 model locally). Visit [Ollama's download page](https://ollama.com/download) to install Ollama for your platform.

### **2. Install Python Dependencies**
Install the required Python library using pip:
```bash
pip install ollama
ollama pull llama3.1
