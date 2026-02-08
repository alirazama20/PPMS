import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class PurchaseFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date", lookup_expr='gte')
	end_date = DateFilter(field_name="date", lookup_expr='lte')
	class Meta:
		model = Purchase
		fields = '__all__'
		exclude = ['date', 'quantity','total','rate','paid','remaining','note']

class PurchaseFilterReport(django_filters.FilterSet):
	start_date = DateFilter(field_name="date", lookup_expr='gte')
	end_date = DateFilter(field_name="date", lookup_expr='lte')
	class Meta:
		model = Purchase
		fields = '__all__'
		exclude = ['receive_date','date', 'quantity','total','rate','paid','remaining','note']
