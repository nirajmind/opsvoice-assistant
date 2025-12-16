# Inspiration

Modern IT operations are flooded with logs, metrics, and alerts — but voice remains untapped. We wanted to build a voice-first assistant that could interpret system health, analyze logs, and respond in natural language using Gemini AI. The goal: empower engineers to debug and monitor infrastructure hands-free.

# What it does

OpsVoice Assistant lets users speak commands like "Check system logs for errors" or "Summarize CPU usage" and get instant, AI-powered responses. It integrates with Vertex AI Gemini for log analysis and uses Datadog for observability, tracing, and metric correlation. The assistant supports endpoints for health checks, model introspection, and voice command processing.

# How we built it

We used Python and Flask to build the backend, instrumented with Datadog APM and logging. Gemini 2.5 Pro handles natural language analysis. We wrapped key functions with custom spans and tags to enable trace-level observability. Logs include trace_id and span_id for correlation. We also scaffolded a dashboard and monitor setup for latency, error rate, and model usage.

# Challenges we ran into

Datadog’s trace metrics weren’t auto-generated, requiring manual span validation and statsd-based metric emission.

Ensuring trace-log correlation across Windows environments and local agent setups.

Handling Gemini’s multi-part responses and error scenarios gracefully.

# Accomplishments that we're proud of

Full trace lifecycle visibility with custom spans and tags.

Real-time voice command processing with Gemini-powered analysis.

Reproducible dashboard and monitor setup for hackathon judging.

# What we learned

How to debug Datadog instrumentation edge cases and validate trace ingestion.

How to structure logs and spans for observability-driven development.

How to integrate Gemini with real backend workflows.

# What's next for opsvoice-assistant

We plan to add:

Alerting via voice ("Notify me if error rate exceeds 5%")

Log summarization across services

Multi-user voice session support

Integration with Slack and PagerDuty for incident response