import google.generativeai as genai
import os
from dotenv import load_dotenv

# Cargar tu clave
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ Error: No encontré la API KEY en el archivo .env")
else:
    print(f"✅ Clave encontrada: {api_key[:5]}...")
    genai.configure(api_key=api_key)

    print("\n🔍 Consultando a Google qué modelos tenés disponibles...")
    try:
        found_any = False
        for m in genai.list_models():
            # Filtramos solo los que sirven para generar texto (chat)
            if 'generateContent' in m.supported_generation_methods:
                print(f" - {m.name}")
                found_any = True
        
        if not found_any:
            print("⚠️ No encontré modelos. Puede ser un problema de permisos de la clave.")
            
    except Exception as e:
        print(f"❌ Error de conexión: {e}")