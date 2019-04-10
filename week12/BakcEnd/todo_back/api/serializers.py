from rest_framework import serializers
from api.models import Task,TaskList
from datetime import datetime
from datetime import timedelta
class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self,data):
        task_list =  TaskList(**data)
        task_list.save()
        return task_list
    
    def update(self,instance,data):
        instance.name = data.get('name',instance.name)
        instance.save()
        return instance

class TaskListSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = TaskList
        fields = ('id','name',)


# DOESN'T WORK
# NEED TO FIX IT
class TasksSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    created_at = datetime.now()
    due_on = datetime.now() + timedelta(days=1)
    status = serializers.CharField()
    task_list =  TaskListSerializer(read_only=True)
    
    def create(self,data):
        task =  Task(**data)
        task.save()
        return task
