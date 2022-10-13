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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        """ Order of view and order for unique chat """
        ordering = ['updated_at']
        unique_together = ['owner', 'contact']

    def __str__(self):
        return f'{self.owner} {self.contact}'


class Message(models.Model):
    """ Model for chat messages """
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Ordering messages """
        ordering = ['-created_at']

    def __str__(self):
        """ Returning content """
        return self.content
