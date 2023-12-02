from channels.generic.websocket import AsyncWebsocketConsumer
import json
# from chat_bot import medical_chatbot

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
    async def disconnect(self, code):
        pass
    async def send(self, text_data=None, bytes_data=None, close=False):
        return await super().send(text_data, bytes_data, close)   
    async def receive(self, text_data):
        text_data_json=json.loads(text_data)
        message=text_data_json['message']
        # response=medical_chatbot.chatbot_reply(message)

        await self.send(text_data=json.dumps({
            'message': message
        }))
 