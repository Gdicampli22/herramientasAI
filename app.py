from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import shutil
import os
import tempfile
from rewrite import rewrite_text, generate_reply, transcribe_audio

app = FastAPI(title="Backend Soporte AI")

# --- MODELOS DE DATOS ---
class TextRequest(BaseModel):
    text: str
    tone: str
    language: str

# --- ENDPOINTS ---
@app.get("/")
def home():
    return {"status": "Backend AI funcionando en Vercel 🚀"}

@app.post("/rewrite")
def endpoint_rewrite(req: TextRequest):
    return {"rewritten_text": rewrite_text(req.text, req.tone, req.language)}

@app.post("/reply")
def endpoint_reply(req: TextRequest):
    return {"reply_text": generate_reply(req.text, req.tone, req.language)}

@app.post("/transcribe")
async def endpoint_transcribe(file: UploadFile = File(...)):
    # Manejo seguro de archivos temporales para Serverless
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
        shutil.copyfileobj(file.file, temp_file)
        temp_path = temp_file.name
    
    try:
        text = transcribe_audio(temp_path)
        return {"transcription": text}
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)