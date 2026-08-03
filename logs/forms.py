from django import forms
from logs.models import Log

class FormLog(forms.ModelForm):
    class Meta:
        model = Log
        fields = ['title','text','status','tags','start_time','end_time','date']