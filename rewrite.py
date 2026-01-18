import os
import google.generativeai as genai
from dotenv import load_dotenv
import tempfile

load_dotenv()

# Configuración segura de API Key
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

generation_config = {
  "temperature": 0.4,
  "max_output_tokens": 1024, # Reducido un poco para velocidad en Serverless
}

# Modelo
model = genai.GenerativeModel(
  model_name="gemini-3-flash-preview", # Usamos Flash estándar por estabilidad
  generation_config=generation_config,
)

def rewrite_text(text: str, tone: str, language: str):
    if not api_key: return "Error: Falta GOOGLE_API_KEY."
    prompt = f"""
    Actúa como Supervisor de Soporte.
    TAREA: Mejorar este borrador.
    IDIOMA: {language}. TONO: {tone}.
    BORRADOR: "{text}"
    Solo devuelve el texto mejorado.
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error Gemini: {str(e)}"

def generate_reply(text: str, tone: str, language: str):
    if not api_key: return "Error: Falta GOOGLE_API_KEY."
    prompt = f"""
    Actúa como Agente Experto.
    TAREA: Responder a este cliente.
    MENSAJE CLIENTE: "{text}"
    IDIOMA: {language}. TONO: {tone}.
    Estructura: Saludo -> Solución -> Cierre.
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error Gemini: {str(e)}"

def transcribe_audio(file_path: str):
    if not api_key: return "Error: Falta GOOGLE_API_KEY."
    try:
        # En Vercel no podemos guardar archivos persistentes, 
        # así que asumimos que file_path es temporal y válido
        audio_file = genai.upload_file(path=file_path)
        prompt = "Transcribe este audio palabra por palabra."
        response = model.generate_content([prompt, audio_file])
        return response.text.strip()
    except Exception as e:
        return f"Error Transcripción: {str(e)}"