from django.db import models
from datetime import datetime
from datetime import timedelta
# Create your models here.

class TaskList(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return '{}:{}'.format(self.id,self.name)

    def to_json(self):
        return {
            'id' : self.id,
            'name' : self.name
        }

class Task(models.Model):
    name = models.CharField(max_length = 200)
    created_at = datetime.now()
    due_on = datetime.now() + timedelta(days=1)
    status = models.CharField(max_length = 200)
    task_list = models.ForeignKey(TaskList,on_delete=models.CASCADE)

    def __str__(self):
        return '{}:{}:{}:{}:{}'.format(self.id,self.name,self.created_at,self.due_on,self.status)

    def to_json(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'created_at' : self.created_at,
            'due_on' : self.due_on,
            'status' : self.status,
            # 'task_list': self.task_list.to_json(),
        }