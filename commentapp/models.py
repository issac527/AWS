from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from functionapp.models import FunctionInfo


class Comment(models.Model):
    func = models.ForeignKey(FunctionInfo, on_delete=models.CASCADE, null=True, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='comment')

    content = models.TextField(null = False)

    create_at = models.DateTimeField(auto_now=True)