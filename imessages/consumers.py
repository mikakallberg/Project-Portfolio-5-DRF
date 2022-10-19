""" Websocket communication for contacts """
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from contacts.models import Contacts
from imessages.models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    """ Connecting """
    async def connect(self):
        self.contact_name = self.scope['url_route']['kwargs']['contact_name']
        self.contact_group_name = 'chat_%s' % self.contact_name

        await self.channel_layer.group_add(
            self.contact_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.contact_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        contact = data['contact']

        await self.save_message(username, contact, message)

        await self.channel_layer.group_send(
            self.contact_group_name,
            {
                'type': 'chat_message',
                'message': 'message',
                'username': 'username',
                'contact': 'contact',
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        contact = event['contact']

        await self.send(text_data=json.dumps({
            'message': 'message',
            'username': 'username',
            'contact': 'contact',
        }))

# Enable storing in database
    @sync_to_async
    def save_message(self, username, contact, message):
        user = User.objects.get(username=username)
        contact = Contacts.objects.get(slug=contact)

        Message.objects.create(user=user, contact=contact, content=message)