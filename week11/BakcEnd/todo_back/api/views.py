from django.shortcuts import render
from api.models import Task,TaskList
from django.http import JsonResponse
# Create your views here.

def task_lists(request):
    task_lists = TaskList.objects.all()
    task_lists_json = [t.to_json() for t in task_lists]
    return JsonResponse(task_lists_json,safe=False)

def task_lists_info(request,pk):
    try:
        task_lists_info = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'Error':str(e)},safe=False)
    return JsonResponse(task_lists_info.to_json(),safe=False)

def tasks(request,pk):
    try:
        task_lists_info = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'Error':str(e)},safe=False)
    tasks =  task_lists_info.task_set.all()
    task = [ t.to_json() for t in tasks ]
    return JsonResponse(task,safe=False)


