from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages


def home(request):
    return render(request, 'home.html')

def task(request):
    todos = Todo.objects.all()
    Todo.objects.filter(completed=True).delete()
    return render(request, 'task.html', {'todos': todos})

def add_task(request):
    todos = Todo.objects.all()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task')
    else:
        form = TodoForm()
    # Delete completed tasks
    
   
    return render(request, 'add_task.html', {
        'todos': todos,
        'form': form
    })

def delete_task(request, task_id):
    todo = Todo.objects.get(pk=task_id)
    todo.delete()
    return redirect('task')

def complete_task(request, task_id):
    todo = Todo.objects.get(pk=task_id)
    todo.delete()
    messages.success(request, "congrates you have completed the task")
    return redirect('task')


    
    

# Create your views here.
