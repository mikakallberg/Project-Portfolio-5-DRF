""" App configuration for posts """
from django.apps import AppConfig


class PostConfig(AppConfig):
    """
    Installed apps communication with
    post
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
