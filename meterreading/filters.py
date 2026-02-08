import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class MeterReadingFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date", lookup_expr='gte')
	end_date = DateFilter(field_name="date", lookup_expr='lte')
	class Meta:
		model = MeterReading
		fields = '__all__'
		exclude = ['date','unit_one_current', 'unit_one_previous', 'unit_two_current','unit_two_previous','unit_three_current','unit_three_previous',
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