"""Serialize Contacts model into JSON-data"""
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db import IntegrityError
from rest_framework import serializers
from .models import Contacts, Message


class ContactsSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contacts model
    Create method handles the unique constraint on 'owner' and 'contact'
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    contact_name = serializers.ReadOnlyField(source='contact.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    class Meta:
        """Specifies which fields to serialize to JSON-data"""
        model = Contacts
        fields = [
            'id',
            'owner',
            'profile_id',
            'profile_image',
            'created_at',
            'contact',
            'contact_name',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})


class MessageSerializers(serializers.ModelSerializer):
    """ Serializing Message model into JSON-data"""
    chat_owner = serializers.ReadOnlyField(source='chat_owner.username')
    chat_contact = serializers.ReadOnlyField(source='chat_contact.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='chat_owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='chat_owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

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
