import streamlit as st
import requests
from PIL import Image

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="AI Optimizador", page_icon="✍️", layout="centered")
API_URL = "http://127.0.0.1:8000"
YOUR_NAME = "Gastón Di Campli" # <--- Pon tu nombre

# --- HEADER & LOGO ---
try:
    logo = Image.open("logo.png")
    st.image(logo, use_container_width=True)
except:
    st.title("✍️ AI Optimizador de Borradores")

st.markdown("### Mejora tus borradores antes de enviarlos")

# --- ENTRADA ---
input_text = st.text_area("Pega tu borrador aquí:", height=150, placeholder="Ej: hola cliente perdon por la demora...")

# --- PROCESO ---
if input_text:
    col1, col2 = st.columns(2)
    with col1:
        tone = st.selectbox("Tono:", ["Profesional", "Amable", "Directo"])
    with col2:
        language = st.selectbox("Idioma:", ["Español", "English", "Português"])
        
    if st.button("✨ Optimizar Borrador", type="primary"):
        with st.spinner("Mejorando redacción..."):
            try:
                res = requests.post(f"{API_URL}/rewrite", json={"text": input_text, "tone": tone, "language": language})
                if res.status_code == 200:
                    final_text = res.json()["rewritten_text"]
                    
                    st.markdown("---")
                    st.success("✅ ¡Borrador Optimizado!")
                    
                    # 1. VISUALIZACIÓN CÓMODA (Sin scroll horizontal)
                    st.subheader("Resultado Final:")
                    st.text_area(
                        label="Resultado",
                        value=final_text,
                        height=250,
                        label_visibility="collapsed"
                    )
                    
                    # 2. BOTÓN DE COPIAR (Oculto en un desplegable para no ensuciar)
                    with st.expander("📋 Copiar texto con un clic"):
                        st.code(final_text, language='text')
                        
                else:
                    st.error("Error del servidor.")
            except requests.exceptions.ConnectionError:
                st.error("No se detecta el backend. Asegúrate de que 'app.py' esté corriendo.")

# --- FOOTER ---
st.markdown("---")
st.markdown(f"<div style='text-align: center; color: grey;'>© 2026 {YOUR_NAME} - AI Solutions</div>", unsafe_allow_html=True)