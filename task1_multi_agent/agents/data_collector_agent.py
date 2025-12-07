# agents/data_collector_agent.py

from google import genai
import os

# Load API key
api_key = os.getenv("GEMINI_API_KEY")

USE_GEMINI = bool(api_key)

if USE_GEMINI:
    try:
        client = genai.Client(api_key=api_key)
        MODEL = "gemini-2.5-flash"     # free tier model
        print("[DataCollector] Gemini client initialized.")
    except:
        print("[DataCollector] Gemini init failed. Falling back to basic output.")
        USE_GEMINI = False
else:
    print("[DataCollector] GEMINI_API_KEY missing — using fallback.")


def run_data_collector_agent(company_name: str) -> dict:
    """
    Agent 1: Collect company details using Gemini itself.
    This replaces DuckDuckGo/Wikipedia.
    """

    # If no AI available, fallback:
    if not USE_GEMINI:
        return {
            "company_name": company_name,
            "search_summary": f"No AI source available for {company_name}.",
        }

    prompt = f"""
You are a company research assistant.

Provide a clean, factual, compact overview about the company named:
**{company_name}**

Return structured paragraphs including:

- Company overview  
- What the company does (products/services)  
- Industry and domains  
- Market presence (global or Indian)  
- Recent updates/news (last 12–18 months)  
- Any known acquisitions or partnerships  
- Competitors  

Do NOT add anything imaginative or fake.
Only return verified or widely-known facts.
Do NOT format in JSON.
"""

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )

        summary = response.text or ""
        print(f"[DataCollector] AI Data collected for: {company_name}")

        return {
            "company_name": company_name,
            "search_summary": summary,
        }

    except Exception as e:
        print("[DataCollector] AI Data fetch failed:", e)
        return {
            "company_name": company_name,
            "search_summary": f"AI error while collecting data for {company_name}.",
        }
