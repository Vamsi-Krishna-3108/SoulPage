# 🚀 Soulpage IT Solutions – GenAI Assignments  
This repository contains both **Task 1 (Multi‑Agent Company Intelligence System)** and **Task 2 (Local ChatGPT Conversational Bot)**.  
Each assignment demonstrates different GenAI principles including **multi‑agent orchestration**, **tool usage**, **offline LLMs**, **memory systems**, and **Streamlit UI development**.

---

# 🧩 Assignment Overview

## ✅ **Task 1 – Multi‑Agent Company Intelligence System**  
**Goal:** Build an automated multi‑agent pipeline capable of collecting information about a company and generating structured analysis using LLMs.

### ✔ Key Concepts Demonstrated
- Multi‑Agent Architecture  
- Tool Use (DuckDuckGo/Wikipedia/Gemini Search)  
- LangChain‑style Orchestrator  
- JSON‑structured LLM outputs  
- Streamlit UI for user interaction  
- Fallback mechanism when Gemini quota is exceeded  

---

# 🧠 Task 1 – System Architecture

```
              ┌─────────────────────────────┐
              │        Streamlit UI         │
              │       (User Input Box)      │
              └───────────────┬─────────────┘
                              ▼
                       Company Name
                              ▼
                       ┌────────────┐
                       │Orchestrator│
                       └──────┬─────┘
                              ▼
         ┌───────────────────────────────────────┐
         │       Agent 1: Data Collector         │
         │ DuckDuckGo / Wikipedia / Gemini Search│
         └───────────────┬───────────────────────┘
                          ▼
                      Raw Data
                          ▼
               ┌──────────────────────┐
               │ Agent 2: Analyst     │
               │  (Gemini or Fallback)│
               └──────────┬───────────┘
                          ▼
               Structured Insights JSON
                          ▼
              ┌──────────────────────────────┐
              │     Streamlit UI Display     │
              │Summary • Strengths • Risks   │
              └──────────────────────────────┘
```

### 🔎 Agent Responsibilities

#### **🔹 Agent 1 – Data Collector**
Fetches public information using:
- DuckDuckGo search
- Wikipedia summaries
- Optional Gemini Search

Returns:
- Titles
- Snippets
- Short Summary

#### **🔹 Agent 2 – Analyst Agent**
Two modes:
1. **Gemini Professional LLM** → Returns structured JSON  
2. **Fallback Rule‑Based Engine** → Used when API quota is exceeded  

This ensures **100% reliability**.

#### **🔹 Orchestrator**
Coordinates the workflow:
- Receives company name  
- Calls Data Collector  
- Passes data to Analyst  
- Returns merged analysis  

---

# 🎨 Task 1 – Streamlit UI

Features:
- Search bar for entering company name  
- Real‑time analysis output  
- Color‑coded sections (Summary, Strengths, Risks)  
- API error handling  

---

# 📁 Task 1 Folder Structure

```
task1_multi_agent/
│── app.py               # Streamlit frontend
│── orchestrator.py      # Pipeline orchestrator
│── requirements.txt
│── README_TASK1.md
│
├── agents/
│   ├── data_collector_agent.py
│   └── analyst_agent.py
└── .env                 # GEMINI_API_KEY
```

---

# 🤖 Task 2 – Local ChatGPT (Offline Conversational Bot)

**Goal:** Create an offline conversational AI chatbot replicating ChatGPT’s experience.

### ✔ Key Concepts Demonstrated
- Offline LLM (Ollama – Llama3.2:1b)
- Streamlit ChatGPT‑style UI (`st.chat_message`, `st.chat_input`)
- File‑based conversational memory
- Auto memory reset
- Strict prompting for small models  
- Runs without API keys & without Internet

---

# 🧠 Task 2 – System Architecture

```
                    ┌────────────────────────┐
                    │    Streamlit UI        │
                    │  ChatGPT‑style chat UI │
                    └───────────┬────────────┘
                                ▼
                     User Message Input
                                ▼
                     ┌────────────────────┐
                     │  Memory Loader     │
                     │ chat_history.txt   │
                     └─────────┬──────────┘
                               ▼
                 ┌──────────────────────────┐
                 │  Prompt Constructor      │
                 │ Injects memory + message │
                 └───────────┬─────────────┘
                             ▼
              ┌─────────────────────────────┐
              │ Local LLM (Ollama – Llama3) │
              └───────────┬─────────────────┘
                          ▼
                AI Response Generated
                          ▼
                Saved Back to Memory File
                          ▼
                     Displayed in UI
```

---

# 🎨 Task 2 – ChatGPT‑Style UI

### Includes:
- AI messages (left bubble)
- User messages (right bubble)
- Smooth scrolling
- Reset Conversation button
- Minimalistic clean layout

### Memory Logic
Memory stored in:
```
chat_history.txt
```
Deleted automatically on:
- User presses Reset
- User types exit (CLI)

---

# 📁 Task 2 Folder Structure

```
task2_chat_bot/
│── app.py                # Streamlit ChatGPT-like UI
│── chat_history.txt      # Auto-generated conversation memory
│── requirements.txt
└── README_TASK2.md
```

---

# 🔧 Technologies Used

### **Common**
- Python 3.11
- Streamlit
- LangChain (selective use)
- JSON handling

### **Task 1**
- DuckDuckGo Search API
- Gemini API (optional)
- Wikipedia scraping
- Multi-agent orchestration

### **Task 2**
- Ollama (LLM runtime)
- Llama3.2:1b model
- Streamlit chat components

---

# 🚀 Running Both Projects

## ▶️ **Run Task 1**
```
cd task1_multi_agent
pip install -r requirements.txt
streamlit run app.py
```

## ▶️ **Run Task 2**
```
cd task2_chat_bot
pip install -r requirements.txt
streamlit run app.py
```

---

# 🏁 Conclusion

This repository demonstrates two core GenAI skills:

### **✔ Multi‑Agent System Design (Task 1)**  
Real‑world production‑like pipeline with agents, tools, LLMs, and fallbacks.

### **✔ ChatGPT‑Style Conversational System (Task 2)**  
A fully offline, Streamlit‑based chatbot with contextual memory.

Both assignments showcase:
- Strong architecture  
- Practical GenAI engineering  
- Clean UI  
- Tool integration  
- LLM fallback & resilience  
- Clear documentation  

---

# 📜 License  
MIT License  
