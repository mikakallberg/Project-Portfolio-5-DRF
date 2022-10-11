"""Serialize Contacts model into JSON-data"""
from django.db import IntegrityError
from rest_framework import serializers
from .models import Contacts


class ContactsSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contacts model
    Create method handles the unique constraint on 'owner' and 'contact'
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    contact_name = serializers.ReadOnlyField(source='contact.username')

    class Meta:
        """Specifies which fields to serialize to JSON-data"""
        model = Contacts
        fields = [
            'id', 'owner', 'created_at', 'contact', 'contact_name'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})
