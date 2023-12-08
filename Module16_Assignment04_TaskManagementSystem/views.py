from django.shortcuts import render
from tasks_app.models import Tasks_Model

def base(request):
    return render(request, 'base.html')

def home(request):
    tasks = Tasks_Model.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)
