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

class CoordMetro(models.Model):
    metroname = models.CharField(max_length=200)
    longitude = models.TextField()
    latitude = models.TextField()
    color = models.CharField(max_length=50, null=True)
    distance_300 = models.ManyToManyField('CoordBar', related_name='metro_300')
    distance_500 = models.ManyToManyField('CoordBar', related_name='metro_500')
    distance_1000 = models.ManyToManyField('CoordBar',related_name='metro_1000')

    def __str__(self):
        return self.metroname

class CoordBar(models.Model):
    barname = models.CharField(max_length=200)
    longitude = models.TextField()
    latitude = models.TextField()
    address = models.TextField()
    district = models.TextField()
    area = models.TextField()
    phone_number = models.TextField()



    def __str__(self):
        return self.barname