from django import forms
from .models import CharClass

class CharForm(forms.Form):
    char_class = forms.ModelChoiceField(label="What character class would you like?", queryset=CharClass.objects.all())
    level = forms.IntegerField(label="What level should they be?", min_value=1, max_value=20, initial=1)
    num_char = forms.IntegerField(label="How many characters would you like to generate?", min_value=1, max_value=10, initial=5)