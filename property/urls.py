from django.urls import path
from .views import create_property, property_list_view, property_detail_view


app_name = 'property'

urlpatterns = [
    path('add/', create_property, name='add_property'),
    path('list/', property_list_view, name='property_list'),
    path('property/<int:property_id>/', property_detail_view, name='property_detail'),
]
