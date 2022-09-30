""" App configuration for comments """
from django.apps import AppConfig


class CommentsConfig(AppConfig):
    """ Comment configuration
    for installed app interactions
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comments'
