from django.db import models
from django.contrib.auth.models import User


class Ad(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=11)
    date_published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

