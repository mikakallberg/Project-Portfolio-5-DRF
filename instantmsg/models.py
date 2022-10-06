""" Instant Messaging """
from django.db import models
from django.contrib.auth.models import User
from profiles.models import profile


class InstantMessage(models.Model):
    """ Models for Instant Messaging"""
    owner = models.ForeignKey(User, on_delete=modesl.CASCADE)
    message = models.ForeignKey(to?, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    textmsg = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_gbfrps', blank=True
    )
    image_filter_choices = [
        ('_1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II')
    ]
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        """ Order of the instant messages"""
        ordering = ['-created_at']

    def __str__(self):
        """ returned content"""
        return self.content
