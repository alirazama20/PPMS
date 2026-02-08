import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class DailyStockFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date", lookup_expr='gte')
	end_date = DateFilter(field_name="date", lookup_expr='lte')
	class Meta:
		model = DailyStock
		fields = ''
		exclude = []