import streamlit as st
import requests

API_URL = st.secrets.get("BACKEND_URL", "http://127.0.0.1:8000")

st.set_page_config(page_title="Auto-Respuesta", page_icon="🤖")
st.title("🤖 Generador de Respuestas")

client_msg = st.text_area("Mensaje del Cliente:", height=150)

col1, col2 = st.columns(2)
with col1: tone = st.selectbox("Tono:", ["Empático", "Técnico", "Venta"])
with col2: language = st.selectbox("Idioma:", ["Español", "English", "Português"])

if st.button("🚀 Generar Respuesta", type="primary"):
    if not client_msg:
        st.warning("Pega el mensaje del cliente primero.")
    else:
        with st.spinner("Analizando caso..."):
            try:
                payload = {"text": client_msg, "tone": tone, "language": language}
                response = requests.post(f"{API_URL}/reply", json=payload)
                
                if response.status_code == 200:
                    data = response.json()
                    st.success("¡Respuesta Generada!")
                    st.text_area("Sugerencia:", value=data["reply_text"], height=300)
                else:
                    st.error(f"Error: {response.status_code}")
            except:
                st.error("Error de conexión con el Backend.")