""" Serialize comment models into JSON """
from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for Comment model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """ Get owner for comment """
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        """ Time of comment creation """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """ Time of comment update """
        return naturaltime(obj.created_at)

    class Meta:
        """ Which assets are shown with comment """
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'post', 'created_at', 'updated_at', 'content'
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serialize comment details
    """
    post = serializers.ReadOnlyField(source='post.id')
