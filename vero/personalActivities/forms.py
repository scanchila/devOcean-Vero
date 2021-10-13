from django import forms

class PersonalActivitiesFilterForm(forms.Form):
  category = forms.CharField(label='Your name', max_length=100)
