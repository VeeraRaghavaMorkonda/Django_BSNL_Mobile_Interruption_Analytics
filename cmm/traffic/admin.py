from django.contrib import admin
from traffic.models import nsn3g_table,zte3g_table
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(nsn3g_table)
class nsn3g_table_Admin(ImportExportModelAdmin):
    list_display = ('DATE','PLMN_name','RNC_name','WBTS_name','WBTS_ID','WCEL_name','WCEL_ID','RRC_CONN_SUCC_RATE','RRC_Connection_Setup_Completed','RRC_Setup_Attempts','CS_RAB_Setup_Success_Rate','RAB_setup_completed_for_CS_Voice_calls','RAB_Attempts_CS_Voice','R99_stp_SR_Usr','R99_Rab_Succ','R99_Rab_Attempts','HSDPA_stp_SR_Usr','HSDPA_Succ','HSDPA_att','HSUPA_stp_SR_Usr','HSUPA_Rab_Success','HSUPA_Rab_Attempts','Voice_DCR','CS_RAB_Drop_Nom','CS_Rab_Release','R99_PS_DROP_RATE','R99_DROP_COUNT','R99_REL_COUNT','HSDPA_CALL_DROP_RATE','HSDPA_CALL_DROP','HSDPA_CALL_REL','HSUPA_CALL_DROP_RATE','HSUPA_CALL_DROP','HSUPA_CALL_REL','Soft_HO_Success_rate_RT','SUCC_UPDATES_ON_SHO_FOR_RT','Soft_HO_Update_Attempts_RT','Inter_sys_RT_Hard_HOSR','RT_IRAT_SUCC','RT_IRAT_ATT','Inter_sys_NRT_Hard_HOSR','NRT_IRAT_SUCC','NRT_IRAT_ATT','Total_CS_traffic_Erl','NRT_DCH_MACd_throughput_DL','NRT_DCH_MACd_throughput_UL','Average_RTWP','Average_number_of_simultaneous_HSDPA_users','Max_simult_HSDPA_users','Active_HS_DSCH_cell_thr','HSUPA_Datapayload_MB','HSDPA_Payload_MB','Active_HSUPA_cell_thp','CSSR','Video_DCR','PS_Congestion_due_to_CE_3G','PS_Congestion_due_to_IUB_3G','PS_Congestion_due_to_Power_3G')     
    ordering = ('DATE',)    
    search_fields = ('WBTS_name',)


@admin.register(zte3g_table)
class zte3g_table_Admin(ImportExportModelAdmin):
    list_display = ('Date','NodeB_ID','NodeB_Name','Cell_Name','LAC','Local_CellID','RatioofsuccessfulRRCconnectionestablishmentservicerelativ','RatioofsuccessfulRRCconnectionestablishment','NumberofsuccessfulRRCconnectionestablishment','NumberofRRCconnectionestablishmentAttempt','Speech_Setup','Call_Volume','NumberofSPEECHRABestablishmentAttempt','RatioofsuccessfulPSRABestablishment','NumberofSuccessfulPSRABestablishment','NumberofPSRABestablishmentAttempt','RatioofsuccessfulPSRABestablishmentHSDPA','NumberofSuccessfulPSRABestablishmentHSDPA','NumberofPSRABestablishmentAttemptHSDPA','RatioofsuccessfulPSRABestablishmentHSUPA','NumberofSuccessfulPSRABestablishmentHSUPA','NumberofPSRABestablishmentAttemptHSUPA','Call_Drop','NumberofCSCallDropSpeech','NumberofCSSpeechRABRelease','RatioofPSR99CallDrop','CallDropTimesPSR99_1456561709706','NormalReleasePSR99_1456561709706','RatioofPSHSDPACallDrop','NumberofPSCallDropHSDPA','releaseDPA_1456561709706','RatioofPSHSUPACallDrop','NumberofPSCallDropHSUPA','NormalReleaseHSUPA_1456561709706','SoftHandoverSuccessRate','NumberofSuccessfulSHO','NumberofAttemptedSHO','CellInterRATCSOutgoingHandoverSuccessRateWCDMAGSM','InterRATCSOutgoingHandoverSuccessnumberWCDMAGSM','NumberofattemptedoutgoingCSinterRAThandovers','CellInterRATPSOutgoingHandoverSuccessRateWCDMAGPRS','InterRATPSOutgoingHandoverSuccessnumberWCDMAGPRS','InterRATPSOutgoingHandoverAttemptnumberWCDMAGPRS','CellTrafficVolumespeechEr','PSHSDPAtrafficDLThroughputMAC','PSHSUPAtrafficULThroughputMAC','AverageThroughput456561709706','HSDPAAveragethroughputperuserMonitor','AverageCellFreqRTWP','ThebestCellAverageHSDPAUsers','ThebestcellMaximumHSDPAUsers','Total_Data_Volume_in_UL','Total_Data_Volume_in_DL_1456561709706','AverageHSUPAThroughput_1456561546549','CallSetupSuccessrateCSVideotelephone_1456561709706','CS64VideocallRABSSR_1456561709706','dl_data','ul_data')     
    ordering = ('Date',)    
    search_fields = ('NodeB_Name',)


