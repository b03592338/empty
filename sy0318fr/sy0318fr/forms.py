from django import forms
from .models import Memory

class Form(forms.Form):
    image = forms.ModelChoiceField(queryset=Memory.objects.all(), label="Add new memory")