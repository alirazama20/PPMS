import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class SaleBillFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date", lookup_expr='gte')
	end_date = DateFilter(field_name="date", lookup_expr='lte')
	class Meta:
		model = Sale
		fields = '__all__'
		exclude = ['phone', 'date','quantity','saleprice','totalAmount','paidAmount','remainingAmount','note','purchase','profit']

class SaleBillReportFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date", lookup_expr='gte')
	end_date = DateFilter(field_name="date", lookup_expr='lte')
	class Meta:
		model = Sale
		fields = '__all__'
		exclude = ['created_date', 'invoiceNo','name','phone','item_name',
                  'date','quantity','saleprice','totalAmount','paidAmount','remainingAmount','note','purchase','profit']


class SaleBillProfitFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date", lookup_expr='gte')
	end_date = DateFilter(field_name="date", lookup_expr='lte')
	class Meta:
		model = Sale
		fields = '__all__'
		exclude = ['account','vechile', 'invoiceNo','name','phone',
                  'date','quantity','totalAmount','paidAmount','remainingAmount','note','profit']

class TyreSaleFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date", lookup_expr='gte')
	end_date = DateFilter(field_name="date", lookup_expr='lte')
	class Meta:
		model = TyreSale
		fields = '__all__'
		exclude = ['phone', 'date','quantity','saleprice','totalAmount','paidAmount','remainingAmount','note','purchase','profit']

class TyreSaleReportFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date", lookup_expr='gte')
	end_date = DateFilter(field_name="date", lookup_expr='lte')
	class Meta:
		model = TyreSale
		fields = '__all__'
		exclude = ['created_date', 'invoiceNo','name','phone','item_name',
                  'date','quantity','saleprice','totalAmount','paidAmount','remainingAmount','note','purchase','profit']

class TyreSaleProfitFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date", lookup_expr='gte')
	end_date = DateFilter(field_name="date", lookup_expr='lte')
	class Meta:
		model = TyreSale
		fields = '__all__'
		exclude = ['account', 'invoiceNo','name','phone','vechile',
                  'date','quantity','saleprice','totalAmount','paidAmount','remainingAmount','note','purchase','profit']