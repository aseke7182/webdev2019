from rest_framework import serializers
from api.models import Task,TaskList

class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(reqired=True)

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
