""" Contacts """
from django.db import models
from django.contrib.auth.models import User


class Contacts(models.Model):
    """ Model for list of active chats """
    owner = models.ForeignKey(
        User,
        related_name='contact1',
        on_delete=models.CASCADE)
    contact = models.ForeignKey(
        User,
        related_name='contact2',
        on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Order of view and order for unique chat """
        ordering = ['-created_at']
        unique_together = ['owner', 'contact']

    def __str__(self):
        return f'{self.owner} {self.contact}'
