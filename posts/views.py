"""
Dictate the view instructions for UI
"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer


class PostList(APIView):
    """
    List all profiles
    No Create view (post method), as profile creation 
    handled by django signals
    """
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(
            posts,
            many=True,
            context={'request': request})
        return Response(serializer.data)
