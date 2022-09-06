""" Model for following and have followers """
from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Model for Users to follow and have followers
    the two are separate depending on status, User or followed.
    """
    owner = models.ForeignKey(
        User,
        related_name='following',
        on_delete=models.CASCADE)
    followed = models.ForeignKey(
        User,
        related_name='followed',
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        unique_together only allows user to
        follow another user once.
        """
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'
