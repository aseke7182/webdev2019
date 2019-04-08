from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from api.models import TaskList,Task

def task_lists(request):
    task_lists = TaskList.objects.all()
    json = [t.to_json() for t in task_lists]
    return JsonResponse(json,safe=False)

def task_info(request,pk):
    try:
        task_list =  TaskList.objects.get(id=pk)
    except  TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)},safe=False)
    return JsonResponse(task_list.to_json(),safe=False)

def tasks(request,pk):
    try:
        t_list = TaskList.objects.get(id = pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)},safe= False)

    tasks = Task.tasks_set.all()
    json_tasks = [t.to_json for t in tasks]
    return JsonResponse(json_tasks,safe=False)



