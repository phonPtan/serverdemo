from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CarInfo(models.Model):
    carid = models.CharField(max_length=200,null=True)
    lane = models.CharField(max_length=200,null=True)
    uniqueNumber = models.CharField(max_length=200,null=True)
    time = models.TimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    front_license_number = models.CharField(max_length=200,null=True,blank=True)
    front_license_image = models.ImageField(upload_to = 'images/',null=True,blank=True)
    front_car_image = models.ImageField(upload_to = 'images/',null=True,blank=True)
    end_license_number = models.CharField(max_length=200,null=True,blank=True)
    end_license_image = models.ImageField(upload_to = 'images/',null=True,blank=True)
    end_car_image = models.ImageField(upload_to = 'images/',null=True,blank=True)
    velocity = models.FloatField(null=True,blank=True)
    number_axis = models.IntegerField(null=True,blank=True)
    totalweight = models.FloatField(null=True,blank=True)
    listweight = models.CharField(max_length=1024,null=True,blank=True)
    maxD = models.FloatField(null=True,blank=True)
    listD = models.CharField(max_length=1024,null=True,blank=True)

    def __str__(self):
        return self.uniqueNumber