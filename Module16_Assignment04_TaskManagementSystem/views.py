from django.shortcuts import render
from tasks_app.models import Tasks_Model

def base(request):
    return render(request, 'base.html')

def home(request):
    # tasks = Tasks_Model.objects.all()
    tasks = Tasks_Model.objects.order_by('assign_date')
    context = {'tasks': tasks}
    return render(request, 'index.html', context)
