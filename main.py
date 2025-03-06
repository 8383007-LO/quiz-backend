from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Query
from pydantic import BaseModel
import random

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Byt ut "*" mot frontend-URL om du vill begränsa åtkomst
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

quiz_questions = {
    "demokrati": [
        {"question": "Vad är en folkomröstning?", 
         "options": ["A) Ett val till riksdagen", "B) En direkt röstning av folket i en specifik fråga", "C) En riksdagsdebatt", "D) Ett möte mellan partiledare"],
         "answer": "B",
         "explanation": "En folkomröstning innebär att folket röstar direkt om en enskild fråga."}
    ]
}

class QuizRequest(BaseModel):
    category: str

@app.get("/quiz/")
def get_quiz(category: str = Query(..., description="Välj en kategori som demokrati")):
    if category not in quiz_questions:
        return {"error": "Kategori finns inte. Välj t.ex. 'demokrati'"}
    
    question_data = random.choice(quiz_questions[category])
    return {
        "question": question_data["question"],
        "options": question_data["options"],
        "answer": question_data["answer"],
        "explanation": question_data["explanation"]
    }
