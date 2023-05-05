from django import forms
from modelapp.models import employee
class employe_Form(forms.ModelForm):
    class Meta:
        model=employee
        fields='__all__'