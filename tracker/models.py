from django.db import models


class Activity(models.Model):
    category = models.CharField(max_length=200)


class ActivityEvent(models.Model):
    name = models.CharField(max_length=200)
    time = models.DateTimeField()
    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, null=True)
