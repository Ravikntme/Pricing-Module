from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Rates)
class RatesAdmin(admin.ModelAdmin):
    list_display=['dbp','tbp']

@admin.register(Timebase)
class TimebaseAdmin(admin.ModelAdmin):
    list_display=['name','variable_tbp']