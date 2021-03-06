from django.db import models
from django.contrib.auth.models import User

AD_CATEGORIES = (
    ('Automotive', 'Automotive'),
    ('Utilities', 'Utilities'),
    ('Entertainment', 'Entertainment'),
    ('Media', 'Media'),
    ('Other', 'Other'),
)


class Ad(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=11)
    date_published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ad_category = models.CharField(max_length=15, choices=AD_CATEGORIES, default='Other')

    def __str__(self):
        return self.title


class PaidAd(models.Model):
    parent = models.ForeignKey(Ad, on_delete=models.CASCADE)
    pinned = models.BooleanField(default=False)

    def pin(self):
        self.pinned = True
        self.save()

    def unpin(self):
        self.pinned = False
        self.save()

    def __str__(self):
        return str(self.parent)
