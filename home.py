import streamlit as st
from PIL import Image

st.set_page_config(page_title="AI Support Suite", page_icon="🚀", layout="centered")

# --- ESTILOS ---
st.markdown("""
    <style>
        .main-title {font-size: 3rem; font-weight: bold; color: #1E88E5; text-align: center;}
        .card {padding: 20px; border-radius: 10px; background-color: #f0f2f6; margin-bottom: 20px;}
    </style>
""", unsafe_allow_html=True)

# --- LOGO ---
try:
    logo = Image.open("logo.png")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2: st.image(logo, use_container_width=True)
except: pass

st.markdown('<div class="main-title">AI Support Suite</div>', unsafe_allow_html=True)
st.write("Herramientas de Inteligencia Artificial para equipos de Customer Success.")
st.info("⚡ Backend optimizado: Ahora corriendo en arquitectura Serverless para máxima velocidad.")

col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="card"><h3>✍️ Optimizador</h3><p>Mejora borradores y transcribe audios.</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="card"><h3>🤖 Auto-Respuesta</h3><p>Genera respuestas completas desde cero.</p></div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("Selecciona una herramienta en el menú de la izquierda 👈")