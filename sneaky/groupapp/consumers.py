import json
from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.consumer import AsyncConsumer
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.send({"send":
                       'websocket.accept'})
        print("connected")

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(message)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
# class ChatConsumer(AsyncConsumer):
#     async def websocket_connect(self,event):
#         print('i have connected')
#         await self.send({
#             "send":'websocket.accept'
#         })
#
#     async def websocket_disconnect(self, event):
#         pass
#
#     async def websocket_receive(self, event):
#         pass
# class ChatConsumer(WebsocketConsumer):
#
#     def fetch_messages(self, data):
#         messages = Message.last50messages()
#         content = {
#             'command': 'messages',
#             'messages': self.messages_to_json(messages)
#         }
#         self.send_message(content)
#
#     def new_message(self, data):
#         author = data['from']
#         author_user = User.objects.filter(username=author)[0]
#         message = Message.objects.create(
#             author=author_user,
#             content=data['message'])
#         content = {
#             'command': 'new_message',
#             'message': self.message_to_json(message)
#         }
#         return self.send_chat_message(content)
#
#     def messages_to_json(self, messages):
#         result = []
#         for message in messages:
#             result.append(self.message_to_json(message))
#         return result
#
#     def message_to_json(self, message):
#         return {
#             'author': message.author.username,
#             'content': message.content,
#             'timestamp': str(message.timestamp)
#         }
#
#     commands = {
#         'fetch_messages': fetch_messages,
#         'new_message': new_message
#     }
#
#     def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name
#         print("i am working fine upto here")
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )
#         self.accept()
#
#     def disconnect(self, close_code):
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )
#
#     def receive(self, text_data):
#         data = json.loads(text_data)
#         self.commands[data['command']](self, data)
#
#     def send_chat_message(self, message):
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )
#
#     def send_message(self, message):
#         self.send(text_data=json.dumps(message))
#
#     def chat_message(self, event):
#         message = event['message']
#         self.send(text_data=json.dumps(message))