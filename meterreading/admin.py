from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(MeterReading)

class ViewAdmin(ImportExportModelAdmin):
    pass