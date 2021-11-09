from django import forms

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