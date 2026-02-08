from django import forms
from .models import *

class MeterReadingForm(forms.ModelForm):
    class Meta:
        model = MeterReading
        fields = ['date', 'unit_one_current', 'unit_one_previous', 'unit_two_current','unit_two_previous','unit_three_current','unit_three_previous',
                  'unit_four_current','unit_four_previous','unit_five_current','unit_five_previous','unit_six_current','unit_six_previous','note',
                  'unit_one_equal','unit_two_equal','unit_three_equal','unit_four_equal','unit_five_equal','unit_six_equal',
                  'total_diesel','total_petrol','test_diesel','test_petrol','credit_diesel','credit_petrol','cash_diesel','cash_petrol',
                  'dunit_one_current', 'dunit_one_previous', 'dunit_two_current', 'dunit_two_previous',
                  'dunit_three_current', 'dunit_three_previous',
                  'dunit_four_current', 'dunit_four_previous', 'dunit_five_current', 'dunit_five_previous',
                  'dunit_six_current', 'dunit_six_previous',
                  'dunit_one_equal', 'dunit_two_equal', 'dunit_three_equal', 'dunit_four_equal', 'dunit_five_equal',
                  'dunit_six_equal',
                  'diesel_rate', 'diesel_Rs', 'petrol_rate', 'petrol_Rs', 'testDie_rate', 'testDie_Rs', 'testPet_rate',
                   'testPet_Rs',
                   'crdie_rate', 'crdie_Rs', 'crPet_rate', 'crPet_Rs', 'cashDie_rate', 'cashDie_Rs', 'cashPet_rate',
                   'cashPet_Rs'
                  ]
        widgets = {
            'dunit_one_current': forms.TextInput(attrs={'class': 'form-control'}),
            'dunit_one_previous': forms.TextInput(attrs={'class': 'form-control'}),
            'dunit_two_current': forms.TextInput(attrs={'class': 'form-control'}),
            'dunit_two_previous': forms.TextInput(attrs={'class': 'form-control'}),
            'dunit_three_current': forms.TextInput(attrs={'class': 'form-control'}),
            'dunit_three_previous': forms.TextInput(attrs={'class': 'form-control'}),
            'dunit_four_current': forms.TextInput(attrs={'class': 'form-control'}),
            'dunit_four_previous': forms.TextInput(attrs={'class': 'form-control'}),
            'dunit_five_current': forms.TextInput(attrs={'class': 'form-control'}),
            'dunit_five_previous': forms.TextInput(attrs={'class': 'form-control'}),
            'dunit_six_current': forms.TextInput(attrs={'class': 'form-control'}),
            'dunit_six_previous': forms.TextInput(attrs={'class': 'form-control'}),

            'dunit_one_equal': forms.TextInput(attrs={'class': 'form-control'}),
            'dunit_two_equal': forms.TextInput(attrs={'class': 'form-control'}),
            'dunit_three_equal': forms.TextInput(attrs={'class': 'form-control'}),
            'dunit_four_equal': forms.TextInput(attrs={'class': 'form-control'}),
            'dunit_five_equal': forms.TextInput(attrs={'class': 'form-control'}),
            'dunit_six_equal': forms.TextInput(attrs={'class': 'form-control'}),

            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'unit_one_current': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_one_previous': forms.TextInput(attrs={'class': 'form-control'}),
             'unit_two_current': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_two_previous': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_three_current': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_three_previous': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_four_current': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_four_previous': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_five_current': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_five_previous': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_six_current': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_six_previous': forms.TextInput(attrs={'class': 'form-control'}),

            'unit_one_equal': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_two_equal': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_three_equal': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_four_equal': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_five_equal': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_six_equal': forms.TextInput(attrs={'class': 'form-control'}),

            'total_diesel': forms.TextInput(attrs={'class': 'form-control'}),
            'diesel_rate': forms.TextInput(attrs={'class': 'form-control'}),
            'diesel_Rs': forms.TextInput(attrs={'class': 'form-control'}),

            'total_petrol': forms.TextInput(attrs={'class': 'form-control'}),
            'petrol_rate': forms.TextInput(attrs={'class': 'form-control'}),
            'petrol_Rs': forms.TextInput(attrs={'class': 'form-control'}),

            'test_diesel': forms.TextInput(attrs={'class': 'form-control'}),
            'testDie_rate': forms.TextInput(attrs={'class': 'form-control'}),
            'testDie_Rs': forms.TextInput(attrs={'class': 'form-control'}),

            'test_petrol': forms.TextInput(attrs={'class': 'form-control'}),
            'testPet_rate': forms.TextInput(attrs={'class': 'form-control'}),
            'testPet_Rs': forms.TextInput(attrs={'class': 'form-control'}),

            'credit_diesel': forms.TextInput(attrs={'class': 'form-control'}),
            'crdie_rate': forms.TextInput(attrs={'class': 'form-control'}),
            'crdie_Rs': forms.TextInput(attrs={'class': 'form-control'}),

            'credit_petrol': forms.TextInput(attrs={'class': 'form-control'}),
            'crPet_rate': forms.TextInput(attrs={'class': 'form-control'}),
            'crPet_Rs': forms.TextInput(attrs={'class': 'form-control'}),

            'cash_diesel': forms.TextInput(attrs={'class': 'form-control'}),
            'cashDie_rate': forms.TextInput(attrs={'class': 'form-control'}),
            'cashDie_Rs': forms.TextInput(attrs={'class': 'form-control'}),

            'cash_petrol': forms.TextInput(attrs={'class': 'form-control'}),
            'cashPet_rate': forms.TextInput(attrs={'class': 'form-control'}),
            'cashPet_Rs': forms.TextInput(attrs={'class': 'form-control'}),

            'note': forms.TextInput(attrs={'class': 'form-control'}),
        }

