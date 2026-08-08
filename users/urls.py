
from users.views import *
from django.contrib import admin
from django.urls import path

app_name = 'users'


urlpatterns = [
    path('login/',login_view,name='login'),
    path('logout/',logout_viwe,name='logout'),
    path('register/',register_viwe,name='register')
]