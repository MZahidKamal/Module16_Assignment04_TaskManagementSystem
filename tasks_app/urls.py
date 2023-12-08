from django.urls import path
from .views import add_task, show_task, complete_task, edit_task, delete_task

urlpatterns = [
    path('tasks/add_task/', add_task, name='add_task'),
    path('tasks/show_task/<int:task_id>/', show_task, name='show_task'),
    path('tasks/complete_task/<int:task_id>/', complete_task, name='complete_task'),
    path('tasks/edit_task/<int:task_id>/', edit_task, name='edit_task'),
    path('tasks/delete_task/<int:task_id>/', delete_task, name='delete_task'),
]
