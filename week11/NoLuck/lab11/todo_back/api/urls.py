from django.urls import path, re_path
from api import views


urlpatterns = [
    path('api/', views.show_tasklists)
]