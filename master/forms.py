from django import forms
from .models import *


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
class DealerForm(forms.ModelForm):
    class Meta:
        model = Dealer
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [ 'emp_name', 'salary', 'perday']
        widgets = {
            'emp_name': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.TextInput(attrs={'class': 'form-control'}),
            'perday': forms.TextInput(attrs={'class': 'form-control'}),
        }

class VechileForm(forms.ModelForm):
    class Meta:
        model = Vechile
        fields = ['name','account']
        widgets = {
            'account': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ['name','item']
        widgets = {
            'item': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }