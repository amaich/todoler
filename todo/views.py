from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import TodoModel


def hello_world(request):
    todos = TodoModel.objects.all()
    return HttpResponse(todos)


class TodoList(View):

    def get(self, request):
        context = {'todos': TodoModel.objects.all()}
        return render(request, 'todo/todo_list.html', context=context)

