from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import TodoModel


class TodoList_old(View):

    def get(self, request):
        context = {'todos': TodoModel.objects.all()}
        return render(request, 'todo/todo_list.html', context=context)


class TodoList(ListView):
    model = TodoModel
    context_object_name = 'todos'
    template_name = 'todo/todo_list.html'


class TodoDetail(DetailView):
    model = TodoModel
    context_object_name = 'todo'
    template_name = 'todo/todo_detail.html'
