from django.db import models
from django.utils import timezone

# Create your models here.

class Mainpage(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class coord_metro(models.Model):
    metroname = models.CharField(max_length=200)
    langituge = models.TextField()
    latitude = models.TextField()

    def __str__(self):
        return self.title