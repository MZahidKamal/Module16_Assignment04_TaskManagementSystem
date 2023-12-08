from django import forms
from .models import Tasks_Model

class TasksModel_Form(forms.ModelForm):
    class Meta:
        model = Tasks_Model
        fields = '__all__'
        exclude = ['completed']
        labels = {
            'title': 'Name your task',
            'description': 'Describe your task here',
            'assign_date': 'Set the date and time',
            'category': 'Which category does it belongs to',
        }
        widgets = {
            'assign_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'category': forms.CheckboxSelectMultiple(),
        }
        error_messages = {
            'title': {
                'max_length': 'Title not more than 200 characters please',
                'unique': 'This title already exists',
            },
            'assign_date': {
                'unique': 'Sorry, this date and time is already booked',
            },
        }
