from django.db import models
from datetime import datetime
from datetime import timedelta
# Create your models here.

class TaskList(models.Model):
    name = models.CharField(max_length = 200)

class Task(models.Model):
    name = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now=True)
    due_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length = 200)
    task_list = models.ForeignKey(TaskList,on_delete=models.CASCADE)
