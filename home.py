import streamlit as st
from PIL import Image

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="AI Support Suite",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- ESTILOS ---
st.markdown("""
    <style>
        .main-title {font-size: 3rem; font-weight: bold; color: #1E88E5; text-align: center;}
        .subtitle {font-size: 1.2rem; color: #555; text-align: center; margin-bottom: 30px;}
        .card {padding: 20px; border-radius: 10px; background-color: #f8f9fa; border: 1px solid #ddd; margin-bottom: 20px;}
        .card h3 {color: #1E88E5;}
    </style>
""", unsafe_allow_html=True)

# --- LOGO Y TÍTULO ---
try:
    logo = Image.open("logo.png")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(logo, use_container_width=True)
except:
    pass

st.markdown('<div class="main-title">AI Support Suite</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Herramientas de Inteligencia Artificial para potenciar equipos de Customer Success</div>', unsafe_allow_html=True)

st.markdown("---")

# --- INTRODUCCIÓN ---
st.write("Bienvenido a la suite de demostración. Esta aplicación utiliza **Google Gemini 3.0** para automatizar tareas complejas de comunicación. Selecciona una herramienta en el menú de la izquierda para comenzar.")

# --- TARJETAS DE INFORMACIÓN ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h3>✍️ Optimizador</h3>
        <p>Convierte borradores rápidos o notas de voz en mensajes profesionales.</p>
        <ul>
            <li>Corrige gramática y tono.</li>
            <li>Transcribe audio a texto.</li>
            <li>Traduce a 5 idiomas.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>🤖 Auto-Respuesta</h3>
        <p>Genera respuestas completas desde cero analizando el mensaje del cliente.</p>
        <ul>
            <li>Detecta la intención (queja, duda).</li>
            <li>Estructura respuestas empáticas.</li>
            <li>Ideal para tickets complejos.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- DETALLES TÉCNICOS (Para reclutadores) ---
with st.expander("🛠️ Ver Stack Tecnológico (Info para Devs)"):
    st.markdown("""
    * **Backend:** FastAPI (Python)
    * **Frontend:** Streamlit
    * **LLM Model:** Google Gemini 3.0 Flash Preview
    * **Arquitectura:** REST API desacoplada
    """)

st.markdown("---")
st.markdown("<div style='text-align: center; color: grey;'>Selecciona una herramienta en la barra lateral 👈</div>", unsafe_allow_html=True)