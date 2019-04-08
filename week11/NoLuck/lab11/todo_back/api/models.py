from django.db import models
import datetime
from datetime import datetime as dt
# Create your models here.

class Task(models.Model):
    name = CharField(max_length=200)
    created_at = dt.now()
    due_on = dt.now + datetime.timedelta(days=2)
    status = CharField(max_length=200)
    task_list = models.ForeignKey(TaskList,on_delete=CASCADE)

    def to_json(self):
        return{
            'name': self.name,
            'created-at': self.created_at,
            'task_list': self.task_list.to_json
        }