from pyexpat import model
from re import T
from turtle import Turtle
from django.db import models

# Create your models here.

class Company(models.Model):
    rank = models.CharField(max_length=3)
    code = models.CharField(max_length=20)
    company = models.CharField(max_length=100, primary_key=True)
    last_update = models.DateField()
    last_update_time = models.TimeField()
    #rate = models.CharField(max_length=10)
    
    def __str__(self):
        return self.company