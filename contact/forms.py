from django import forms
from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ['created']
        labels= {
            'name': 'Nombre',
            'last_name': 'Apellido',
            'mobile': 'Móvil',
            'phone': 'Teléfono',
            'company': 'Compañia',
            'notes': 'Nota',
            'is_favorite': 'Favorito'
        }
        widgets = {
            'notes': forms.Textarea(attrs={'rows': '3'})
        }