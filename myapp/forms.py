from django import forms
from .models import FormData

class FormDataForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = ['name','email','message']