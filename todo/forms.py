from django.forms import ModelForm
from .models import Todo
from django import forms

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        exclude = ['created'],
        fields = ['title', 'priority', 'estimated_end', 'description', 'finished']
        labels = {
            'title': 'Título',
            'priority': 'Prioridad',
            'estimated_end': 'Fecha estimada',
            'description': 'Descripción',
            'finished': 'Finalizado',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'estimated_end': forms.DateInput(attrs={'type': 'date'})
        }