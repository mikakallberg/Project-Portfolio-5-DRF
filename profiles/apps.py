""" App configuration for profiles """
from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configuring communication between installed apps
    and profiles
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
