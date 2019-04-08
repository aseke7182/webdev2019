from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api import models
# Create your views here.

def show_tasklists(request):
    t_lists = models.TaskList.objects().all() #select * from tasklist
    json_t_lists = [t.to_json() for t in t_lists]
    return JsonResponse(json_t_lists, safe=False)
    