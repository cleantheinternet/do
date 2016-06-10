from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Campaign(models.Model):
    user = models.ForeignKey(User, default=1)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    links = models.CharField(max_length=1000)
    suggestion = models.CharField(max_length=1000)
    views = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    date = models.DateTimeField(default=datetime.now, blank=True)
    amount = models.CharField(max_length=10, default=0)
    progress = models.CharField(max_length=10, default=0)

    def __str__(self):
        return self.name


class PublisherCampaign(models.Model):
    user = models.ForeignKey(User, default=1)
    name = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now)
    amount = models.CharField(max_length=10, default=0)
    progress = models.CharField(max_length=10, default=0)

    def __str__(self):
        return self.name


class Finance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
    balance = models.CharField(max_length=5, default=0)

    def __str__(self):
        return
