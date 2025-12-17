#main.py 

import os
import vertexai
vertexai.init(project="opsvoice-assistant-v2", location="us-central1")
# --- Configuration ---
os.environ["DD_TRACE_DEBUG"] = "True"
os.environ["DD_AGENT_HOST"] = "localhost"
os.environ["DD_TRACE_AGENT_PORT"] = "8126"

print("--- Configuring Datadog to use Local Agent ---", flush=True)

from ddtrace import tracer, config, patch_all, patch

patch(logging=True)


config.service = "opsvoice-backend"
config.env = "hackathon-dev"
config.version = "local-agent-mode"
patch_all()

import logging
from flask import Flask, request, jsonify
app = Flask(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] trace_id=%(dd.trace_id)s span_id=%(dd.span_id)s %(message)s'
)

logger = logging.getLogger(__name__)

@tracer.wrap(name="ai.speech_to_text", service="google-stt")
def mock_speech_to_text(audio_data):
    logger.info("Simulating STT processing...")
    span = tracer.current_span()
    if span:
        span.set_tag("debug.trace_id", span.trace_id)
        span.set_tag("debug.span_id", span.span_id)

    import time; time.sleep(0.1)
    return "Check system logs for errors."

@tracer.wrap(name="ai.analyze_logs", service="vertex-ai-gemini")
def mock_gemini_analysis(query_text):
    logger.info(f"Calling Gemini for query: {query_text} to analyze")
    span = tracer.current_span()
    if span:
        span.set_tag("debug.trace_id", span.trace_id)
        span.set_tag("debug.span_id", span.span_id)

    try:
        result = ask_gemini(query_text)
        logger.info(f"Gemini response: {result}")
        return result
    except Exception as e:
        logger.error(f"Gemini error: {e}")
        return "Gemini failed to respond."

    
from vertexai.preview.generative_models import GenerativeModel
from vertexai.preview.generative_models import ChatSession

def ask_gemini(prompt_text: str) -> str:
    logger.info(f"Asking Gemini analysis for query - {prompt_text}.")
    model = GenerativeModel("gemini-2.5-pro")
    chat = model.start_chat()
    response = chat.send_message(prompt_text)
    logger.info(f"Gemini replied with - {response.text}")
    return response.text    

@app.route('/status', methods=['GET'])
def health_check():
    span = tracer.current_span()
    if span:
        span.set_tag("debug.trace_id", span.trace_id)
        span.set_tag("debug.span_id", span.span_id)

    return jsonify({"status": "healthy", "service": "opsvoice-backend"})
    
@app.route('/model-info', methods=['GET'])
def list_gemini_models():
    with tracer.trace("ai.model_info", service="vertex-ai-gemini") as span:
        span = tracer.current_span()
        trace_id = span.trace_id if span else "N/A"
        span_id = span.span_id if span else "N/A"
        logger.info(f"Listing Gemini models — trace_id={trace_id}, span_id={span_id}")

        model_names = [
            "gemini-2.0-flash-001",
            "gemini-2.5-pro",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3-pro-preview"
        ]

        results = {}
        for name in model_names:
            try:
                logger.info(f"Trying model: {name}")
                model = GenerativeModel(name)
                chat = model.start_chat()
                response = chat.send_message("Hello Gemini!")

                # Handle multi-part responses
                text = None
                try:
                    text = response.text
                except Exception:
                    if hasattr(response, "candidates") and response.candidates:
                        parts = []
                        for c in response.candidates:
                            if hasattr(c, "content") and hasattr(c.content, "parts"):
                                for p in c.content.parts:
                                    if hasattr(p, "text"):
                                        parts.append(p.text)
                        text = "\n".join(parts) if parts else "No text available"

                results[name] = {
                    "status": "success",
                    "sample": text[:200] if text else "No text"
                }

                # ✅ Add Datadog tags
                if span:
                    span.set_tag("model_name", name)
                    span.set_tag("status", "success")
                    span.set_tag("sample_length", len(text) if text else 0)

            except Exception as e:
                logger.error(f"Model {name} failed: {e}")
                results[name] = {"status": "error", "message": str(e)}

                # ✅ Add Datadog tags for errors
                if span:
                    span.set_tag("model_name", name)
                    span.set_tag("status", "error")
                    span.set_tag("error.message", str(e))

        return jsonify({
            "trace_id": trace_id,
            "span_id": span_id,
            "available_models": results
        })

@app.route('/process-command', methods=['POST'])
def process_voice_command():
    span = tracer.current_span()
    if span:
        trace_id = span.trace_id
        span_id = span.span_id
        span.set_tag("debug.trace_id", span.trace_id)
        span.set_tag("debug.span_id", span.span_id)
        logger.info(f"Trace ID: {trace_id}, Span ID: {span_id}")
    else:
        logger.warning("No active span found")

    transcribed_text = mock_speech_to_text(None)
    analysis_result = mock_gemini_analysis(transcribed_text)
    return jsonify({
        "input_text": transcribed_text,
        "analysis": analysis_result,
        "trace_id": trace_id if span else None,
        "span_id": span_id if span else None,
        "status": "success"
    })



if __name__ == '__main__':
    print("🤖 OpsVoice Backend Starting (Local Agent Mode)...", flush=True)
    print(app.url_map)
    app.run(host='0.0.0.0', port=8080)