# OpsVoice Assistant 🚀

Voice‑powered AI observability assistant built with **Google Cloud Vertex AI / Gemini** and **Datadog APM**.  
Built for the **AI Partner Catalyst Hackathon** to showcase end‑to‑end monitoring of an LLM‑powered backend.

---

## 📌 Overview

opsvoice-assistant/
├── venv/                             # Python virtual environment (excluded from repo)
├── main.py                           # Flask app with Datadog + Vertex AI integration
├── README.md                         # Project overview, setup, and submission details
├── requirements.txt                  # Python dependencies
├── Connect-Datadog-with-docker.md    # Optional guide or notes


OpsVoice Assistant is a Flask‑based backend service that:
- Accepts voice command requests (`/process-command`)
- Simulates **speech‑to‑text** (Google STT)
- Runs **LLM analysis** (Vertex AI Gemini)
- Streams **traces, logs, and metrics** to **Datadog APM**
- Provides **dashboards and monitors** for latency, errors, and downstream service health

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
```

2. Install Dependencies

```bash
pip install -r requirements.txt
```

3. Run the Backend

```bash
python main.py
```

4. 🔍 Observability
- Datadog Agent must be running locally (localhost:8126)
- Logs include trace_id and span_id for correlation
- Dashboards track latency, error rate, and model usage
- Monitors can be configured for:
- Latency thresholds
- Error rate > 5%
- Model usage anomalies


5. 📡 API Endpoints
- GET /status → Health check
- GET /model-info → Gemini model list
- POST /process-command → Voice command processing








