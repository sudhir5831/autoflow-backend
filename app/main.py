from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import ResumeRequest, ResumeAnalysis
from app.agent import analyze_resume

app = FastAPI(
    title="AutoFlow AI Backend",
    version="0.2.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"status": "AutoFlow AI backend running"}

@app.post("/resume-analyze", response_model=ResumeAnalysis)
def resume_analyzer(payload: ResumeRequest):
    return analyze_resume(payload.resume_text)
