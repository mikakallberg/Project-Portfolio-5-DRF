""" Messages view """
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import generics
from p5_api.permissions import IsOwnerOrReadOnly
from messages.models import Message
from .serializers import MessageSerializers


@method_decorator(login_required, name='dispatch')
class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    The detail view of a authenticated user that
    is following another user
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Message.objects.all()
    serializer_class = MessageSerializers
