from django import forms
from django.forms import ModelForm
from .models import EspecialEvent


class eventRegisterForm(forms.Form):
    nombre = forms.Field()
    descripcion = forms.Field()
    duracion = forms.Field()
    hora = forms.Field()
    fecha = forms.DateField()
    maximo = forms.Field()
    tipo = forms.Field()
    direccion = forms.Field()
    email = forms.EmailField()


class EspecialEventForm(ModelForm):
    class Meta:
        model = EspecialEvent
        fields = ['name', 'description', 'category',
                  'dateTime', 'address', 'contact', 'creator', 'capacity']
