from django.db import models
from datetime import datetime as d
import datetime

class TaskList(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return '{}: {}'.format(self.id,self.name)

    def to_json(self):
        return{
            'name': self.name
        }

class Task(models.Model):
    name = models.CharField(max_length = 200)
    created_at = d.now()
    due_on = d.now() + datetime.timedelta(days=5)
    status = models.CharField(max_length=200)
    task_list = models.ForeignKey(TaskList,on_delete=models.CASCADE)

    def __str__(self):
        return '{}:{}'.format(self.id,self.name)

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'created at': self.created_at,
            'due on': self.due_on,
            'status': self.status,
            # 'task list': self.task_list.to_json
        }


