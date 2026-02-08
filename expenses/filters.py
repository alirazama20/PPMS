import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class ExpenseDetailFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date", lookup_expr='gte')
	end_date = DateFilter(field_name="date", lookup_expr='lte')
	class Meta:
		model = ExpenseDetail
		fields = '__all__'
		exclude = ['amount','date','note']