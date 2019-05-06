from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from api.models import TaskList, Task
from api.serializers import TaskListSerializer, TasksSerializer, UserSerializer


class TaskListList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskListSerializer

    def get_queryset(self):
        return TaskList.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskListInfo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskListSerializer

    def get_queryset(self):
        return TaskList.objects.for_user(self.request.user)


class TasksList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TasksSerializer

    def get_queryset(self):
        tasklist = get_object_or_404(TaskList, id=self.kwargs.get('pk'))
        return tasklist.task_set.filter(task_list__owner=self.request.user)


class TaskInfo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TasksSerializer
    lookup_url_kwarg = 'pk2'

    def get_queryset(self):
        tasklist = get_object_or_404(TaskList, id=self.kwargs.get('pk'))
        return tasklist.task_set.filter(task_list__owner=self.request.user)
