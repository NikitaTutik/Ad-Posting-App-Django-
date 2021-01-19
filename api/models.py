from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=11)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title