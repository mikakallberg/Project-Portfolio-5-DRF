"""Serialize Contacts model into JSON-data"""
from rest_framework import serializers
from .models import Contacts


class ContactsSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contacts model
    Create method handles the unique constraint on 'owner' and 'contact'
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    contact_name = serializers.ReadOnlyField(source='contact.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        """Specifies which fields to serialize to JSON-data"""
        model = Contacts
        fields = [
            'id',
            'owner',
            'profile_id',
            'profile_image',
            'created_at',
            'updated_at',
            'contact',
            'contact_name',
            'is_owner',
        ]
