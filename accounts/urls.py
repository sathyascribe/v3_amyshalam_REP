from django.urls import path
from .views import login_page, dashboard, logout_user


app_name='accounts'

urlpatterns = [
    path('login/', login_page, name='login'),
    path('', dashboard, name='index'),
    path('logout/', logout_user, name='logout'),
]
