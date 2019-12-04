from django.contrib import admin
from tudafaults.models import cfa_bb,cfa_wl
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(cfa_wl)
class cfa_wl_Admin(ImportExportModelAdmin):
    list_display = ('PHONE_NO','NAME','HOUSE_NO','VILLAGE_NAME','ADDITIONAL_DETAILS','CITY','PIN_CODE','SWITCH_CODE','NE','PORT_CARD_SLOT','VERTICAL','PILLAR_IN','PILLAR_OUT','DP_NO','LINEMAN_CODE','JTO_CODE','BB_FLAG','BB_PLAN','LL_PLAN','OS_AMOUNT','OPERATING_STATUS','MOBILE_NO','EMAIL_ID')     
    ordering = ('PHONE_NO',)    
    search_fields = ('PHONE_NO',)



@admin.register(cfa_bb)
class cfa_bb_Admin(ImportExportModelAdmin):
    list_display = ('SSA','EXCHANGE_CODE','PHONE_NO','USER_ID','NW_TYPE','MODEM_TYPE','MODEM_ACQ_TYPE','DSLAM_IP','INNER_VLAN','OUTER_VLAN')     
    ordering = ('PHONE_NO',)    
    search_fields = ('PHONE_NO',)



