from logs.views import *
from django.contrib import admin
from django.urls import path

app_name = 'logs'

urlpatterns = [
    path('', dashboard , name = 'dashboard'),
    path('add-log/',new_log,name = 'add_log'),
    path('history/',history_logs,name='history'),
    
    path('delete-log/<int:log_id>/', delete_log ,name = 'delete_log'),
    path('toggle-task/<int:task_id>/',toggle_task_status, name='toggle_task_status'),

]