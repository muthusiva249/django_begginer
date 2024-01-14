from django.db import models
from django.utils import timezone

class Door(models.Model):
    door_name = models.CharField(max_length=100, default='null')
    door_image = models.ImageField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Door"
