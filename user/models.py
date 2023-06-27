from django.db import models


# Create your models here.
class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    text_message = models.TextField(max_length=200)
    user = models.CharField(max_length=200)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField(max_length=255)
