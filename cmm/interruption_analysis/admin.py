
from django.contrib import admin
from interruption_analysis.models import interruptions_table
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(interruptions_table)
class InterruptionAdmin(ImportExportModelAdmin):
    list_display = ('RPID','BTS_NAME','BTS_TRF_CAT','SSA','SDCA','CIRCLE','MAKE','TECH','SITE_TYPE','DOWN_DATE','DOWN_TIME','CLEARED_DATE','CLEARED_TIME','REASON','DURATION')     
    ordering = ('-DURATION',)    
    search_fields = ('BTS_NAME',)








