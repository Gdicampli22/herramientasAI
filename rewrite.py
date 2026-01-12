import os
import google.generativeai as genai
from dotenv import load_dotenv

# Cargar variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Configuración del modelo (Gemini 3 Flash Preview)
generation_config = {
  "temperature": 0.4,
  "max_output_tokens": 2048,
}

# TU MODELO (Asegurate que sea el que te funcionó: gemini-3-flash-preview)
model = genai.GenerativeModel(
  model_name="gemini-3-flash-preview", 
  generation_config=generation_config,
)

def rewrite_text(text: str, tone: str, language: str):
    """Reescribe un borrador del agente."""
    prompt = f"""
    Actúa como un Supervisor de Soporte Técnico.
    TAREA: Reescribe este borrador para mejorarlo.
    IDIOMA: {language}.
    TONO: {tone}.
    
    Borrador original: "{text}"
    
    Solo devuelve el texto mejorado:
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def generate_reply(text: str, tone: str, language: str):
    """Genera una respuesta a una consulta de un cliente."""
    prompt = f"""
    Actúa como un Agente de Soporte Experto.
    TAREA: Genera una respuesta completa para este mensaje del cliente.
    MENSAJE DEL CLIENTE: "{text}"
    
    REQUISITOS:
    - IDIOMA RESPUESTA: {language}
    - TONO: {tone}
    - Estructura: Saludo empático -> Solución/Respuesta -> Cierre profesional.
    - NO inventes datos técnicos específicos (usa [marcador] si faltan datos).
    
    Respuesta sugerida:
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def transcribe_audio(file_path: str):
    """Transcribe audio a texto."""
    try:
        audio_file = genai.upload_file(path=file_path)
        prompt = "Transcribe este audio exactamente palabra por palabra."
        response = model.generate_content([prompt, audio_file])
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"