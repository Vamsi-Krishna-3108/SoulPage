# agents/analyst_agent.py

from dotenv import load_dotenv
load_dotenv()

from typing import Dict
import json
import os

from google import genai
from google.genai import types


# ---------- Gemini setup ----------

api_key = os.getenv("GEMINI_API_KEY")

USE_GEMINI = bool(api_key)

if USE_GEMINI:
    try:
        client = genai.Client(api_key=api_key)
        MODEL = "gemini-2.5-flash"   # free / light model
        print("[AnalystAgent] Gemini client initialized.")
    except Exception as e:
        print("[AnalystAgent] Gemini init failed:", e)
        USE_GEMINI = False
else:
    print("[AnalystAgent] GEMINI_API_KEY not set – using fallback_local_analysis.")


# ---------- Prompt builder ----------

def build_analysis_prompt(raw_data: Dict) -> str:
    company_name = raw_data.get("company_name", "the company")
    search_summary = raw_data.get("search_summary", "")

    prompt = f"""
You are a company intelligence analyst.

Analyze the following information about a company and produce a structured JSON
with the following keys:
- company_name
- industry  (guess if not explicitly mentioned)
- summary   (2-4 sentences)
- strengths (list of 3 bullet points)
- risks     (list of 3 bullet points)
- sentiment (one of: "positive", "negative", "mixed")

Company: {company_name}


Return ONLY valid JSON. Do not include any explanations or markdown.
"""
    return prompt


# ---------- Fallback (no Gemini) ----------

def fallback_local_analysis(raw_data: Dict) -> Dict:
    """
    Simple rule-based analysis when Gemini is not available.
    """
    company_name = raw_data.get("company_name", "Unknown company")
    text = raw_data.get("search_summary", "")

    cleaned = text.replace("\n", " ")
    sentences = [s.strip() for s in cleaned.split(".") if s.strip()]
    summary = ". ".join(sentences[:3])
    if summary and not summary.endswith("."):
        summary += "."

    lowered = text.lower()
    if "software" in lowered or "it services" in lowered or "technology" in lowered:
        industry = "Information Technology / Software"
    elif "bank" in lowered or "financial" in lowered:
        industry = "Banking / Financial Services"
    elif "automotive" in lowered or "car" in lowered or "vehicle" in lowered:
        industry = "Automotive / Mobility"
    elif "pharma" in lowered or "biotech" in lowered:
        industry = "Pharmaceuticals / Healthcare"
    else:
        industry = "Unknown / Mixed"

    strengths = [
        f"Established presence in the {industry} domain.",
        "Recognizable brand mentioned in multiple sources.",
        "Potential for growth based on recent activities and partnerships.",
    ]

    risks = [
        "Subject to competition from other players in the same industry.",
        "Sensitive to macroeconomic and regulatory changes.",
        "Public information may not reflect internal challenges.",
    ]

    if any(word in lowered for word in ["growth", "record profit", "expansion", "partnership"]):
        sentiment = "positive"
    elif any(word in lowered for word in ["loss", "scandal", "fraud", "decline"]):
        sentiment = "negative"
    else:
        sentiment = "mixed"

    return {
        "company_name": company_name,
        "industry": industry,
        "summary": summary or f"{company_name} operates in the {industry} sector.",
        "strengths": strengths,
        "risks": risks,
        "sentiment": sentiment,
    }


# ---------- Main agent function ----------

def run_analyst_agent(raw_data: Dict) -> Dict:
    """
    Agent 2: tries Gemini first (if configured), falls back to local analysis
    if Gemini is unavailable (no key, quota exceeded, other error).
    """

    if not USE_GEMINI:
        print("[AnalystAgent] USE_GEMINI=False – using fallback_local_analysis.")
        return fallback_local_analysis(raw_data)

    prompt = build_analysis_prompt(raw_data)

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt,
        )

        content = response.text or ""

        # Try parsing JSON from Gemini output
        analysis = json.loads(content)
        return analysis

    except Exception as e:
        print(f"[AnalystAgent] Gemini failed ({type(e).__name__}): {e}")
        print("[AnalystAgent] Falling back to local rule-based analysis.")
        return fallback_local_analysis(raw_data)
