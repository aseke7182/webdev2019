from django.contrib import admin
from api.models import Task, TaskList

# admin.site.register(Task)
# admin.site.register(TaskList)


@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # list_display = '__all__'
    list_display = [field.name for field in Task._meta.get_fields()]
