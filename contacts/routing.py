""" Routing the Url for websocket """
from django.urls import path
from contacts import consumers

websocket_urlpatterns = [
    path('ws/<str:contact_name>/', consumers.ChatConsumer.as_asgi()),
]
