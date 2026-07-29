from django.contrib import admin
from logs.models import Log
# Register your models here.

@admin.register(Log)
class admin_log(admin.ModelAdmin):
    list_display = ['title','status','start_time','end_time']
    filter = ['status']
    search_fields = ['title']