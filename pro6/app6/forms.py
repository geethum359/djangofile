from django import forms
from app6.models import Employee
class studentform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

