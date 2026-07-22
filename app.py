from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

# Configuration CORS pour autoriser l'interface HTML à interroger l'API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    prompt: str

@app.post("/chat")
def chat(query: Query):
    try:
        # Appel à Ollama en local
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "mistral", "prompt": query.prompt, "stream": False}
        )
        return response.json()
    except Exception as e:
        return {"error": str(e)}
