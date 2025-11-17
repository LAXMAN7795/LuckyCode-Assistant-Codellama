# LuckyCode-Assistant (CodeLlama + Ollama + Gradio)

LuckyCode-Assistant is a local AI-powered code assistant built using **CodeLlama**, **Ollama**, and **Gradio**.  
It runs completely offline and is designed to help with programming tasks such as debugging, explaining concepts, generating code, and improving developer productivity.

---

## 🚀 Features

- Runs on your local machine using **Ollama**
- Powered by **CodeLlama**, Meta’s coding-optimized LLM
- Custom model named **LuckyCode**
- Gradio-based interactive UI
- Supports conversation history
- Works offline (no API keys needed)

---

## 🧠 About CodeLlama

**CodeLlama** is a specialized version of Llama 2, fine-tuned specifically for programming.  
It supports many languages like Python, C++, JavaScript, Java, PHP, C#, Bash, and more.

### Key capabilities:
- Code generation & explanation  
- Code infilling  
- Long-context understanding  
- Multi-language support  
- Available in 7B–70B parameter variants  
- Open-access and free for research/commercial use  

---

## ❌ Why Not Llama-2?

Llama-2 is general-purpose and not optimized for code.  
Its limitations include:
- Weaker coding accuracy  
- Poor reasoning for complex problems  
- Small context window  
- High prompt sensitivity  

CodeLlama fixes these and performs much better for coding tasks.

---

## 🛠️ Setup Instructions

### 1️⃣ Install **Ollama**
Download and install Ollama from:
- https://ollama.com/download

### 2️⃣ Pull the CodeLlama model
Run the following in your terminal:
- `ollama run codellama`

This downloads the base model.

### 3️⃣ Create a Conda environment
- Create environment with Python 3.10  
- Activate it in VS Code for development  

### 4️⃣ Create a custom model
Add a `modelfile` in the project to define:
- The base model (`codellama`)
- Temperature settings  
- System prompt for LuckyCode  

Then create your model using `ollama create`.

### 5️⃣ Install dependencies  
Add required libraries such as:
- Gradio  
- LangChain  
- Requests  

Install them using your environment.

### 6️⃣ Run the assistant  
Launch the Gradio app to access the UI in your browser.

---

## 📁 Project Structure

LuckyCode-Assistant/
│── modelfile
│── app.py
│── requirements.txt
│── README.md
└── (your conda environment ignored)

---

## 🔒 .gitignore Note

If your Conda environment is stored inside the project folder (e.g., `codeAssist/`),  
add it to `.gitignore` to avoid pushing it to GitHub.

---

## 📜 License

CodeLlama models are licensed under Meta’s **Llama Community License**.

---

## 👤 Author

**Laxman Sannu Gouda** 
Creator of **LuckyCode – AI Code Assistant**

---

⭐ If you like this project, consider giving it a star on GitHub!
