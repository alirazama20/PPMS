from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Item, Commission, Expense, Employee,Dealer,Vechile,Rate)

class ViewAdmin(ImportExportModelAdmin):
    pass