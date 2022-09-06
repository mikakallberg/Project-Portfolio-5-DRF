"""
Profile view instructions
"""
from rest_framework import generics
from p5_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    Listing all User profiles
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View of individual user profile
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

