from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, related_name='owned_rooms', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='rooms')

    def __str__(self):
        return self.name
