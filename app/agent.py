from langchain_ollama import OllamaLLM
from app.config import OLLAMA_MODEL
import json

llm = OllamaLLM(model=OLLAMA_MODEL)

def analyze_resume(resume_text: str) -> dict:
    prompt = f"""
You are a professional AI resume evaluator.

Analyze the resume below and return ONLY valid JSON
with the following fields:
- score (0-100 integer)
- experience_level (Junior / Mid / Senior)
- key_skills (array of strings)
- strengths (array of strings)
- weaknesses (array of strings)
- recommendation (Hire / Maybe / Reject with reason)

Resume:
\"\"\"
{resume_text}
\"\"\"
"""

    response = llm.invoke(prompt)

    # Fallback safety (LLMs sometimes add text)
    try:
        json_start = response.find("{")
        json_end = response.rfind("}") + 1
        clean_json = response[json_start:json_end]
        return json.loads(clean_json)
    except Exception:
        return {
            "score": 0,
            "experience_level": "Unknown",
            "key_skills": [],
            "strengths": [],
            "weaknesses": ["Failed to parse resume"],
            "recommendation": "Retry"
        }
