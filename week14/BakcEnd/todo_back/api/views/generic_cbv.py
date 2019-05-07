from rest_framework import generics,filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from api.models import TaskList, Task
from api.serializers import TaskListSerializer, TasksSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from api.filters import TaskFilter


class TaskListList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskListSerializer

    def get_queryset(self):
        queryset = TaskList.objects.for_user(self.request.user)
        name = self.request.query_params.get('name')
        if name is not None:
             queryset = queryset.filter(name=name)
        return queryset


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskListInfo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskListSerializer

    def get_queryset(self):
        return TaskList.objects.for_user(self.request.user)


class TasksList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    # pagination_class = PageNumberPagination      # Just exatly how many files on one page
    pagination_class = LimitOffsetPagination       # How many you should offset and limit on one page
    serializer_class = TasksSerializer
    filter_class = TaskFilter # url ... ?___=___
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter,)  # lik settings
    search_fields = ('name','status',)  # url... ?serach=...
    ordering_fileds = ('name','status',)   # you can order by this      ?url ordering=name     or ?url ordering=-name
    ordering = ('name',) # order by what
    # filterset_fields = ('name','status',)

    def get_queryset(self):
        tasklist = get_object_or_404(TaskList, id=self.kwargs.get('pk'))
        queryset = tasklist.task.filter(task_list__owner=self.request.user)
        # name = self.request.query_params.get('name',None)
        # status = self.request.query_params.get('status', None)
        # if name is not None:
        #     queryset = queryset.filter(name=name)
        # if status is not None:
        #     queryset = queryset.filter(status=status)
        return queryset


class TaskInfo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TasksSerializer
    lookup_url_kwarg = 'pk2'

    def get_queryset(self):
        tasklist = get_object_or_404(TaskList, id=self.kwargs.get('pk'))
        return tasklist.task.filter(task_list__owner=self.request.user)
