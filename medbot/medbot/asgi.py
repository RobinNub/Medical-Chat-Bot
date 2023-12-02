"""
ASGI config for medbot project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medbot.settings')

# application = get_asgi_application()
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from chatbot import consumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medbot.settings')  # Adjust 'myproject' as needed

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # For handling traditional HTTP requests
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("/ws/chatbot/", consumer.ChatConsumer.as_asgi()),
            # Add more WebSocket paths and consumers if needed
        ])
    ),
})
