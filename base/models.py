from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Speciality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Doctors(models.Model):
    name = models.CharField(max_length=100)
    availability = models.BooleanField(default=False)
    appointments = models.IntegerField(default=0)
    speciality = models.ManyToManyField(Speciality)
    email=models.EmailField(null=True)

    def __str__(self):
        return self.name