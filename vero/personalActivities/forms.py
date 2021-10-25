from django import forms

class PersonalActivitiesFilterForm(forms.Form):
  category = forms.CharField(label='Your name', max_length=100)
class personalActivitiesForm(forms.Form):
    respiracion = forms.Field(widget=forms.TextInput(attrs={"class":"check-act", "type":"checkbox", "name":"check"}), label=False, required=False)
    estiramiento = forms.Field(widget=forms.TextInput(attrs={"class":"check-act", "type":"checkbox", "name": "check"}), label=False, required=False)
    recurso = forms.CharField()
    video = forms.ChoiceField(widget=forms.TextInput(attrs={"class":"btn btn-primary", "type":"button", "name": "video"}), label=False, required=False)
    audio = forms.ChoiceField(widget=forms.TextInput(attrs={"class":"btn btn-primary", "type":"button", "name": "audio"}), label=False, required=False)
    texto = forms.ChoiceField(widget=forms.TextInput(attrs={"class":"btn btn-primary", "type":"button", "name": "texto"}), label=False, required=False)

