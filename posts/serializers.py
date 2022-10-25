"""
Serialize Post-model into JSON-data
"""
from rest_framework import serializers
from posts.models import Post
from likes.models import Like


class PostSerializer(serializers.ModelSerializer):
    """
    Structures serilialized to JSON-data
    Id is found within owner for React.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        """
        Acceptable image size by px and byte.
        """
        if value.size > 2097152:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        """
        Acceptable access to object.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        """Get like IDs from likes"""
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user,
                post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        """
        Visible model structures in UI-view
        """
        model = Post
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'created_at',
            'updated_at',
            'title',
            'content',
            'image',
            'image_filter',
            'like_id',
            'comments_count',
            'likes_count',
        ]
