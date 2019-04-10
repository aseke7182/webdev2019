import json
from django.shortcuts import render
from api.models import Task,TaskList
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.serializers import TaskListSerializer
@csrf_exempt
def task_lists(request):
    if request.method == 'GET':
        task_lists = TaskList.objects.all()
        task_lists_json = [t.to_json() for t in task_lists]
        return JsonResponse(task_lists_json,safe=False)
    elif request.method =='POST':
        data = json.loads(request.body)
        serializer = TaskListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

@csrf_exempt
def task_lists_info(request,pk):
    try:
        task_lists_info = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'Error':str(e)},safe=False)
    return JsonResponse(task_lists_info.to_json(),safe=False)

@csrf_exempt
def tasks(request,pk):
    try:
        task_lists_info = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'Error':str(e)},safe=False)
    tasks =  task_lists_info.task_set.all()
    task = [ t.to_json() for t in tasks ]
    return JsonResponse(task,safe=False)


