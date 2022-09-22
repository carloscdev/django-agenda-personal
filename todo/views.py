from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages

def index(request):
    todos = Todo.objects.filter(title__contains=request.GET.get('search', '')).order_by('finished', '-priority')

    context = {
        'todos': todos
    }
    return render(request, 'views/todo/index.html', context)

def detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'views/todo/detail.html', context)

def update(request, id):
    todo = Todo.objects.get(id=id)

    if request.method == 'GET':
        form = TodoForm(instance=todo)
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'views/todo/update.html', context)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
            'id': id
        }
        messages.success(request, 'Tarea actualizada correctamente')
        return render(request, 'views/todo/update.html', context)

def create(request):
    if request.method == 'GET':
        form = TodoForm()
        context = {
            'form': form
        }
        return render(request, 'views/todo/create.html', context)

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('todo')

def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()

    return redirect('todo')

