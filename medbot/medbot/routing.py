from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
# from django.urls import path
# from chatbot import consumer

# application = ProtocolTypeRouter({
#     'websocket': AuthMiddlewareStack(
#         URLRouter([
#             path('ws/chatbot/', consumer.ChatConsumer.as_asgi()),
#         ])
#     ),
# })

# projectname/routing.py
# from channels.routing import ProtocolTypeRouter, URLRouter
# from chatbot import routing  # Import your app's routing configuration

# application = ProtocolTypeRouter({
#     "websocket": URLRouter(routing.websocket_urlpatterns),
# })

from django.urls import path
from chatbot import consumer

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/chatbot/', consumer.ChatConsumer.as_asgi()),
        ])
    ),
})
