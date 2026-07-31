from django.shortcuts import render , redirect ,get_object_or_404
from logs.models import Log
from datetime import date
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def dashboard(request):
    today = date.today()
    today_tasks = Log.objects.filter(date=today)
    context = {
        'log' : today_tasks ,
        'today' : today ,
        }

    return render(request,'logs/index.html',context=context)



@require_POST
def toggle_task_status(request, task_id):
    try:
        task = Log.objects.get(id=task_id)
        task.status = not task.status
        task.save()
        return JsonResponse({'success': True, 'new_status': task.status})

    except Log.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Task not found'}, status=404)




