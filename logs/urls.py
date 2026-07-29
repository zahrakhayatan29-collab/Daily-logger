from logs.views import *
from django.contrib import admin
from django.urls import path

app_name = 'logs'

urlpatterns = [
    path('', index , name = 'index'),
]