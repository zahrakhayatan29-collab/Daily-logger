from logs.views import *
from django.contrib import admin
from django.urls import path

app_name = 'logs'

urlpatterns = [
    path('', dashboard , name = 'index'),
    path('toggle-task/<int:task_id>/',toggle_task_status, name='toggle_task_status'),
]