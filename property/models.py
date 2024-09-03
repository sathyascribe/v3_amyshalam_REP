from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.



class PropertyType(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class PropertyStatus(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Property(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(PropertyStatus, on_delete=models.SET_NULL, null=True)
    price = models.CharField(max_length=20)
    address_line_1 = models.CharField(max_length=150)
    address_line_2 = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=40)
    province_state = models.CharField(max_length=40)
    zipcode = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="property_images/")