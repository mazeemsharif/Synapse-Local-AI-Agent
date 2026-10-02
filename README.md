markdown
# ⚡ Synapse - Local LLM Agent with Web Search

Synapse is a fully local AI agent built with Streamlit, Ollama, and LangChain. It combines a locally hosted Large Language Model with real-time web search capabilities via the Tavily API (using MCP).

## 🚀 Features
- **Fully Local LLM:** Runs `llama3.2` locally via Ollama (no cloud inference costs, complete privacy).
- **Real-time Web Search:** Integrates Tavily API to fetch current information from the internet.
- **Interactive UI:** Built with Streamlit for a smooth chat experience.
- **Conversation History:** Sidebar panel to view past messages.
- **Reset Button:** Easily clear the chat history.

## 🛠️ Tech Stack
- **Language:** Python
- **Frontend:** Streamlit
- **Local LLM:** Ollama (Llama 3.2)
- **Agent Framework:** LangChain, LangGraph
- **Web Search:** Tavily API (via Model Context Protocol - MCP)

## ⚙️ Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mazeemsharif/Synapse-Local-AI-Agent.git
   cd Synapse-Local-AI-Agent
Install Ollama and pull the model:
Download Ollama from ollama.com and run:

bash
ollama pull llama3.2
Create a virtual environment and install dependencies:

bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
Set your Tavily API Key:
Get a free key from tavily.com.

bash
# Windows PowerShell:
$env:TAVILY_API_KEY="your-api-key-here"
Run the app:

bash
streamlit run app.py

## 👩‍💻 Author
M.Azeem 
- Generative AI Intern at Arch Technologies
- GitHub: https://github.com/mazeemsharif
- LinkedIn: www.linkedin.com/in/muhammad-azeem-sharif-00853122a
