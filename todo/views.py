from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import TodoModel


def hello_world(request):
    todos = TodoModel.objects.all()
    return HttpResponse(todos)


class TodoList(ListView):
    model = TodoModel
    template_name = 'todo/todo_list.html'
    context_object_name = 'todos'


class TodoCreate(CreateView):
    model = TodoModel
    template_name = 'todo/todo_create.html'
    fields = ['name']
    success_url = reverse_lazy('todo:todo_list')


class TodoDetail(DetailView):
    model = TodoModel
    template_name = 'todo/todo_details.html'
    context_object_name = 'todo'


class TodoUpdate(UpdateView):
    model = TodoModel
    template_name = 'todo/todo_update.html'
    context_object_name = 'todo'

    def get_success_url(self):
        return reverse('todo:todo_detail', kwargs={'pk': self.object.id})


class TodoDelete(DeleteView):
    model = TodoModel
    template_name = 'todo/todo_delete.html'
    context_object_name = 'todo'
    success_url = reverse_lazy('todo:todo_delete')

