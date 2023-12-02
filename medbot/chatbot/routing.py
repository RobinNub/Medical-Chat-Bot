from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from chatbot import consumer

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('/ws/chat/', consumer.ChatConsumer.as_asgi()),
        ])
    ),
})

# from django.urls import re_path

# from . import consumer

# websocket_urlpatterns = [
#     re_path(r'ws/chat/$', consumer.ChatConsumer.as_asgi()),
# ]
