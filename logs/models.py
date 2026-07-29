from django.db import models

# Create your models here.


class Log(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(null=True,blank=True)
    #tags
    status = models.BooleanField(default=False)
    start_time = models.TimeField(null=True,blank=True)
    end_time = models.TimeField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True)
