from django.shortcuts import render, redirect
from .forms import CategoriesModel_Form

# Create your views here.
def add_category(request):
    if request.method == 'POST':
        form = CategoriesModel_Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('add_task')
    else:
        form = CategoriesModel_Form()
    context = {'form': form}
    return render(request, 'categories_app/add_category.html', context)
