from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import shutil
import os
from analysis import analyze_text
from rewrite import rewrite_text, transcribe_audio, generate_reply # <--- Importamos la nueva función

app = FastAPI(title="Soporte AI Multimodal")

class TextRequest(BaseModel):
    text: str
    tone: str
    language: str = "Español"

@app.post("/analyze")
def analyze(req: TextRequest): # Simplificado para usar el mismo modelo
    return {"analysis": analyze_text(req.text)}

@app.post("/rewrite")
def rewrite(req: TextRequest):
    result = rewrite_text(req.text, req.tone, req.language)
    return {"rewritten_text": result}

@app.post("/reply") # <--- NUEVO ENDPOINT PARA DEMO 2
def reply(req: TextRequest):
    result = generate_reply(req.text, req.tone, req.language)
    return {"reply_text": result}

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    temp_filename = f"temp_{file.filename}"
    with open(temp_filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    try:
        transcript = transcribe_audio(temp_filename)
        return {"transcription": transcript}
    finally:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)