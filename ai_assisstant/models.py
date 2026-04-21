from django.db import models
from django.conf import settings
from django.utils import timezone

class ChatConversation(models.Model):
    conversation_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name="ai_conversations")
    title = models.CharField(max_length=200, blank=True)
    # stores list of {"role":"user"|"assistant"|"system", "content": "...", "ts": "..."}
    messages = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def append(self, role, content):
        self.messages.append({
            "role": role,
            "content": content,
            "ts": timezone.now().isoformat()
        })
        self.save()

    def __str__(self):
        return self.title or f"Conversation {self.conversation_id}"

class ChatMessage(models.Model):
    ROLE_CHOICES = (('user', 'User'), ('assistant', 'Assistant'), ('system', 'System'))

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="ai_chat_messages",
        null=True,
        blank=True,
    )
    role = models.CharField(max_length=16, choices=ROLE_CHOICES)
    content = models.TextField()
    mode = models.CharField(max_length=32, default='chat')  # e.g. chat, summarize, quiz, rewrite
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        user = self.user.username if self.user else "Anonymous"
        return f"{user} [{self.role}] {self.created_at.isoformat()}"

class AssistantSetting(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="assistant_settings"
    )
    default_mode = models.CharField(max_length=32, default='chat')
    max_tokens = models.PositiveIntegerField(default=600)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} settings"