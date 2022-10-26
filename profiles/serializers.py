"""
Serialize profile model into JSON data
"""
from rest_framework import serializers
from followers.models import Follower
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer model for profile model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """Get profiles"""
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        """Get following IDs from followers"""
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user,
                followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        """Fields included in the profile JSON data"""
        model = Profile
        fields = [
            'id',
            'owner',
            'created_at',
            'updated_at',
            'name',
            'content',
            'image',
            'is_owner',
            'following_id',
            'posts_count',
            'followers_count',
            'following_count',
        ]
