from django import forms
from .models import *



class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['dealer','invoice_No', 'date','receive_date', 'product','quantity','rate','total','paid','remaining','note']
        widgets = {
            'dealer': forms.Select(attrs={'class': 'form-control'}),
            'invoice_No': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'receive_date': forms.DateInput(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'rate': forms.TextInput(attrs={'class': 'form-control'}),
            'total': forms.TextInput(attrs={'class': 'form-control'}),
            'paid': forms.TextInput(attrs={'class': 'form-control'}),
            'remaining': forms.TextInput(attrs={'class': 'form-control'}),
            'note': forms.TextInput(attrs={'class': 'form-control'}),
        }