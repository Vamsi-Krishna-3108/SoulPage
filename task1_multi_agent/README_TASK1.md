
# 🚀 Multi-Agent Company Intelligence System  
**Using LangChain + Streamlit + DuckDuckGo + Gemini (with fallback)**  

This project demonstrates a complete **multi-agent AI pipeline**:

- **Agent 1 – Data Collector** (DuckDuckGo or Wikipedia or Gemini Search)
- **Agent 2 – Analyst Agent** (Gemini or fallback rule-based engine)
- **Orchestrator** (LangChain-style controller)
- **Streamlit UI** for interaction  
- **Automatic fallback** when Gemini API quota is exceeded

---

## ⚙️ Features

### ✅ Multi-Agent Workflow  
Each agent performs a specific step and passes results forward.

### ✅ LangChain-style Orchestration  
Central pipeline to coordinate all agents.

### ✅ Robust Fallback System  
Since free Gemini quota is limited:  
- If Gemini works → **LLM-powered structured JSON**  
- If Gemini exceeds quota → **Rule-based fallback analysis**

This ensures reliability even without API credits.

---

## 🧠 System Architecture

```
              ┌─────────────────────────────┐
              │        Streamlit UI         │
              │       (User Input Box)      │
              └───────────────┬─────────────┘
                              ▼
                  [ company_name entered ]

                       ┌────────────┐
                       │Orchestrator│
                       │ (Pipeline) │
                       └──────┬─────┘
                              ▼
         ┌────────────────────────────────────────────┐
         │        Agent 1: Data Collector              │
         │  (DuckDuckGo / Wikipedia / Gemini Search)   │
         └───────────────┬────────────────────────────┘
                          ▼
                    raw_data dict

                       ┌────────────┐
                       │Agent 2:     │
                       │ Analyst     │
                       └──────┬─────┘
                              ▼
     ┌──────────────────────────────────────────────────────┐
     │ If Gemini quota available → LLM JSON analysis         │
     │ If Gemini fails/429 → fallback_local_analysis         │
     └──────────────────────────────────────────────────────┘

                              ▼
                     structured analysis

              ┌─────────────────────────────┐
              │     Streamlit UI Output     │
              │ Summary • Strengths • Risks │
              └─────────────────────────────┘
```

---

## 📂 Project Structure

```
task1_multi_agent/
│── app.py               # Streamlit frontend
│── orchestrator.py      # LangChain-style pipeline
│── requirements.txt
│── README.md / README_TASK1.md
│
├── agents/
│   ├── data_collector_agent.py
│   └── analyst_agent.py
└── .env                 # GEMINI_API_KEY
```

---

## 🌱 How It Works

### **1️⃣ User enters a company name**
Example: `"TCS"`

### **2️⃣ Data Collector Agent**
- Uses DuckDuckGo/Wikipedia to fetch:
  - Titles  
  - Snippets  
  - Summaries  

### **3️⃣ Analyst Agent (Gemini or fallback)**
- Attempts Gemini LLM JSON output  
- If API quota exhausted → rule-based fallback

### **4️⃣ Output shown on UI**
- Summary  
- Strengths  
- Risks  
- Sentiment  

---

## 🧪 Running the Project

### Install dependencies  
```
pip install -r requirements.txt
```

### Add your Gemini API key  
Create `.env`:

```
GEMINI_API_KEY=your_key_here
```

### Launch the UI  
```
streamlit run app.py
```

---

## 🏆 Why This Project Meets the Assignment Requirements

✔ Multi-agent system  
✔ LangChain-style orchestrator  
✔ Tool usage (search tools + LLM)  
✔ Streamlit UI  
✔ Clear architecture documentation  
✔ Robust fallback  
✔ Perfect for Task 1 submission  

---

## 📸 Screenshots  
![image1](image.png)

---

## 📘 License  
MIT License  
