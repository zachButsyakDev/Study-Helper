from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import os, json
from openai import OpenAI

ENDPOINT = "https://models.github.ai/inference"
MODEL = "openai/gpt-5-mini"
GITHUB_TOKEN="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"

_client = None
def _get_client():
    global _client
    if _client is None:
        token = GITHUB_TOKEN or os.getenv("GITHUB_TOKEN")
        if not token:
            raise RuntimeError("GITHUB_TOKEN not set in environment")
        _client = OpenAI(base_url=ENDPOINT, api_key=token)
    return _client

def chat_view(request):
    return render(request, "chat.html")

@require_POST
def api_chat(request):
    try:
        data = json.loads(request.body.decode() or "{}")
        user_message = data.get("message", "")
        mode = data.get("mode", "chat")  # "chat", "summarize", "rewrite", etc.

        system_prompt = "You are Study Helper, a concise helpful assistant for taking notes, summarizing, and quiz prep."
        if mode == "summarize":
            system_prompt += " Summarize the user's notes into concise bullet points."
        elif mode == "quiz":
            system_prompt += " Create 5 short quiz questions from the notes."

        client = _get_client()
        resp = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
            max_completion_tokens=600,
        )

        reply = resp.choices[0].message.content
        return JsonResponse({"ok": True, "reply": reply})
    except Exception as e:
        return JsonResponse({"ok": False, "error": str(e)}, status=500)