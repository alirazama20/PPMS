from django import forms
from .models import *

class DailyStockForm(forms.ModelForm):
    class Meta:
        model = DailyStock
        fields = ['date','dip_one_hsd','ltrs_one_hsd','diff_ltrs_one_hsd','status_one_hsd','stock_one_hsd','sale_one_hsd','rmg_one_hsd',
                  'dip_two_hsd', 'ltrs_two_hsd', 'diff_ltrs_two_hsd', 'status_two_hsd', 'stock_two_hsd', 'sale_two_hsd','rmg_two_hsd',
                  'dip_pmg', 'ltrs_pmg', 'diff_pmg', 'status_pmg', 'stock_pmg', 'sale_pmg','rmg_pmg','note'
                  ]
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control'}),

            'dip_one_hsd': forms.TextInput(attrs={'class': 'form-control'}),
            'ltrs_one_hsd': forms.TextInput(attrs={'class': 'form-control'}),
            'diff_ltrs_one_hsd': forms.TextInput(attrs={'class': 'form-control'}),
            'status_one_hsd': forms.TextInput(attrs={'class': 'form-control'}),
            'stock_one_hsd': forms.TextInput(attrs={'class': 'form-control'}),
            'sale_one_hsd': forms.TextInput(attrs={'class': 'form-control'}),
            'rmg_one_hsd': forms.TextInput(attrs={'class': 'form-control'}),

            'dip_two_hsd': forms.TextInput(attrs={'class': 'form-control'}),
            'ltrs_two_hsd': forms.TextInput(attrs={'class': 'form-control'}),
            'diff_ltrs_two_hsd': forms.TextInput(attrs={'class': 'form-control'}),
            'status_two_hsd': forms.TextInput(attrs={'class': 'form-control'}),
            'stock_two_hsd': forms.TextInput(attrs={'class': 'form-control'}),
            'sale_two_hsd': forms.TextInput(attrs={'class': 'form-control'}),
            'rmg_two_hsd': forms.TextInput(attrs={'class': 'form-control'}),

            'dip_pmg': forms.TextInput(attrs={'class': 'form-control'}),
            'ltrs_pmg': forms.TextInput(attrs={'class': 'form-control'}),
            'diff_pmg': forms.TextInput(attrs={'class': 'form-control'}),
            'status_pmg': forms.TextInput(attrs={'class': 'form-control'}),
            'stock_pmg': forms.TextInput(attrs={'class': 'form-control'}),
            'sale_pmg': forms.TextInput(attrs={'class': 'form-control'}),
            'rmg_pmg': forms.TextInput(attrs={'class': 'form-control'}),
            'note': forms.TextInput(attrs={'class': 'form-control'}),
        }

