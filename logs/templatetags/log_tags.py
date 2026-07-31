from django import template
from datetime import datetime

register = template.Library()

@register.filter
def total_hours(log_list):
    if not log_list:
        return "00"

    total_minutes = 0

    for item in log_list:
        if item.start_time and item.end_time:
            start_min = item.start_time.hour * 60 + item.start_time.minute
            end_min = item.end_time.hour * 60 + item.end_time.minute
            
            if end_min >= start_min:
                total_minutes += (end_min - start_min)

    hours = total_minutes // 60
    minutes = total_minutes % 60

    if hours > 0:
        return f"{hours}h {minutes}m"
    return f"{minutes}m"

@register.filter
def percent_tasks(log_list):
    if log_list :
        done = []
        for item in log_list :
            if item.status :
                done.append(item)
        if len(done) == 0 :
             return "0 %"

        precent = round(len(done)/len(log_list)* 100) 
        return f"{precent}%"

    else:
        return "0 %"

@register.filter
def pending(log_list):
    if log_list :
        list = []
        for item in log_list :
            if not item.status :
                list.append(item)
        return len(list)
    else:
        return "0"