from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import ChatConversation  
import json, os, traceback
from openai import OpenAI

MODEL = "gpt-4o-mini"
GITHUB_KEY = "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"

_client = None

def _get_client():
    global _client
    if _client is None:
        api_key = GITHUB_KEY or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY not set in environment")
        _client = OpenAI(api_key=api_key)
    return _client


def chat_view(request):
    return render(request, "ai_assisstance/ai_assistant.html")


# 🔥 cost control
MAX_INPUT_CHARS = 4000
MAX_OUTPUT_TOKENS = 400


# helper: create or fetch conversation
def _get_or_create_conversation(user, conv_id=None, title=None):
    if conv_id:
        try:
            return ChatConversation.objects.get(conversation_id=conv_id, user=user)
        except ChatConversation.DoesNotExist:
            return None
    # create new
    conv = ChatConversation.objects.create(user=user if user.is_authenticated else None, title=title or "")
    return conv

@require_POST
def api_chat(request):
    try:
        data = json.loads(request.body.decode() or "{}")
        user_message = (data.get("message", "") or "")[:MAX_INPUT_CHARS]
        mode = data.get("mode", "chat")

        # optional conversation handling
        conv_id = data.get("conversation_id")
        conv_title = data.get("conversation_title")
        conv = None
        if conv_id or conv_title:
            conv = _get_or_create_conversation(request.user, conv_id, conv_title)
        else:
            # create a new conversation for this chat so messages are persisted
            conv = ChatConversation.objects.create(user=request.user if request.user.is_authenticated else None, title=conv_title or "")

        # build prompts same as before
        system_prompt = (
            "You are Study Helper AI. "
            "Be concise, correct, and helpful. "
            "Avoid long explanations unless asked."
        )
        # mode-specific instructions
        mode_instructions = {
            "chat": "",
            "explain": "When explaining, simplify the text, give short examples, and summarize key points for a learner.",
            "command": "Treat the provided context as an input resource. Perform the requested transformation or action and return the result concisely."
        }
        system_prompt += " " + (mode_instructions.get(mode, "") or "")

        client = _get_client()

        # if conversation exists, include prior messages optionally (cheap: only include last N)
        messages_for_api = [{"role":"system","content":system_prompt}]
        if conv and conv.messages:
            # include last 6 messages to keep cost low
            tail = conv.messages[-6:]
            for m in tail:
                messages_for_api.append({"role": m["role"], "content": m["content"]})
        messages_for_api.append({"role":"user","content": user_message})

        # call the OpenAI client (SDK shape may vary; be defensive)
        resp = client.chat.completions.create(
            model=MODEL,
            messages=messages_for_api,
            max_tokens=MAX_OUTPUT_TOKENS,
            temperature=0.4
        )

        # extract reply safely from different possible response shapes
        reply = None
        try:
            # common shape: resp.choices[0].message.content
            if hasattr(resp, 'choices') and len(resp.choices) > 0:
                choice0 = resp.choices[0]
                # object-like
                if hasattr(choice0, 'message') and hasattr(choice0.message, 'content'):
                    reply = choice0.message.content
                # dict-like
                elif isinstance(choice0, dict) and choice0.get('message', {}).get('content'):
                    reply = choice0['message']['content']
                # older shape: text
                elif isinstance(choice0, dict) and choice0.get('text'):
                    reply = choice0.get('text')
            # fallback: try top-level fields
            if reply is None and isinstance(resp, dict):
                # maybe a streaming/other response
                if resp.get('choices') and len(resp['choices']) > 0:
                    c = resp['choices'][0]
                    if isinstance(c, dict) and c.get('message', {}).get('content'):
                        reply = c['message']['content']
                    elif isinstance(c, dict) and c.get('text'):
                        reply = c.get('text')
        except Exception:
            # non-fatal parse error here; we'll report below
            reply = None

        if not reply:
            raise RuntimeError(f"Unexpected AI response shape: {type(resp)}")

        reply = reply.strip()

        # persist messages into conversation if exists (or create new)
        if conv:
            conv.append("user", user_message)
            conv.append("assistant", reply)

        return JsonResponse({
            "ok": True,
            "reply": reply,
            "conversation_id": conv.conversation_id if conv else None
        })

    except Exception as e:
        # print full traceback for local debugging
        print("AI ERROR:", str(e))
        traceback.print_exc()
        return JsonResponse({"ok": False, "error": "AI request failed"}, status=500)


# new endpoints
@login_required
def conversations_list(request):
    qs = ChatConversation.objects.filter(user=request.user).order_by("-updated_at")
    data = [{"id": c.conversation_id, "title": c.title or f"Conversation {c.conversation_id}", "updated_at": c.updated_at.isoformat()} for c in qs]
    return JsonResponse(data, safe=False)

@login_required
def conversation_detail(request, pk):
    conv = get_object_or_404(ChatConversation, conversation_id=pk, user=request.user)
    return JsonResponse({"id": conv.conversation_id, "title": conv.title, "messages": conv.messages, "created_at": conv.created_at.isoformat(), "updated_at": conv.updated_at.isoformat()})
# ...existing code...