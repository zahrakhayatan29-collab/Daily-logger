from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone
from django.contrib.auth.models import User


class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logs')

    title = models.CharField(max_length=255)
    text = models.TextField(null=True,blank=True)
    tags = TaggableManager()
    status = models.BooleanField(default=False)
    start_time = models.TimeField(null=True,blank=True)
    end_time = models.TimeField(null=True,blank=True)
    date = models.DateField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f"{self.user.username} _ {self.title}"
