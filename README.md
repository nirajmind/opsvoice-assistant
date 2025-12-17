# OpsVoice Assistant 🚀

**Voice‑powered AI observability assistant built with Google Cloud Vertex AI & Datadog.**

> 🏆 **Submission for the Google Cloud x Datadog Hackathon (AI Partner Catalyst)**

OpsVoice Assistant is a backend service designed to demonstrate **end‑to‑end observability** for AI pipelines. It simulates a voice-command workflow where specific observability challenges (like long LLM inference times) are tracked, visualized, and analyzed using Datadog APM.

---

## 🔗 Live Demo & Resources

- **🚀 Live API Health Check:** [https://opsvoice-service-359923875882.us-central1.run.app/status](https://opsvoice-service-359923875882.us-central1.run.app/status)
- **📹 Demo Video:** [https://youtu.be/keq4gTuqZ3Y]
- **📊 Datadog Dashboard:** ["See Demo Video"]

---

## 📌 Features

* **Real-time AI Tracing:** End-to-end distributed traces separating `Google Speech-to-Text` latency from `Vertex AI (Gemini)` inference time.
* **Granular Visibility:** Custom Datadog Spans identify exactly which part of the AI pipeline is the bottleneck.
* **Production Ready:** Dockerized and deployed on **Google Cloud Run** (Serverless).
* **Custom Metrics:** Tracks "AI Token Usage" and "Request Latency" via DogStatsD.

---

## 🛠 Tech Stack

* **Language:** Python 3.11
* **Framework:** Flask (Gunicorn for Production)
* **AI Services:** Google Vertex AI (Gemini Pro), Google Cloud Speech-to-Text
* **Observability:** Datadog APM (`ddtrace`), DogStatsD
* **Deployment:** Google Cloud Run, Docker

---

## 📂 Project Structure

```text
opsvoice-assistant/
├── main.py              # Flask app with Datadog + Vertex AI integration
├── Dockerfile           # Production-ready Docker configuration
├── requirements.txt     # Python dependencies (includes ddtrace, google-cloud-aiplatform)
├── README.md            # Project documentation
└── Connect-Datadog...   # Setup notes
```

## ---

**🚀 Getting Started**

### **Option 1: Run with Docker (Recommended)**

You can build and run the container locally to simulate the production environment.

1. **Build the Image:**  
   Bash  
   docker build -t opsvoice-local .

2. **Run Container:**  
   Bash  
   docker run -p 8080:8080 -e DD_API_KEY=your_datadog_api_key -e GOOGLE_CLOUD_PROJECT=your_project_id opsvoice-local

### **Option 2: Run Locally (Python)**

1. **Install Dependencies:**  
   Bash  
   pip install -r requirements.txt

2. **Run the App:**  
   Bash  
   ddtrace-run python main.py

## ---

**📡 API Endpoints**

| Method | Endpoint | Description |
| :---- | :---- | :---- |
| **GET** | /status | **Health Check.** Returns JSON status to verify service is up. |
| **POST** | /process-command | **Core Logic.** Simulates voice input, transcribes audio (STT), and queries Gemini LLM. |
| **GET** | /model-info | Lists available Google Vertex AI models. |

## ---

**🔍 Observability Details**

This project uses **Datadog APM** to solve the "Black Box" problem in AI apps.

1. **The Trace:** We capture the full request lifecycle.  
2. **The Span:** We create child spans for ai.speech_to_text and vertex_ai.generate.  
3. **The Insight:** Dashboard clearly shows if latency is caused by audio processing (CPU bound) or LLM generation (Network/Model bound).

---

*Built with ❤️ by Niraj for the Devpost Hackathon.*