from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello_world),
    path("todos/", views.TodoList.as_view())
]