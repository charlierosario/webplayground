from django import forms

from .models import Contacto


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contacto


fields = [
    'nombre',
    'sexo',
    'edad_aproximada',
    'fecha_rescate',
    ]

labels = {
    'nombre': 'Nombre',
    'sexo': 'Sexo',
    'edad_aproximada': 'Edad aproximada',
    'fecha_rescate':'Fecha de rescate',
    }

widgets = {
    'nombre': forms.TextInput(attrs={'class': 'form-control'}),
    'sexo': forms.TextInput(attrs={'class': 'form-control'}),
    'edad_aproximada': forms.TextInput(attrs={'class': 'form-control'}),
    'fecha_rescate': forms.TextInput(attrs={'class': 'form-control'}),
    }