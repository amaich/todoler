from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path("", views.hello_world),
    path("todos/", views.TodoList.as_view(), name='todo_list'),
    path("todos/create", views.TodoCreate.as_view(), name='todo_create'),
    path("todos/<int:pk>", views.TodoDetail.as_view(), name='todo_detail'),
    path("todos/<int:pk>/update", views.TodoUpdate.as_view(), name='todo_update'),
    path("todos/<int:pk>/delete", views.TodoDelete.as_view(), name='todo_delete')
]