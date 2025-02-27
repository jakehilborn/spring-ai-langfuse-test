#!/usr/bin/env python3

import openai
from traceloop.sdk import Traceloop
import os

Traceloop.init(
    app_name="python-demo",
    api_endpoint=os.environ.get("OTEL_EXPORTER_OTLP_ENDPOINT"),
    headers={
        "Authorization": os.environ.get("OTEL_EXPORTER_OTLP_HEADERS").replace("Authorization=", ""),
    }
)

openai.api_key = os.environ.get("SPRING_AI_OPENAI_APIKEY")

response = openai.chat.completions.create(
    max_tokens=5,
    model="gpt-3.5-turbo", # Or any other model you prefer
    messages=[
        {"role": "user", "content": "Reply with the word 'python'"}
    ]
)

print("OpenAI API Response:")
print(response.choices[0].message.content)
print("\nScript execution complete.")
print("Traceloop should have automatically traced the OpenAI API call and sent OpenTelemetry metrics to http://localhost:3000/api/public/otel")
