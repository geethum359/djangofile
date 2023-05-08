from django import forms
from loginapp.models import sigup
class sigupform(forms.ModelForm):
    class Meta:
        model=sigup
        fields='__all__'