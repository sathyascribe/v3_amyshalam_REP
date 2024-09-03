from django.contrib import admin
from .models import Property, PropertyStatus, PropertyType, PropertyImage
# Register your models here.



admin.site.register(Property)
admin.site.register(PropertyStatus)
admin.site.register(PropertyType)
admin.site.register(PropertyImage)