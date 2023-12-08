from django import forms
from .models import Categories_Model

class CategoriesModel_Form(forms.ModelForm):
    class Meta:
        model = Categories_Model
        fields = '__all__'
        labels = {
            'name': 'Name the category',
        }
        error_messages = {
            'name': {
                'max_length': 'Name not more than 50 characters please',
                'unique': 'Sorry, this category name already exists',
            },
        }
