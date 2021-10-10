from django.contrib.auth.models import User
from django.db import models

LANGUAGE_CHOICES = (("Korean", "Korean"), ("English", "English"), ("Japanese", "Japanese"),
                    ("Simplified Chinese", "Simplified Chinese"), ("Traditional Chinese", "Traditional Chinese"),
                    ("Vietnamese", "Vietnamese"), ("Indonesian", "Indonesian"), ("Thai", "Thai"), ("German", "German"),
                    ("Russian", "Russian"), ("Spanish", "Spanish"), ("Italian", "Italian"), ("French", "French"))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=20, null=False, blank=False)
