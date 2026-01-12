# 🎧 AI Support Suite

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Gemini](https://img.shields.io/badge/AI-Google%20Gemini%203.0-orange)

**Suite de herramientas de Inteligencia Artificial diseñada para optimizar y automatizar la comunicación en equipos de Soporte Técnico y Customer Success.**

Este proyecto implementa una arquitectura desacoplada (Backend API + Multiple Frontends) para ofrecer dos soluciones clave: optimización de borradores y generación automática de respuestas.

---

## 🚀 Características Principales

* **🧠 Motor Multimodal:** Integración con **Google Gemini 3.0 Flash Preview** para procesamiento de texto y audio.
* **✍️ Optimizador de Borradores (`demo.py`):** Mejora la redacción, tono y gramática de mensajes escritos por agentes.
* **🤖 Auto-Respuesta Inteligente (`demo2.py`):** Genera respuestas completas a partir del mensaje del cliente.
* **🎙️ Transcripción de Audio:** Convierte notas de voz (WhatsApp/Soporte) a texto automáticamente.
* **🌍 Traducción Instantánea:** Soporte nativo para Español, Inglés, Portugués, Francés y Alemán.
* **📋 Copiado Fácil:** Interfaz optimizada para copiar y pegar respuestas en CRMs (Zendesk, Salesforce, etc.).

---

## 🛠️ Stack Tecnológico

* **Backend:** Python + FastAPI (API RESTful).
* **Frontend:** Streamlit (Interfaces interactivas web).
* **AI Model:** Google Generative AI (Gemini 3 Flash Preview).
* **Librerías Clave:** `uvicorn`, `requests`, `python-dotenv`.

---

## 📂 Estructura del Proyecto

```text
ai-support-suite/
├── app.py           # Backend: API Server (FastAPI)
├── rewrite.py       # Lógica: Conexión con Gemini (Brain)
├── analysis.py      # Lógica: Análisis de texto (NLP)
├── demo.py          # Frontend 1: Optimizador de Borradores
├── demo2.py         # Frontend 2: Generador de Respuestas
├── requirements.txt # Dependencias
├── .env             # Variables de entorno (API Keys)
└── logo.png         # Recursos gráficos
