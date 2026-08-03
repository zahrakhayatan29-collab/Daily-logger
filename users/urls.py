
from logs.views import *
from django.contrib import admin
from django.urls import path

app_name = 'users'


urlpatterns = [
    path('loggin/',loggin_view,name='loggin'),
]