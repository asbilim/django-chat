from django.urls import path
from .consumer import ChatConsumer


websocket_urlpatterns = [
    path("chat/<str:room>/",ChatConsumer.as_asgi(),name="chat-backend")
]