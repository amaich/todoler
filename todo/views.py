from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoModel


def hello_world(request):
    todos = TodoModel.objects.all()
    return HttpResponse(todos)


# Create your views here.
