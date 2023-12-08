from django.shortcuts import render, redirect
from .forms import TasksModel_Form
from .models import Tasks_Model

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        form = TasksModel_Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
    else:
        form = TasksModel_Form()
    context = {'form': form}
    return render(request, 'tasks_app/add_task.html', context)


def show_task(request, task_id):
    task_from_db = Tasks_Model.objects.get(pk=task_id)
    context = {'task': task_from_db}
    return render(request, 'tasks_app/show_task.html', context)


def complete_task(request, task_id):
    task_from_db = Tasks_Model.objects.get(pk=task_id)
    task_from_db.completed = True
    task_from_db.save()
    return redirect('home')


def edit_task(request, task_id):
    task_from_db = Tasks_Model.objects.get(pk=task_id)
    form = TasksModel_Form(instance=task_from_db)
    if request.method == 'POST':
        form = TasksModel_Form(request.POST, instance=task_from_db)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
    context = {'form': form}
    return render(request, 'tasks_app/edit_task.html', context)


def delete_task(request, task_id):
    task_from_db = Tasks_Model.objects.get(pk=task_id)
    task_from_db.delete()
    return redirect('home')
