from django import forms
from .models import *

class ExpenseDetailForm(forms.ModelForm):
    class Meta:
        model = ExpenseDetail
        fields = ['exp_type','exp_name', 'amount', 'date','note']
        widgets = {
            'exp_type': forms.Select(attrs={'class': 'form-control'}),
            'exp_name': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'note': forms.TextInput(attrs={'class': 'form-control'}),
        }

