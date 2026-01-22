from pydantic import BaseModel

class ResumeRequest(BaseModel):
    resume_text: str

class ResumeAnalysis(BaseModel):
    score: int
    experience_level: str
    key_skills: list[str]
    strengths: list[str]
    weaknesses: list[str]
    recommendation: str
