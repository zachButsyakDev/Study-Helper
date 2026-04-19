from django.db import models
from django.conf import settings

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