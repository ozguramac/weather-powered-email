from django.db import models

class Location(models.Model):
    city = models.CharField(max_length=255, null=False)
    state = models.CharField(max_length=255, null=False)

class User(models.Model):
    email = models.CharField(max_length=255, unique='true')
    location = models.IntegerField()