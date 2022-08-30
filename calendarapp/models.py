from django.db import models
from django.contrib.auth.models import User
import calendar
from calendar import HTMLCalendar


class Calendar(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    time_field = models.TimeField(blank=True)
    date_field = models.DateField(blank=True)
    month_field = models.DateTimeField()
    header = models.TextField(blank=True)
    content = models.TextField(blank=True)
    file = models.FileField(
        max_length=None,
        allow_empty_file=False,
        use_url=UPLOADED_FILES_USE_URL)
    alert = models.DurationField(max_value=None, min_value=None)
