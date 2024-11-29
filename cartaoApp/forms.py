from django import forms
from cartaoApp.models import Validar

class ValidarForm(forms.ModelForm):
    class Meta:
        model = Validar
        fields = '__all__'