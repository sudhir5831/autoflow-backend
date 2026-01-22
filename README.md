# AutoFlow AI Backend

An intelligent resume analysis backend powered by AI, built with FastAPI and Ollama.

## Overview

AutoFlow AI Backend provides an API endpoint to analyze resumes using the Mistral LLM model. It evaluates candidate qualifications, skills, experience level, and provides hiring recommendations.

## Features

- **Resume Analysis**: Evaluates resumes and provides detailed assessments
- **AI-Powered Scoring**: Uses Ollama/Mistral for intelligent analysis
- **Structured Output**: Returns JSON-formatted analysis with scores, skills, strengths, and weaknesses
- **Error Handling**: Graceful fallback handling for parsing failures
- **CORS Support**: Pre-configured for frontend integration

## Tech Stack

- **Framework**: FastAPI
- **LLM**: Ollama (Mistral model)
- **Language**: Python 3.x

## Setup

### Prerequisites

- Python 3.8+
- Ollama installed and running with Mistral model
- pip

### Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install fastapi uvicorn langchain-ollama
```

3. Ensure Ollama is running:
```bash
ollama serve
```

### Configuration

Edit `app/config.py` to change the LLM model:
```python
OLLAMA_MODEL = "mistral"  # Change to your preferred model
```

## Running the Server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Health Check
```
GET /
```
Returns status of the backend.

### Resume Analysis
```
POST /resume-analyze
```

**Request Body:**
```json
{
  "resume_text": "Your resume content here..."
}
```

**Response:**
```json
{
  "score": 85,
  "experience_level": "Senior",
  "key_skills": ["Python", "FastAPI", "AI/ML"],
  "strengths": ["Strong technical background", "Good communication"],
  "weaknesses": ["Limited leadership experience"],
  "recommendation": "Hire"
}
```

## Project Structure

```
app/
├── agent.py       # Resume analysis logic
├── config.py      # Configuration settings
├── main.py        # FastAPI application
├── schemas.py     # Pydantic models
└── __pycache__/   # Python cache
```

## Development

The frontend is configured to connect via CORS at `http://localhost:5173`.

## License

MIT
