# ...existing code...
from django.urls import path
from . import views

app_name = "assistant"

urlpatterns = [
    path("", views.chat_view, name="chat"),
    path("api/chat/", views.api_chat, name="api_chat"),

    # conversation endpoints
    path("api/conversations/", views.conversations_list, name="conversations_list"),
    path("api/conversations/<int:pk>/", views.conversation_detail, name="conversation_detail"),
]