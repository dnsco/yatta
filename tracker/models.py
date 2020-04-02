import datetime

from django.db import models
from django.utils import timezone


class Activity(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category


class ActivityEvent(models.Model):
    name = models.CharField(max_length=200)
    time = models.DateTimeField()
    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def was_today(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)
