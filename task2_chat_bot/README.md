# 🧠 Local ChatGPT – Conversational AI Bot (Streamlit + Ollama)

A fully offline ChatGPT-style AI assistant built using:

- **Ollama** (local LLaMA model – no API keys required)
- **Streamlit Chat UI** (ChatGPT-like interface)
- **File-based memory** (persists conversation between turns)
- **Python 3.11**
- **No Internet needed**
- **Free and open-source**

This bot remembers previous messages, responds naturally, and gives a beautiful ChatGPT-like chat experience — all running on your own machine.

## 🚀 Features

✔ Offline LLM (Ollama)  
✔ ChatGPT-style interface  
✔ File-based memory  
✔ Reset button  
✔ Runs on any OS  
✔ No API keys needed  

## 📁 Project Structure

```
task2_chat_bot/
│
├── app.py
├── chat_history.txt
├── requirements.txt
└── README.md
```

## 🛠️ Installation

### 1. Install Python 3.11  
https://www.python.org/downloads/release/python-3110/

### 2. Install Ollama  
https://ollama.com/download

Pull model:
```
ollama pull llama3.2:1b
```

### 3. Create Virtual Environment
```
python -m venv .venv
```

Activate:
- Windows: `.\.venv\Scripts\activate`
- Linux/macOS: `source .venv/bin/activate`

### 4. Install Dependencies
```
pip install -r requirements.txt
```

## ▶️ Run the Chatbot

```
streamlit run app.py
```

Open browser:
```
http://localhost:8501
```

## 🧩 How It Works

- Loads chat memory from a text file  
- Builds a structured prompt  
- Uses local LLaMA model to generate responses  
- Saves new messages to the memory file  
- Reset deletes memory  

## 📦 requirements.txt
```
streamlit
langchain-community
langchain-ollama
```

## 📄 License
MIT License
