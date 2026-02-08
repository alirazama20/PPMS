from django import forms
from .models import *
class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['created_date','invoiceType','catagery', 'invoiceNo','name','phone','account','vechile','item_name',
                  'date','quantity','saleprice','totalAmount','paidAmount','remainingAmount','note','purchase','profit']
        widgets = {
            'invoiceType': forms.Select(attrs={'class': 'form-control'}),
            'catagery': forms.Select(attrs={'class': 'form-control'}),
            'invoiceNo': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'item_name': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'created_date': forms.DateInput(attrs={'class': 'form-control'}),
            'account': forms.Select(attrs={'class': 'form-control'}),
            'vechile': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'saleprice': forms.TextInput(attrs={'class': 'form-control'}),
            'totalAmount': forms.TextInput(attrs={'class': 'form-control'}),
            'paidAmount': forms.TextInput(attrs={'class': 'form-control'}),
            'remainingAmount': forms.TextInput(attrs={'class': 'form-control'}),
            'note': forms.TextInput(attrs={'class': 'form-control'}),
            'purchase': forms.TextInput(attrs={'class': 'form-control'}),
            'profit': forms.TextInput(attrs={'class': 'form-control'}),
        }
class TyreSaleForm(forms.ModelForm):
    class Meta:
        model = TyreSale
        fields = ['created_date','invoiceType','catagery', 'invoiceNo','name','phone','account','vechile','item_name',
                  'date','quantity','saleprice','totalAmount','paidAmount','remainingAmount','note','purchase','profit']
        widgets = {
            'invoiceType': forms.Select(attrs={'class': 'form-control'}),
            'catagery': forms.Select(attrs={'class': 'form-control'}),
            'invoiceNo': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'item_name': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'created_date': forms.DateInput(attrs={'class': 'form-control'}),
            'account': forms.Select(attrs={'class': 'form-control'}),
            'vechile': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'saleprice': forms.TextInput(attrs={'class': 'form-control'}),
            'totalAmount': forms.TextInput(attrs={'class': 'form-control'}),
            'paidAmount': forms.TextInput(attrs={'class': 'form-control'}),
            'remainingAmount': forms.TextInput(attrs={'class': 'form-control'}),
            'note': forms.TextInput(attrs={'class': 'form-control'}),
            'purchase': forms.TextInput(attrs={'class': 'form-control'}),
            'profit': forms.TextInput(attrs={'class': 'form-control'}),
        }
