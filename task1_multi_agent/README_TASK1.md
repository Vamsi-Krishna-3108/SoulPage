🧠 Company Intelligence Multi-Agent System

Using LangChain | Streamlit | Gemini (with automatic fallback)

This project implements a multi-agent AI system where multiple agents collaborate to collect, analyze, and summarize company-level intelligence.
The architecture uses:

Agent 1 – Data Collector

Agent 2 – Analyst Agent

LangChain Runnable Pipeline – Orchestrator

Streamlit UI – User Interface

Google Gemini API – LLM for analysis (fallback supported)

🚀 Features
✔ Multi-Agent Design

Two agents with clear roles:

Agent	Description
Data Collector Agent	Fetches company information using DuckDuckGo search (or Gemini-based collection optionally).
Analyst Agent	Uses Gemini LLM to analyze and structure the data into insights. If quota is exhausted → automatically falls back to a rule-based analysis engine.
✔ LangChain Orchestration

The system uses LangChain’s RunnableLambda to create a multi-step pipeline:

User Input → Collector Agent → Analyst Agent → Structured Report


Implemented as:

collector = RunnableLambda(run_data_collector_agent)
analyst = RunnableLambda(run_analyst_agent)

orchestrator_chain = collector | analyst


This satisfies the assignment’s requirement for agent workflow orchestration using LangChain.

✔ Streamlit UI

A simple and friendly UI for users to type a company name and receive:

Summary

Industry

Strengths

Risks

Sentiment

Full history of past queries

✔ Gemini API + Fallback

The Analyst Agent uses:

google.generativeai → gemini-2.5-flash or related models

Since the free tier has strict limits, the system gracefully handles 429 errors:

If Gemini quota is available → use real LLM output

If exhausted → automatically uses fallback_local_analysis

This makes the system reliable even without paid API access.

🏗 System Architecture Diagram
                ┌──────────────────┐
                │   Streamlit UI   │
                │  (User Input)    │
                └─────────┬────────┘
                          │
                          ▼
               ┌──────────────────────┐
               │   LangChain          │
               │   Orchestrator       │
               │  (Runnable Pipeline) │
               └─────────┬────────────┘
         company_name     │
                          ▼
          ┌───────────────────────────┐
          │   Agent 1: Data Collector │
          │  DuckDuckGo / Gemini      │
          └─────────┬─────────────────┘
                    raw_data
                          │
                          ▼
          ┌───────────────────────────┐
          │   Agent 2: Analyst Agent  │
          │  Gemini → fallback mode   │
          └─────────┬─────────────────┘
                    analysis
                          │
                          ▼
                ┌──────────────────┐
                │   Streamlit UI   │
                │  Display Output  │
                └──────────────────┘

📦 Project Structure
task1_multi_agent/
│
├── app.py                     # Streamlit UI
├── orchestrator.py            # LangChain pipeline
│
├── agents/
│   ├── data_collector_agent.py
│   ├── analyst_agent.py
│
├── requirements.txt
└── README.md                  # (this file)

🧩 How It Works
1️⃣ User enters a company name in Streamlit

Example: "TCS"

2️⃣ Data Collector Agent

Expands known abbreviations → "Tata Consultancy Services"

Searches DuckDuckGo for top company insights

Returns text summary

3️⃣ Analyst Agent

Builds a prompt → sends to Gemini → gets structured JSON:

{
  "company_name": "TCS",
  "industry": "IT Services",
  "summary": "...",
  "strengths": [...],
  "risks": [...],
  "sentiment": "positive"
}


If Gemini is unavailable → uses rule-based fallback.

4️⃣ Results are displayed on the Streamlit dashboard.
🛠 Installation & Setup
Install dependencies
pip install -r requirements.txt

Set environment variable
GEMINI_API_KEY=your_api_key_here


Or create a .env file:

GEMINI_API_KEY=your_api_key_here

Run the app
streamlit run app.py

⚠️ About Gemini API Quotas

Google offers limited free-tier requests (~20/day depending on model).
This project automatically switches to fallback analysis when:

quota exceeds

API key is missing

API errors occur

This ensures the system always works, even when LLM access is limited.

🎉 What This Project Demonstrates

Building multi-agent systems

Using AI tools in LangChain

Handling tool-based orchestration

Designing reliable LLM-based systems with fallback logic

Creating a clean interactive UI

Modular architecture suitable for extension into LangGraph
