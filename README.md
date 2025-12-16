# OpsVoice Assistant 🚀

An AI-powered backend application built for the **AI Partner Catalyst Hackathon**.  
This project integrates **Google Cloud Vertex AI / Gemini** with **Datadog APM** to deliver end-to-end observability for an LLM-powered application.

---

## 📌 Overview

opsvoice-assistant/
├── venv/                             # Python virtual environment (excluded from repo)
├── main.py                           # Your Flask app with Datadog + Vertex AI integration
├── README.md                         # Project overview, setup, and submission details
├── requirements.txt                  # Python dependencies (currently empty — we’ll fix that)
├── Connect-Datadog-with-docker.md    # Optional guide or notes (can be useful for judges)

OpsVoice Assistant is a Flask-based backend service that:
- Accepts voice command requests (`/process-command`)
- Simulates **speech-to-text** (Google STT)
- Simulates **LLM analysis** (Vertex AI Gemini)
- Streams **traces, logs, and metrics** to **Datadog APM**
- Provides **dashboards and monitors** for latency, errors, and downstream service health

This project demonstrates how to combine **Google Cloud AI** with **Datadog observability** to build a reliable, production-ready AI application.

---

## 🛠 Tech Stack

- **Python 3.11**
- **Flask** (REST API)
- **Google Cloud Vertex AI / Gemini**
- **Datadog APM (`ddtrace`)**
- **Datadog Agent** (local, port `8126`)
- **DogStatsD** (custom metrics)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/opsvoice-assistant.git
cd opsvoice-assistant