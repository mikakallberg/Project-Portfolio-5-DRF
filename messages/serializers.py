"""Serialize Messages model into JSON-data"""
from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from messages.models import Message


class MessageSerializers(serializers.ModelSerializer):
    """ Serializing Message model into JSON-data """
    chat_owner = serializers.ReadOnlyField(source='chat_owner.username')
    chat_contact = serializers.ReadOnlyField(source='chat_contact.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='chat_owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='chat_owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def validate_image(self, value):
        """
        Acceptable image size by px and byte.
        """
        if value.size > 2 * 1024 * 1024:
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
        """ Get owner for message """
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        """ Time of message creation """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """ Time of message update """
        return naturaltime(obj.created_at)

    class Meta:
        """ Which assets are shown with message """
        model = Message
        fields = [
            'id',
            'chat_contact',
            'chat_owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'created_at',
            'updated_at',
            'content'
        ]
