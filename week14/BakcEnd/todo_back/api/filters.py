from django_filters import rest_framework as filter
from api.models import Task

class TaskFilter(filter.FilterSet):
    name = filter.CharFilter(lookup_expr=('contains'))
    # no lte and gte , cause there is no field in out models, that will requre numberFilter
    class Meta:
        model = Task
        fields = ('name','status',)
