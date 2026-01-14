# 🎧 AI Support Suite

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Gemini](https://img.shields.io/badge/AI-Google%20Gemini-orange)

**Suite de herramientas de Inteligencia Artificial diseñada para optimizar y automatizar la comunicación en equipos de Soporte Técnico y Customer Success.**

Este proyecto implementa una arquitectura moderna para ofrecer soluciones clave: optimización de borradores, generación automática de respuestas y análisis inteligente.

---

## 🚀 Características Principales

* **🧠 Motor Multimodal:** Integración con **Google Gemini** para procesamiento avanzado de texto.
* **✍️ Optimizador de Borradores:** Mejora la redacción, tono y gramática de mensajes escritos por agentes.
* **🤖 Generador de Respuestas:** Crea respuestas completas y empáticas a partir del mensaje del cliente.
* **🎙️ Transcripción de Audio:** (Próximamente) Convierte notas de voz a texto automáticamente.
* **🌍 Traducción & Adaptación:** Soporte nativo multilingüe y adaptación de tono (Formal, Empático, Directo).
* **☁️ Cloud Ready:** Optimizado para despliegue en Streamlit Community Cloud usando gestión de secretos.

---

## 🛠️ Stack Tecnológico

* **Backend:** Python + FastAPI (API RESTful para lógica de negocio).
* **Frontend:** Streamlit (Interfaz web interactiva multipágina).
* **AI Model:** Google Generative AI (Gemini Flash).
* **Gestión de Entorno:** `st.secrets` (Producción) / `.env` (Desarrollo local).
* **Librerías Clave:** `uvicorn`, `requests`, `python-dotenv`, `spacy`.

---

## 📂 Estructura del Proyecto

```text
herramientasai/
├── app.py                   # Backend: API Server (FastAPI) - Lógica central
├── home.py                  # Frontend: Página de Inicio (Streamlit Entrypoint)
├── pages/                   # Frontend: Páginas de la aplicación
│   ├── _Optimizador_Borradores.py
│   └── _Generador_de_Respuestas.py
├── rewrite.py               # Módulo: Conexión con Gemini (Brain)
├── analysis.py              # Módulo: Análisis de texto (NLP/Spacy)
├── requirements.txt         # Dependencias del proyecto
├── .gitignore               # Archivos ignorados por seguridad
└── .env                     # Variables locales (NO SUBIR A GITHUB)
