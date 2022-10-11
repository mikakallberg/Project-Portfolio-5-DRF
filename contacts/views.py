""" Contacts view """
from rest_framework import generics, permissions
from p5_api.permissions import IsOwnerOrReadOnly
from .models import Contacts
from .serializers import ContactsSerializer


class ContactList(generics.ListCreateAPIView):
    """
    List all contacts
    contacts = authenticated users in active chats with User
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ContactDetail(generics.RetrieveDestroyAPIView):
    """
    The detail view of a authenticated user that
    is following another user
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
