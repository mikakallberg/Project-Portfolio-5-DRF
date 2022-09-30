""" App configuration for likes """
from django.apps import AppConfig


class LikesConfig(AppConfig):
    """ Configuring likes in app
    for installed app interactions
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'likes'
