import streamlit as st
import requests
from PIL import Image

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="AI Auto-Respuesta", page_icon="🤖", layout="centered")
# Si estamos en Streamlit Cloud, usamos la URL de Render.
# Si estamos en tu PC, usamos localhost.
if "RENDER_URL" in st.secrets:
    API_URL = st.secrets["https://herramientasai.onrender.com/"]
else:
    API_URL = "http://127.0.0.1:8000"
YOUR_NAME = "Gastón Di Campli" # <--- Pon tu nombre

# --- HEADER & LOGO ---
try:
    logo = Image.open("logo.png")
    st.image(logo, use_container_width=True)
except:
    st.title("🤖 Generador de Respuestas AI")

st.markdown("### Genera una respuesta completa desde cero")

# --- ENTRADA ---
client_msg = st.text_area("Mensaje del Cliente (Consulta, Queja, Error):", height=150, placeholder="Ej: El sistema me está dando error 504 cuando intento pagar...")

# --- PROCESO ---
if client_msg:
    col1, col2 = st.columns(2)
    with col1:
        tone = st.selectbox("Tono de Respuesta:", ["Empático y Resolutivo", "Técnico y Formal", "Venta Consultiva"])
    with col2:
        language = st.selectbox("Idioma de Respuesta:", ["Español", "English", "Português"])
        
    if st.button("🚀 Generar Respuesta", type="primary"):
        with st.spinner("Analizando y redactando respuesta..."):
            try:
                # Nota: Llama al endpoint /reply
                res = requests.post(f"{API_URL}/reply", json={"text": client_msg, "tone": tone, "language": language})
                if res.status_code == 200:
                    reply_text = res.json()["reply_text"]
                    
                    st.markdown("---")
                    st.success("✅ ¡Respuesta Generada!")
                    
                    # 1. VISUALIZACIÓN CÓMODA
                    st.subheader("Respuesta Sugerida:")
                    st.caption("Puedes editar el texto abajo antes de enviar:")
                    st.text_area(
                        label="Respuesta",
                        value=reply_text,
                        height=300,
                        label_visibility="collapsed"
                    )
                    
                    # 2. BOTÓN DE COPIAR
                    with st.expander("📋 Copiar texto con un clic"):
                        st.code(reply_text, language='text')

                else:
                    st.error("Error del servidor.")
            except requests.exceptions.ConnectionError:
                st.error("No se detecta el backend. Asegúrate de que 'app.py' esté corriendo.")

# --- FOOTER ---
st.markdown("---")
st.markdown(f"<div style='text-align: center; color: grey;'>© 2026 {YOUR_NAME} - AI Solutions</div>", unsafe_allow_html=True)