from django import forms

levels = (
    ("8", "Triste"),
    ("7", "Enojado"),
    ("6", "Estresado"),
    ("5", "Asustado"),
    ("4", "Cansado"),
    ("3", "Amigable"),
    ("2", "Enérgico"),
    ("1", "Feliz")
)

class HowDoYouFeel(forms.Form):
    happyLevel = forms.ChoiceField(choices=levels, help_text="Seleccione cómo se siente ahora: ")
