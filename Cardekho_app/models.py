from django.db import models
from rest_framework import serializers

def alphanumberic(value):
    if not str(value).isalnum():
        raise serializers.ValidationError("Only Alphanumeric characters are allowed")
    return value


class Showroomlist(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    website = models.URLField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
        
class Carlist(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    chassisnumber = models.CharField(max_length=100,blank=True,null=True,validators=[alphanumberic])
    price = models.DecimalField(max_digits=9,decimal_places=2,blank=True,null=True)
    
    def __str__(self) -> str:
        return self.name