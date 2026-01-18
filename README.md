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


# ☁️ Guía de Despliegue del Backend (Render)

Esta guía explica cómo publicar la API (FastAPI) en **Render** para que sea accesible desde la aplicación de Streamlit.

## 📋 Prerrequisitos
1. Tener el código subido a **GitHub** (sin el archivo `.env`).
2. Tener una cuenta en [Render.com](https://render.com).

## 🚀 Paso 1: Crear el Web Service

1. Entra a tu Dashboard de Render y haz clic en **"New +"**.
2. Selecciona **"Web Service"**.
3. Conecta tu repositorio de GitHub (`herramientasai`).
4. Configura los siguientes campos:

| Campo | Valor Recomendado |
| :--- | :--- |
| **Name** | `herramientasai-api` (o el que gustes) |
| **Region** | Oregon (US West) o la más cercana |
| **Branch** | `main` |
| **Runtime** | **Python 3** |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn app:app --host 0.0.0.0 --port $PORT` |

> **⚠️ Nota sobre el Start Command:** Si tu archivo principal no se llama `app.py`, cambia la primera parte. Ejemplo: si es `main.py`, usa `uvicorn main:app ...`.

## 🔐 Paso 2: Configurar Variables de Entorno (Environment)

**¡IMPORTANTE!** Aquí es donde pegas tus claves de seguridad. Render actúa como tu archivo `.env` seguro en la nube.

1. En la página del servicio en Render, baja hasta la sección **"Environment Variables"**.
2. Haz clic en **"Add Environment Variable"**.
3. Agrega tus claves (las mismas que tenías en tu `.env` local):

   * **Key:** `OPENAI_API_KEY` (o `GOOGLE_API_KEY` según tu código)
   * **Value:** `tu-clave-que-empieza-con-sk...`

4. Haz clic en **"Save Changes"**.

## ✅ Paso 3: Verificar el Despliegue

1. Render empezará a construir (Build) tu aplicación. Esto tarda unos minutos.
2. Si todo sale bien, verás un mensaje verde que dice **"Live"**.
3. Copia la URL que te da Render (ej: `https://herramientasai.onrender.com`).
4. Abre esa URL en tu navegador y agrega `/docs` al final (ej: `https://herramientasai.onrender.com/docs`).
   * Si ves la pantalla de Swagger UI, ¡tu Backend está funcionando!

## 🔗 Paso 4: Conectar con Streamlit

Ahora que tienes la URL de Render, debes "decirle" a tu Frontend de Streamlit dónde buscar.

1. Ve a tu App en **Streamlit Community Cloud**.
2. Entra en **Settings** -> **Secrets**.
3. Actualiza la variable `mi_api_render` con la URL real que acabas de copiar:

```toml
# En Streamlit Secrets:
mi_api_render = "[https://herramientasai.onrender.com](https://herramientasai.onrender.com)"

