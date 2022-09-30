""" For User access using JWT authentication """
from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer


class CurrentUserSerializer(UserDetailsSerializer):
    """ Cookie-token access"""

    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        """ The information cookies store to give User access"""
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id',
            'profile_image',
            )
