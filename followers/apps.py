""" App configuration for followers """
from django.apps import AppConfig


class FollowersConfig(AppConfig):
    """ Configuring the app for followers
    for installed app interactions
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'followers'
