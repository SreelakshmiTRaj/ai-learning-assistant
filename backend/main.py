from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from agent import concept_agent, quiz_agent, study_agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ConceptRequest(BaseModel):
    topic: str
    level: str


class QuizRequest(BaseModel):
    topic: str
    difficulty: str


class StudyRequest(BaseModel):
    subjects: str
    days: int
    hours: int


@app.post("/explain")

def explain(req: ConceptRequest):
    result = concept_agent(req.topic, req.level)
    return {"result": result}


@app.post("/quiz")

def quiz(req: QuizRequest):
    result = quiz_agent(req.topic, req.difficulty)
    return {"result": result}


@app.post("/study-plan")

def study_plan(req: StudyRequest):
    result = study_agent(req.subjects, req.days, req.hours)
    return {"result": result}