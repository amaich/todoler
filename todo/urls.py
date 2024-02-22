from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path("todos/", views.TodoList.as_view(), name='todo_list'),
    path("todos/<int:pk>", views.TodoDetail.as_view(), name='todo_detail'),
]