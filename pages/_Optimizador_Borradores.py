import streamlit as st
import requests

# --- CONFIGURACIÓN DE CONEXIÓN ---
# Busca la variable BACKEND_URL en los secretos de Streamlit. 
# Si no existe, usa localhost (para cuando pruebas en tu PC).
API_URL = st.secrets.get("BACKEND_URL", "http://127.0.0.1:8000")

st.set_page_config(page_title="Optimizador", page_icon="✍️")
st.title("✍️ Optimizador de Borradores")

input_text = st.text_area("Escribe tu borrador:", height=150)

col1, col2 = st.columns(2)
with col1: tone = st.selectbox("Tono:", ["Profesional", "Amable", "Directo"])
with col2: language = st.selectbox("Idioma:", ["Español", "English", "Português"])

if st.button("✨ Optimizar", type="primary"):
    if not input_text:
        st.warning("Escribe algo primero.")
    else:
        with st.spinner("Conectando con el cerebro AI..."):
            try:
                payload = {"text": input_text, "tone": tone, "language": language}
                response = requests.post(f"{API_URL}/rewrite", json=payload)
                
                if response.status_code == 200:
                    data = response.json()
                    st.success("¡Hecho!")
                    st.text_area("Resultado:", value=data["rewritten_text"], height=200)
                else:
                    st.error(f"Error del servidor: {response.status_code}")
            except Exception as e:
                st.error(f"No se pudo conectar al backend en: {API_URL}")
                st.caption("Verifica que el Backend en Vercel esté funcionando.")