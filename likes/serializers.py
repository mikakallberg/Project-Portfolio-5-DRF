""" Serialize Like from models """
from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serialize Like model into JSON-data
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """ Instruct fields from model to serialize """
        model = Like
        fields = [
            'id',
            'owner',
            'post',
            'created_at'
            ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
