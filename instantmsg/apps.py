""" App configuration for Instant messaging """
from django.apps import AppConfig


class InstantmsgConfig(AppConfig):
    """ Configuring instant messageing in app
    for installed app interactions
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'instantmsg'
