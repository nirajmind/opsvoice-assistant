from vertexai.preview.generative_models import GenerativeModel
import vertexai

vertexai.init(project="opsvoice-assistant-v2", location="us-central1")

model_names = [
    "gemini-1.5-pro-001",
    "gemini-1.5-flash-001",
    "gemini-2.0-flash-001",
    "gemini-2.5-pro",
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-3-pro-preview"
]

for name in model_names:
    try:
        print(f"Trying model: {name}")
        model = GenerativeModel(name)
        chat = model.start_chat()
        response = chat.send_message("Hello Gemini!")
        print(f"✅ Success with {name}: {response.text[:60]}...\n")
    except Exception as e:
        print(f"❌ Failed with {name}: {e}\n")