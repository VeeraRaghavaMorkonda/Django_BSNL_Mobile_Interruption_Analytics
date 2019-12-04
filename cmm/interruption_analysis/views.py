from django.shortcuts import render
from interruption_analysis.models import interruptions_table
from django.db.models import Sum, Value, Count 
from django.db.models.functions import Coalesce



# Create your views here.

def analysis_2g3g(request):


    # Queries & Calculations for BKOTHAKOTA SDCA

    bkk_tot_duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA').aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bkktotal = round(bkk_tot_duration['downtime'],2)
    bkkavg = round(bkktotal / 10, 2)  # BKOTHAKOTA TOWERS

    # BKOTHAKOTA STR OFC BREAKS
    
    bkkstrcnt = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).count()   
    bkkstr_duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bkkstrofc = round(bkkstr_duration['downtime'],2)
    bkkstrofcper = round(bkkstrofc / bkktotal * 100, 2)

    # BKOTHAKOTA SSA OFC BREAKS

    bkkssacnt = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).count()   
    bkkssa_duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bkkssaofc = round(bkkssa_duration['downtime'],2)
    bkkssaofcper = round(bkkssaofc / bkktotal * 100, 2)

    # BKOTHAKOTA BUILTUP FAULTS

    bkkbltcnt = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).count()   
    bkkblt_duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bkkblt = round(bkkblt_duration['downtime'],2)
    bkkbltper = round(bkkblt / bkktotal * 100, 2)

    # BKOTHAKOTA RING FAULTS

    bkkringcnt = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).count()   
    bkkring_duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bkkring = round(bkkring_duration['downtime'],2)
    bkkringper = round(bkkring / bkktotal * 100, 2)

    # BKOTHAKOTA OF EQPT FAULTS

    bkkofeptcnt = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).count()   
    bkkofept_duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bkkofept = round(bkkofept_duration['downtime'],2)
    bkkofeptper = round(bkkofept / bkktotal * 100, 2)

    # BKOTHAKOTA TOTAL OUTAGE DUE TO MEDIA

    bkktotmedia = round(bkkstrofc + bkkssaofc + bkkblt + bkkring + bkkofept, 2)
    bkktotmediaper = round(bkktotmedia / bkktotal * 100, 2)

    # BKOTHAKOTA POWER SUPPLY FAULTS

    bkkpsfcnt = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).count()   
    bkkpsf_duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bkkpsf = round(bkkpsf_duration['downtime'],2)
    bkkpsfper = round(bkkpsf / bkktotal * 100, 2)

    # BKOTHAKOTA POWER PLANT FAULTS

    bkkppfcnt = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).count()   
    bkkppf_duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bkkppf = round(bkkppf_duration['downtime'],2)
    bkkppfper = round(bkkppf / bkktotal * 100, 2)

    # BKOTHAKOTA DG SET FAULTS

    bkkdgcnt = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).count()   
    bkkdg_duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bkkdg = round(bkkdg_duration['downtime'],2)
    bkkdgper = round(bkkdg / bkktotal * 100, 2)

    # BKOTHAKOTA DG START BATTERY FAULTS

    bkkdgbattcnt = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - DG Startup Batt Faulty']).count()   
    bkkdgbatt_duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bkkdgbatt = round(bkkdgbatt_duration['downtime'],2)
    bkkdgbattper = round(bkkdgbatt / bkktotal * 100, 2)

    # BKOTHAKOTA LOW BATTERY BACKUP FAULTS

    bkklbattcnt = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).count()   
    bkklbatt_duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bkklbatt = round(bkklbatt_duration['downtime'],2)
    bkklbattper = round(bkklbatt / bkktotal * 100, 2)

    # BKOTHAKOTA NO DG SET FAULTS

    bkknodgcnt = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - Power Problem ,No DG']).count()   
    bkknodg_duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bkknodg = round(bkknodg_duration['downtime'],2)
    bkknodgper = round(bkknodg / bkktotal * 100, 2)

    # BKOTHAKOTA NO DIESEL FAULTS

    bkknodslcnt = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - Power Problem,No Diesel in D.G']).count()   
    bkknodsl_duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bkknodsl = round(bkknodsl_duration['downtime'],2)
    bkknodslper = round(bkknodsl / bkktotal * 100, 2)

    # BKOTHAKOTA TOTAL OUTAGE DUE TO POWER

    bkktotpwr = round(bkkpsf + bkkppf + bkkdg + bkkdgbatt + bkklbatt + bkknodg + bkknodsl, 2)
    bkktotpwrper = round(bkktotpwr / bkktotal * 100, 2)

    # BKOTHAKOTA HARDWARE FAULTS

    bkkhwbtscnt = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).count()   
    bkkhwbts_duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bkkhwbts = round(bkkhwbts_duration['downtime'],2)
    bkkhwbtsper = round(bkkhwbts / bkktotal * 100, 2)

    # BKOTHAKOTA MISC FAULTS

    bkkmisccnt = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).count()   
    bkkmisc_duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bkkmisc = round(bkkmisc_duration['downtime'],2)
    bkkmiscper = round(bkkmisc / bkktotal * 100, 2)

    # BKOTHAKOTA TOTAL OUTAGE DUE TO HARDWARE & MISC

    bkktothwmisc = round(bkkhwbts + bkkmisc, 2)
    bkktothwmiscper = round(bkktothwmisc / bkktotal * 100, 2)


        # Queries & Calculations for BANGARUPALEM SDCA

    bgp_tot_duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM').aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bgptotal = round(bgp_tot_duration['downtime'],2)
    bgpavg = round(bgptotal / 18, 2)  # BANGARUPALEM TOWERS

    # BANGARUPALEM STR OFC BREAKS
    
    bgpstrcnt = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).count()   
    bgpstr_duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bgpstrofc = round(bgpstr_duration['downtime'],2)
    bgpstrofcper = round(bgpstrofc / bgptotal * 100, 2)

    # BANGARUPALEM SSA OFC BREAKS

    bgpssacnt = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).count()   
    bgpssa_duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bgpssaofc = round(bgpssa_duration['downtime'],2)
    bgpssaofcper = round(bgpssaofc / bgptotal * 100, 2)

    # BANGARUPALEM BUILTUP FAULTS

    bgpbltcnt = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).count()   
    bgpblt_duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bgpblt = round(bgpblt_duration['downtime'],2)
    bgpbltper = round(bgpblt / bgptotal * 100, 2)

    # BANGARUPALEM RING FAULTS

    bgpringcnt = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).count()   
    bgpring_duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bgpring = round(bgpring_duration['downtime'],2)
    bgpringper = round(bgpring / bgptotal * 100, 2)

    # BANGARUPALEM OF EQPT FAULTS

    bgpofeptcnt = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).count()   
    bgpofept_duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bgpofept = round(bgpofept_duration['downtime'],2)
    bgpofeptper = round(bgpofept / bgptotal * 100, 2)

    # BANGARUPALEM TOTAL OUTAGE DUE TO MEDIA

    bgptotmedia = round(bgpstrofc + bgpssaofc + bgpblt + bgpring + bgpofept, 2)
    bgptotmediaper = round(bgptotmedia / bgptotal * 100, 2)

    # BANGARUPALEM POWER SUPPLY FAULTS

    bgppsfcnt = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).count()   
    bgppsf_duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bgppsf = round(bgppsf_duration['downtime'],2)
    bgppsfper = round(bgppsf / bgptotal * 100, 2)

    # BANGARUPALEM POWER PLANT FAULTS

    bgpppfcnt = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).count()   
    bgpppf_duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bgpppf = round(bgpppf_duration['downtime'],2)
    bgpppfper = round(bgpppf / bgptotal * 100, 2)

    # BANGARUPALEM DG SET FAULTS

    bgpdgcnt = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).count()   
    bgpdg_duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bgpdg = round(bgpdg_duration['downtime'],2)
    bgpdgper = round(bgpdg / bgptotal * 100, 2)

    # BANGARUPALEM DG START BATTERY FAULTS

    bgpdgbattcnt = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - DG Startup Batt Faulty']).count()   
    bgpdgbatt_duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bgpdgbatt = round(bgpdgbatt_duration['downtime'],2)
    bgpdgbattper = round(bgpdgbatt / bgptotal * 100, 2)

    # BANGARUPALEM LOW BATTERY BACKUP FAULTS

    bgplbattcnt = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).count()   
    bgplbatt_duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bgplbatt = round(bgplbatt_duration['downtime'],2)
    bgplbattper = round(bgplbatt / bgptotal * 100, 2)

    # BANGARUPALEM NO DG SET FAULTS

    bgpnodgcnt = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - Power Problem ,No DG']).count()   
    bgpnodg_duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bgpnodg = round(bgpnodg_duration['downtime'],2)
    bgpnodgper = round(bgpnodg / bgptotal * 100, 2)

    # BANGARUPALEM NO DIESEL FAULTS

    bgpnodslcnt = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - Power Problem,No Diesel in D.G']).count()   
    bgpnodsl_duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bgpnodsl = round(bgpnodsl_duration['downtime'],2)
    bgpnodslper = round(bgpnodsl / bgptotal * 100, 2)

    # BANGARUPALEM TOTAL OUTAGE DUE TO POWER

    bgptotpwr = round(bgppsf + bgpppf + bgpdg + bgpdgbatt + bgplbatt + bgpnodg + bgpnodsl, 2)
    bgptotpwrper = round(bgptotpwr / bgptotal * 100, 2)

    # BANGARUPALEM HARDWARE FAULTS

    bgphwbtscnt = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).count()   
    bgphwbts_duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bgphwbts = round(bgphwbts_duration['downtime'],2)
    bgphwbtsper = round(bgphwbts / bgptotal * 100, 2)

    # BANGARUPALEM MISC FAULTS

    bgpmisccnt = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).count()   
    bgpmisc_duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    bgpmisc = round(bgpmisc_duration['downtime'],2)
    bgpmiscper = round(bgpmisc / bgptotal * 100, 2)

    # BANGARUPALEM TOTAL OUTAGE DUE TO HARDWARE & MISC

    bgptothwmisc = round(bgphwbts + bgpmisc, 2)
    bgptothwmiscper = round(bgptothwmisc / bgptotal * 100, 2)


        # Queries & Calculations for CHANDRAGIRI SDCA

    cdr_tot_duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI').aggregate(downtime=Coalesce(Sum('DURATION'),0))
    cdrtotal = round(cdr_tot_duration['downtime'],2)
    cdravg = round(cdrtotal / 155, 2)  # CHANDRAGIRI TOWERS

    # CHANDRAGIRI STR OFC BREAKS
    
    cdrstrcnt = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).count()   
    cdrstr_duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    cdrstrofc = round(cdrstr_duration['downtime'],2)
    cdrstrofcper = round(cdrstrofc / cdrtotal * 100, 2)

    # CHANDRAGIRI SSA OFC BREAKS

    cdrssacnt = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).count()   
    cdrssa_duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    cdrssaofc = round(cdrssa_duration['downtime'],2)
    cdrssaofcper = round(cdrssaofc / cdrtotal * 100, 2)

    # CHANDRAGIRI BUILTUP FAULTS

    cdrbltcnt = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).count()   
    cdrblt_duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    cdrblt = round(cdrblt_duration['downtime'],2)
    cdrbltper = round(cdrblt / cdrtotal * 100, 2)

    # CHANDRAGIRI RING FAULTS

    cdrringcnt = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).count()   
    cdrring_duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    cdrring = round(cdrring_duration['downtime'],2)
    cdrringper = round(cdrring / cdrtotal * 100, 2)

    # CHANDRAGIRI OF EQPT FAULTS

    cdrofeptcnt = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).count()   
    cdrofept_duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    cdrofept = round(cdrofept_duration['downtime'],2)
    cdrofeptper = round(cdrofept / cdrtotal * 100, 2)

    # CHANDRAGIRI TOTAL OUTAGE DUE TO MEDIA

    cdrtotmedia = round(cdrstrofc + cdrssaofc + cdrblt + cdrring + cdrofept, 2)
    cdrtotmediaper = round(cdrtotmedia / cdrtotal * 100, 2)

    # CHANDRAGIRI POWER SUPPLY FAULTS

    cdrpsfcnt = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).count()   
    cdrpsf_duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    cdrpsf = round(cdrpsf_duration['downtime'],2)
    cdrpsfper = round(cdrpsf / cdrtotal * 100, 2)

    # CHANDRAGIRI POWER PLANT FAULTS

    cdrppfcnt = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).count()   
    cdrppf_duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    cdrppf = round(cdrppf_duration['downtime'],2)
    cdrppfper = round(cdrppf / cdrtotal * 100, 2)

    # CHANDRAGIRI DG SET FAULTS

    cdrdgcnt = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).count()   
    cdrdg_duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    cdrdg = round(cdrdg_duration['downtime'],2)
    cdrdgper = round(cdrdg / cdrtotal * 100, 2)

    # CHANDRAGIRI DG START BATTERY FAULTS

    cdrdgbattcnt = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - DG Startup Batt Faulty']).count()   
    cdrdgbatt_duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    cdrdgbatt = round(cdrdgbatt_duration['downtime'],2)
    cdrdgbattper = round(cdrdgbatt / cdrtotal * 100, 2)

    # CHANDRAGIRI LOW BATTERY BACKUP FAULTS

    cdrlbattcnt = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).count()   
    cdrlbatt_duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    cdrlbatt = round(cdrlbatt_duration['downtime'],2)
    cdrlbattper = round(cdrlbatt / cdrtotal * 100, 2)

    # CHANDRAGIRI NO DG SET FAULTS

    cdrnodgcnt = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - Power Problem ,No DG']).count()   
    cdrnodg_duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    cdrnodg = round(cdrnodg_duration['downtime'],2)
    cdrnodgper = round(cdrnodg / cdrtotal * 100, 2)

    # CHANDRAGIRI NO DIESEL FAULTS

    cdrnodslcnt = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - Power Problem,No Diesel in D.G']).count()   
    cdrnodsl_duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    cdrnodsl = round(cdrnodsl_duration['downtime'],2)
    cdrnodslper = round(cdrnodsl / cdrtotal * 100, 2)

    # CHANDRAGIRI TOTAL OUTAGE DUE TO POWER

    cdrtotpwr = round(cdrpsf + cdrppf + cdrdg + cdrdgbatt + cdrlbatt + cdrnodg + cdrnodsl, 2)
    cdrtotpwrper = round(cdrtotpwr / cdrtotal * 100, 2)

    # CHANDRAGIRI HARDWARE FAULTS

    cdrhwbtscnt = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).count()   
    cdrhwbts_duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    cdrhwbts = round(cdrhwbts_duration['downtime'],2)
    cdrhwbtsper = round(cdrhwbts / cdrtotal * 100, 2)

    # CHANDRAGIRI MISC FAULTS

    cdrmisccnt = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).count()   
    cdrmisc_duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    cdrmisc = round(cdrmisc_duration['downtime'],2)
    cdrmiscper = round(cdrmisc / cdrtotal * 100, 2)

    # CHANDRAGIRI TOTAL OUTAGE DUE TO HARDWARE & MISC

    cdrtothwmisc = round(cdrhwbts + cdrmisc, 2)
    cdrtothwmiscper = round(cdrtothwmisc / cdrtotal * 100, 2)

        # Queries & Calculations for CHITTOOR SDCA

    ctr_tot_duration = interruptions_table.objects.filter(SDCA='CHITTOOR').aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ctrtotal = round(ctr_tot_duration['downtime'],2)
    ctravg = round(ctrtotal / 92, 2)  # CHITTOOR TOWERS

    # CHITTOOR STR OFC BREAKS
    
    ctrstrcnt = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).count()   
    ctrstr_duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ctrstrofc = round(ctrstr_duration['downtime'],2)
    ctrstrofcper = round(ctrstrofc / ctrtotal * 100, 2)

    # CHITTOOR SSA OFC BREAKS

    ctrssacnt = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).count()   
    ctrssa_duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ctrssaofc = round(ctrssa_duration['downtime'],2)
    ctrssaofcper = round(ctrssaofc / ctrtotal * 100, 2)

    # CHITTOOR BUILTUP FAULTS

    ctrbltcnt = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).count()   
    ctrblt_duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ctrblt = round(ctrblt_duration['downtime'],2)
    ctrbltper = round(ctrblt / ctrtotal * 100, 2)

    # CHITTOOR RING FAULTS

    ctrringcnt = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).count()   
    ctrring_duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ctrring = round(ctrring_duration['downtime'],2)
    ctrringper = round(ctrring / ctrtotal * 100, 2)

    # CHITTOOR OF EQPT FAULTS

    ctrofeptcnt = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).count()   
    ctrofept_duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ctrofept = round(ctrofept_duration['downtime'],2)
    ctrofeptper = round(ctrofept / ctrtotal * 100, 2)

    # CHITTOOR TOTAL OUTAGE DUE TO MEDIA

    ctrtotmedia = round(ctrstrofc + ctrssaofc + ctrblt + ctrring + ctrofept, 2)
    ctrtotmediaper = round(ctrtotmedia / ctrtotal * 100, 2)

    # CHITTOOR POWER SUPPLY FAULTS

    ctrpsfcnt = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).count()   
    ctrpsf_duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ctrpsf = round(ctrpsf_duration['downtime'],2)
    ctrpsfper = round(ctrpsf / ctrtotal * 100, 2)

    # CHITTOOR POWER PLANT FAULTS

    ctrppfcnt = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).count()   
    ctrppf_duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ctrppf = round(ctrppf_duration['downtime'],2)
    ctrppfper = round(ctrppf / ctrtotal * 100, 2)

    # CHITTOOR DG SET FAULTS

    ctrdgcnt = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).count()   
    ctrdg_duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ctrdg = round(ctrdg_duration['downtime'],2)
    ctrdgper = round(ctrdg / ctrtotal * 100, 2)

    # CHITTOOR DG START BATTERY FAULTS

    ctrdgbattcnt = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - DG Startup Batt Faulty']).count()   
    ctrdgbatt_duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ctrdgbatt = round(ctrdgbatt_duration['downtime'],2)
    ctrdgbattper = round(ctrdgbatt / ctrtotal * 100, 2)

    # CHITTOOR LOW BATTERY BACKUP FAULTS

    ctrlbattcnt = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).count()   
    ctrlbatt_duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ctrlbatt = round(ctrlbatt_duration['downtime'],2)
    ctrlbattper = round(ctrlbatt / ctrtotal * 100, 2)

    # CHITTOOR NO DG SET FAULTS

    ctrnodgcnt = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - Power Problem ,No DG']).count()   
    ctrnodg_duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ctrnodg = round(ctrnodg_duration['downtime'],2)
    ctrnodgper = round(ctrnodg / ctrtotal * 100, 2)

    # CHITTOOR NO DIESEL FAULTS

    ctrnodslcnt = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - Power Problem,No Diesel in D.G']).count()   
    ctrnodsl_duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ctrnodsl = round(ctrnodsl_duration['downtime'],2)
    ctrnodslper = round(ctrnodsl / ctrtotal * 100, 2)

    # CHITTOOR TOTAL OUTAGE DUE TO POWER

    ctrtotpwr = round(ctrpsf + ctrppf + ctrdg + ctrdgbatt + ctrlbatt + ctrnodg + ctrnodsl, 2)
    ctrtotpwrper = round(ctrtotpwr / ctrtotal * 100, 2)

    # CHITTOOR HARDWARE FAULTS

    ctrhwbtscnt = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).count()   
    ctrhwbts_duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ctrhwbts = round(ctrhwbts_duration['downtime'],2)
    ctrhwbtsper = round(ctrhwbts / ctrtotal * 100, 2)

    # CHITTOOR MISC FAULTS

    ctrmisccnt = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).count()   
    ctrmisc_duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ctrmisc = round(ctrmisc_duration['downtime'],2)
    ctrmiscper = round(ctrmisc / ctrtotal * 100, 2)

    # CHITTOOR TOTAL OUTAGE DUE TO HARDWARE & MISC

    ctrtothwmisc = round(ctrhwbts + ctrmisc, 2)
    ctrtothwmiscper = round(ctrtothwmisc / ctrtotal * 100, 2)

        # Queries & Calculations for KUPPAM SDCA

    kup_tot_duration = interruptions_table.objects.filter(SDCA='KUPPAM').aggregate(downtime=Coalesce(Sum('DURATION'),0))
    kuptotal = round(kup_tot_duration['downtime'],2)
    kupavg = round(kuptotal / 22, 2)  # KUPPAM TOWERS

    # KUPPAM STR OFC BREAKS
    
    kupstrcnt = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).count()   
    kupstr_duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    kupstrofc = round(kupstr_duration['downtime'],2)
    kupstrofcper = round(kupstrofc / kuptotal * 100, 2)

    # KUPPAM SSA OFC BREAKS

    kupssacnt = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).count()   
    kupssa_duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    kupssaofc = round(kupssa_duration['downtime'],2)
    kupssaofcper = round(kupssaofc / kuptotal * 100, 2)

    # KUPPAM BUILTUP FAULTS

    kupbltcnt = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).count()   
    kupblt_duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    kupblt = round(kupblt_duration['downtime'],2)
    kupbltper = round(kupblt / kuptotal * 100, 2)

    # KUPPAM RING FAULTS

    kupringcnt = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).count()   
    kupring_duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    kupring = round(kupring_duration['downtime'],2)
    kupringper = round(kupring / kuptotal * 100, 2)

    # KUPPAM OF EQPT FAULTS

    kupofeptcnt = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).count()   
    kupofept_duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    kupofept = round(kupofept_duration['downtime'],2)
    kupofeptper = round(kupofept / kuptotal * 100, 2)

    # KUPPAM TOTAL OUTAGE DUE TO MEDIA

    kuptotmedia = round(kupstrofc + kupssaofc + kupblt + kupring + kupofept, 2)
    kuptotmediaper = round(kuptotmedia / kuptotal * 100, 2)

    # KUPPAM POWER SUPPLY FAULTS

    kuppsfcnt = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).count()   
    kuppsf_duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    kuppsf = round(kuppsf_duration['downtime'],2)
    kuppsfper = round(kuppsf / kuptotal * 100, 2)

    # KUPPAM POWER PLANT FAULTS

    kupppfcnt = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).count()   
    kupppf_duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    kupppf = round(kupppf_duration['downtime'],2)
    kupppfper = round(kupppf / kuptotal * 100, 2)

    # KUPPAM DG SET FAULTS

    kupdgcnt = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).count()   
    kupdg_duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    kupdg = round(kupdg_duration['downtime'],2)
    kupdgper = round(kupdg / kuptotal * 100, 2)

    # KUPPAM DG START BATTERY FAULTS

    kupdgbattcnt = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - DG Startup Batt Faulty']).count()   
    kupdgbatt_duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    kupdgbatt = round(kupdgbatt_duration['downtime'],2)
    kupdgbattper = round(kupdgbatt / kuptotal * 100, 2)

    # KUPPAM LOW BATTERY BACKUP FAULTS

    kuplbattcnt = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).count()   
    kuplbatt_duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    kuplbatt = round(kuplbatt_duration['downtime'],2)
    kuplbattper = round(kuplbatt / kuptotal * 100, 2)

    # KUPPAM NO DG SET FAULTS

    kupnodgcnt = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - Power Problem ,No DG']).count()   
    kupnodg_duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    kupnodg = round(kupnodg_duration['downtime'],2)
    kupnodgper = round(kupnodg / kuptotal * 100, 2)

    # KUPPAM NO DIESEL FAULTS

    kupnodslcnt = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - Power Problem,No Diesel in D.G']).count()   
    kupnodsl_duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    kupnodsl = round(kupnodsl_duration['downtime'],2)
    kupnodslper = round(kupnodsl / kuptotal * 100, 2)

    # KUPPAM TOTAL OUTAGE DUE TO POWER

    kuptotpwr = round(kuppsf + kupppf + kupdg + kupdgbatt + kuplbatt + kupnodg + kupnodsl, 2)
    kuptotpwrper = round(kuptotpwr / kuptotal * 100, 2)

    # KUPPAM HARDWARE FAULTS

    kuphwbtscnt = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).count()   
    kuphwbts_duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    kuphwbts = round(kuphwbts_duration['downtime'],2)
    kuphwbtsper = round(kuphwbts / kuptotal * 100, 2)

    # KUPPAM MISC FAULTS

    kupmisccnt = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).count()   
    kupmisc_duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    kupmisc = round(kupmisc_duration['downtime'],2)
    kupmiscper = round(kupmisc / kuptotal * 100, 2)

    # KUPPAM TOTAL OUTAGE DUE TO HARDWARE & MISC

    kuptothwmisc = round(kuphwbts + kupmisc, 2)
    kuptothwmiscper = round(kuptothwmisc / kuptotal * 100, 2)

        # Queries & Calculations for MADANAPALLI SDCA

    mdp_tot_duration = interruptions_table.objects.filter(SDCA='MADANAPALLI').aggregate(downtime=Coalesce(Sum('DURATION'),0))
    mdptotal = round(mdp_tot_duration['downtime'],2)
    mdpavg = round(mdptotal / 68, 2)  # MADANAPALLI TOWERS

    # MADANAPALLI STR OFC BREAKS
    
    mdpstrcnt = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).count()   
    mdpstr_duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    mdpstrofc = round(mdpstr_duration['downtime'],2)
    mdpstrofcper = round(mdpstrofc / mdptotal * 100, 2)

    # MADANAPALLI SSA OFC BREAKS

    mdpssacnt = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).count()   
    mdpssa_duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    mdpssaofc = round(mdpssa_duration['downtime'],2)
    mdpssaofcper = round(mdpssaofc / mdptotal * 100, 2)

    # MADANAPALLI BUILTUP FAULTS

    mdpbltcnt = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).count()   
    mdpblt_duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    mdpblt = round(mdpblt_duration['downtime'],2)
    mdpbltper = round(mdpblt / mdptotal * 100, 2)

    # MADANAPALLI RING FAULTS

    mdpringcnt = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).count()   
    mdpring_duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    mdpring = round(mdpring_duration['downtime'],2)
    mdpringper = round(mdpring / mdptotal * 100, 2)

    # MADANAPALLI OF EQPT FAULTS

    mdpofeptcnt = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).count()   
    mdpofept_duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    mdpofept = round(mdpofept_duration['downtime'],2)
    mdpofeptper = round(mdpofept / mdptotal * 100, 2)

    # MADANAPALLI TOTAL OUTAGE DUE TO MEDIA

    mdptotmedia = round(mdpstrofc + mdpssaofc + mdpblt + mdpring + mdpofept, 2)
    mdptotmediaper = round(mdptotmedia / mdptotal * 100, 2)

    # MADANAPALLI POWER SUPPLY FAULTS

    mdppsfcnt = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).count()   
    mdppsf_duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    mdppsf = round(mdppsf_duration['downtime'],2)
    mdppsfper = round(mdppsf / mdptotal * 100, 2)

    # MADANAPALLI POWER PLANT FAULTS

    mdpppfcnt = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).count()   
    mdpppf_duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    mdpppf = round(mdpppf_duration['downtime'],2)
    mdpppfper = round(mdpppf / mdptotal * 100, 2)

    # MADANAPALLI DG SET FAULTS

    mdpdgcnt = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).count()   
    mdpdg_duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    mdpdg = round(mdpdg_duration['downtime'],2)
    mdpdgper = round(mdpdg / mdptotal * 100, 2)

    # MADANAPALLI DG START BATTERY FAULTS

    mdpdgbattcnt = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - DG Startup Batt Faulty']).count()   
    mdpdgbatt_duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    mdpdgbatt = round(mdpdgbatt_duration['downtime'],2)
    mdpdgbattper = round(mdpdgbatt / mdptotal * 100, 2)

    # MADANAPALLI LOW BATTERY BACKUP FAULTS

    mdplbattcnt = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).count()   
    mdplbatt_duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    mdplbatt = round(mdplbatt_duration['downtime'],2)
    mdplbattper = round(mdplbatt / mdptotal * 100, 2)

    # MADANAPALLI NO DG SET FAULTS

    mdpnodgcnt = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - Power Problem ,No DG']).count()   
    mdpnodg_duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    mdpnodg = round(mdpnodg_duration['downtime'],2)
    mdpnodgper = round(mdpnodg / mdptotal * 100, 2)

    # MADANAPALLI NO DIESEL FAULTS

    mdpnodslcnt = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - Power Problem,No Diesel in D.G']).count()   
    mdpnodsl_duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    mdpnodsl = round(mdpnodsl_duration['downtime'],2)
    mdpnodslper = round(mdpnodsl / mdptotal * 100, 2)

    # MADANAPALLI TOTAL OUTAGE DUE TO POWER

    mdptotpwr = round(mdppsf + mdpppf + mdpdg + mdpdgbatt + mdplbatt + mdpnodg + mdpnodsl, 2)
    mdptotpwrper = round(mdptotpwr / mdptotal * 100, 2)

    # MADANAPALLI HARDWARE FAULTS

    mdphwbtscnt = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).count()   
    mdphwbts_duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    mdphwbts = round(mdphwbts_duration['downtime'],2)
    mdphwbtsper = round(mdphwbts / mdptotal * 100, 2)

    # MADANAPALLI MISC FAULTS

    mdpmisccnt = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).count()   
    mdpmisc_duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    mdpmisc = round(mdpmisc_duration['downtime'],2)
    mdpmiscper = round(mdpmisc / mdptotal * 100, 2)

    # MADANAPALLI TOTAL OUTAGE DUE TO HARDWARE & MISC

    mdptothwmisc = round(mdphwbts + mdpmisc, 2)
    mdptothwmiscper = round(mdptothwmisc / mdptotal * 100, 2)

        # Queries & Calculations for PAKALA SDCA

    pak_tot_duration = interruptions_table.objects.filter(SDCA='PAKALA').aggregate(downtime=Coalesce(Sum('DURATION'),0))
    paktotal = round(pak_tot_duration['downtime'],2)
    pakavg = round(paktotal / 23, 2)  # PAKALA TOWERS

    # PAKALA STR OFC BREAKS
    
    pakstrcnt = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).count()   
    pakstr_duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pakstrofc = round(pakstr_duration['downtime'],2)
    pakstrofcper = round(pakstrofc / paktotal * 100, 2)

    # PAKALA SSA OFC BREAKS

    pakssacnt = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).count()   
    pakssa_duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pakssaofc = round(pakssa_duration['downtime'],2)
    pakssaofcper = round(pakssaofc / paktotal * 100, 2)

    # PAKALA BUILTUP FAULTS

    pakbltcnt = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).count()   
    pakblt_duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pakblt = round(pakblt_duration['downtime'],2)
    pakbltper = round(pakblt / paktotal * 100, 2)

    # PAKALA RING FAULTS

    pakringcnt = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).count()   
    pakring_duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pakring = round(pakring_duration['downtime'],2)
    pakringper = round(pakring / paktotal * 100, 2)

    # PAKALA OF EQPT FAULTS

    pakofeptcnt = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).count()   
    pakofept_duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pakofept = round(pakofept_duration['downtime'],2)
    pakofeptper = round(pakofept / paktotal * 100, 2)

    # PAKALA TOTAL OUTAGE DUE TO MEDIA

    paktotmedia = round(pakstrofc + pakssaofc + pakblt + pakring + pakofept, 2)
    paktotmediaper = round(paktotmedia / paktotal * 100, 2)

    # PAKALA POWER SUPPLY FAULTS

    pakpsfcnt = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).count()   
    pakpsf_duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pakpsf = round(pakpsf_duration['downtime'],2)
    pakpsfper = round(pakpsf / paktotal * 100, 2)

    # PAKALA POWER PLANT FAULTS

    pakppfcnt = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).count()   
    pakppf_duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pakppf = round(pakppf_duration['downtime'],2)
    pakppfper = round(pakppf / paktotal * 100, 2)

    # PAKALA DG SET FAULTS

    pakdgcnt = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).count()   
    pakdg_duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pakdg = round(pakdg_duration['downtime'],2)
    pakdgper = round(pakdg / paktotal * 100, 2)

    # PAKALA DG START BATTERY FAULTS

    pakdgbattcnt = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - DG Startup Batt Faulty']).count()   
    pakdgbatt_duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pakdgbatt = round(pakdgbatt_duration['downtime'],2)
    pakdgbattper = round(pakdgbatt / paktotal * 100, 2)

    # PAKALA LOW BATTERY BACKUP FAULTS

    paklbattcnt = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).count()   
    paklbatt_duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    paklbatt = round(paklbatt_duration['downtime'],2)
    paklbattper = round(paklbatt / paktotal * 100, 2)

    # PAKALA NO DG SET FAULTS

    paknodgcnt = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - Power Problem ,No DG']).count()   
    paknodg_duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    paknodg = round(paknodg_duration['downtime'],2)
    paknodgper = round(paknodg / paktotal * 100, 2)

    # PAKALA NO DIESEL FAULTS

    paknodslcnt = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - Power Problem,No Diesel in D.G']).count()   
    paknodsl_duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    paknodsl = round(paknodsl_duration['downtime'],2)
    paknodslper = round(paknodsl / paktotal * 100, 2)

    # PAKALA TOTAL OUTAGE DUE TO POWER

    paktotpwr = round(pakpsf + pakppf + pakdg + pakdgbatt + paklbatt + paknodg + paknodsl, 2)
    paktotpwrper = round(paktotpwr / paktotal * 100, 2)

    # PAKALA HARDWARE FAULTS

    pakhwbtscnt = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).count()   
    pakhwbts_duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pakhwbts = round(pakhwbts_duration['downtime'],2)
    pakhwbtsper = round(pakhwbts / paktotal * 100, 2)

    # PAKALA MISC FAULTS

    pakmisccnt = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).count()   
    pakmisc_duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pakmisc = round(pakmisc_duration['downtime'],2)
    pakmiscper = round(pakmisc / paktotal * 100, 2)

    # PAKALA TOTAL OUTAGE DUE TO HARDWARE & MISC

    paktothwmisc = round(pakhwbts + pakmisc, 2)
    paktothwmiscper = round(paktothwmisc / paktotal * 100, 2)

        # Queries & Calculations for PALAMANER SDCA

    plm_tot_duration = interruptions_table.objects.filter(SDCA='PALAMANER').aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plmtotal = round(plm_tot_duration['downtime'],2)
    plmavg = round(plmtotal / 22, 2)  # PALAMANER TOWERS

    # PALAMANER STR OFC BREAKS
    
    plmstrcnt = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).count()   
    plmstr_duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plmstrofc = round(plmstr_duration['downtime'],2)
    plmstrofcper = round(plmstrofc / plmtotal * 100, 2)

    # PALAMANER SSA OFC BREAKS

    plmssacnt = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).count()   
    plmssa_duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plmssaofc = round(plmssa_duration['downtime'],2)
    plmssaofcper = round(plmssaofc / plmtotal * 100, 2)

    # PALAMANER BUILTUP FAULTS

    plmbltcnt = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).count()   
    plmblt_duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plmblt = round(plmblt_duration['downtime'],2)
    plmbltper = round(plmblt / plmtotal * 100, 2)

    # PALAMANER RING FAULTS

    plmringcnt = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).count()   
    plmring_duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plmring = round(plmring_duration['downtime'],2)
    plmringper = round(plmring / plmtotal * 100, 2)

    # PALAMANER OF EQPT FAULTS

    plmofeptcnt = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).count()   
    plmofept_duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plmofept = round(plmofept_duration['downtime'],2)
    plmofeptper = round(plmofept / plmtotal * 100, 2)

    # PALAMANER TOTAL OUTAGE DUE TO MEDIA

    plmtotmedia = round(plmstrofc + plmssaofc + plmblt + plmring + plmofept, 2)
    plmtotmediaper = round(plmtotmedia / plmtotal * 100, 2)

    # PALAMANER POWER SUPPLY FAULTS

    plmpsfcnt = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).count()   
    plmpsf_duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plmpsf = round(plmpsf_duration['downtime'],2)
    plmpsfper = round(plmpsf / plmtotal * 100, 2)

    # PALAMANER POWER PLANT FAULTS

    plmppfcnt = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).count()   
    plmppf_duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plmppf = round(plmppf_duration['downtime'],2)
    plmppfper = round(plmppf / plmtotal * 100, 2)

    # PALAMANER DG SET FAULTS

    plmdgcnt = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).count()   
    plmdg_duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plmdg = round(plmdg_duration['downtime'],2)
    plmdgper = round(plmdg / plmtotal * 100, 2)

    # PALAMANER DG START BATTERY FAULTS

    plmdgbattcnt = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - DG Startup Batt Faulty']).count()   
    plmdgbatt_duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plmdgbatt = round(plmdgbatt_duration['downtime'],2)
    plmdgbattper = round(plmdgbatt / plmtotal * 100, 2)

    # PALAMANER LOW BATTERY BACKUP FAULTS

    plmlbattcnt = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).count()   
    plmlbatt_duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plmlbatt = round(plmlbatt_duration['downtime'],2)
    plmlbattper = round(plmlbatt / plmtotal * 100, 2)

    # PALAMANER NO DG SET FAULTS

    plmnodgcnt = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - Power Problem ,No DG']).count()   
    plmnodg_duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plmnodg = round(plmnodg_duration['downtime'],2)
    plmnodgper = round(plmnodg / plmtotal * 100, 2)

    # PALAMANER NO DIESEL FAULTS

    plmnodslcnt = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - Power Problem,No Diesel in D.G']).count()   
    plmnodsl_duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plmnodsl = round(plmnodsl_duration['downtime'],2)
    plmnodslper = round(plmnodsl / plmtotal * 100, 2)

    # PALAMANER TOTAL OUTAGE DUE TO POWER

    plmtotpwr = round(plmpsf + plmppf + plmdg + plmdgbatt + plmlbatt + plmnodg + plmnodsl, 2)
    plmtotpwrper = round(plmtotpwr / plmtotal * 100, 2)

    # PALAMANER HARDWARE FAULTS

    plmhwbtscnt = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).count()   
    plmhwbts_duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plmhwbts = round(plmhwbts_duration['downtime'],2)
    plmhwbtsper = round(plmhwbts / plmtotal * 100, 2)

    # PALAMANER MISC FAULTS

    plmmisccnt = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).count()   
    plmmisc_duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plmmisc = round(plmmisc_duration['downtime'],2)
    plmmiscper = round(plmmisc / plmtotal * 100, 2)

    # PALAMANER TOTAL OUTAGE DUE TO HARDWARE & MISC

    plmtothwmisc = round(plmhwbts + plmmisc, 2)
    plmtothwmiscper = round(plmtothwmisc / plmtotal * 100, 2)

        # Queries & Calculations for PILER SDCA

    plr_tot_duration = interruptions_table.objects.filter(SDCA='PILER').aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plrtotal = round(plr_tot_duration['downtime'],2)
    plravg = round(plrtotal / 38, 2)  # PILER TOWERS

    # PILER STR OFC BREAKS
    
    plrstrcnt = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).count()   
    plrstr_duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plrstrofc = round(plrstr_duration['downtime'],2)
    plrstrofcper = round(plrstrofc / plrtotal * 100, 2)

    # PILER SSA OFC BREAKS

    plrssacnt = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).count()   
    plrssa_duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plrssaofc = round(plrssa_duration['downtime'],2)
    plrssaofcper = round(plrssaofc / plrtotal * 100, 2)

    # PILER BUILTUP FAULTS

    plrbltcnt = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).count()   
    plrblt_duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plrblt = round(plrblt_duration['downtime'],2)
    plrbltper = round(plrblt / plrtotal * 100, 2)

    # PILER RING FAULTS

    plrringcnt = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).count()   
    plrring_duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plrring = round(plrring_duration['downtime'],2)
    plrringper = round(plrring / plrtotal * 100, 2)

    # PILER OF EQPT FAULTS

    plrofeptcnt = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).count()   
    plrofept_duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plrofept = round(plrofept_duration['downtime'],2)
    plrofeptper = round(plrofept / plrtotal * 100, 2)

    # PILER TOTAL OUTAGE DUE TO MEDIA

    plrtotmedia = round(plrstrofc + plrssaofc + plrblt + plrring + plrofept, 2)
    plrtotmediaper = round(plrtotmedia / plrtotal * 100, 2)

    # PILER POWER SUPPLY FAULTS

    plrpsfcnt = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).count()   
    plrpsf_duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plrpsf = round(plrpsf_duration['downtime'],2)
    plrpsfper = round(plrpsf / plrtotal * 100, 2)

    # PILER POWER PLANT FAULTS

    plrppfcnt = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).count()   
    plrppf_duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plrppf = round(plrppf_duration['downtime'],2)
    plrppfper = round(plrppf / plrtotal * 100, 2)

    # PILER DG SET FAULTS

    plrdgcnt = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).count()   
    plrdg_duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plrdg = round(plrdg_duration['downtime'],2)
    plrdgper = round(plrdg / plrtotal * 100, 2)

    # PILER DG START BATTERY FAULTS

    plrdgbattcnt = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - DG Startup Batt Faulty']).count()   
    plrdgbatt_duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plrdgbatt = round(plrdgbatt_duration['downtime'],2)
    plrdgbattper = round(plrdgbatt / plrtotal * 100, 2)

    # PILER LOW BATTERY BACKUP FAULTS

    plrlbattcnt = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).count()   
    plrlbatt_duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plrlbatt = round(plrlbatt_duration['downtime'],2)
    plrlbattper = round(plrlbatt / plrtotal * 100, 2)

    # PILER NO DG SET FAULTS

    plrnodgcnt = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - Power Problem ,No DG']).count()   
    plrnodg_duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plrnodg = round(plrnodg_duration['downtime'],2)
    plrnodgper = round(plrnodg / plrtotal * 100, 2)

    # PILER NO DIESEL FAULTS

    plrnodslcnt = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - Power Problem,No Diesel in D.G']).count()   
    plrnodsl_duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plrnodsl = round(plrnodsl_duration['downtime'],2)
    plrnodslper = round(plrnodsl / plrtotal * 100, 2)

    # PILER TOTAL OUTAGE DUE TO POWER

    plrtotpwr = round(plrpsf + plrppf + plrdg + plrdgbatt + plrlbatt + plrnodg + plrnodsl, 2)
    plrtotpwrper = round(plrtotpwr / plrtotal * 100, 2)

    # PILER HARDWARE FAULTS

    plrhwbtscnt = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).count()   
    plrhwbts_duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plrhwbts = round(plrhwbts_duration['downtime'],2)
    plrhwbtsper = round(plrhwbts / plrtotal * 100, 2)

    # PILER MISC FAULTS

    plrmisccnt = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).count()   
    plrmisc_duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    plrmisc = round(plrmisc_duration['downtime'],2)
    plrmiscper = round(plrmisc / plrtotal * 100, 2)

    # PILER TOTAL OUTAGE DUE TO HARDWARE & MISC

    plrtothwmisc = round(plrhwbts + plrmisc, 2)
    plrtothwmiscper = round(plrtothwmisc / plrtotal * 100, 2)

        # Queries & Calculations for PUNGANUR SDCA

    pgr_tot_duration = interruptions_table.objects.filter(SDCA='PUNGANUR').aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pgrtotal = round(pgr_tot_duration['downtime'],2)
    pgravg = round(pgrtotal / 26, 2)  # PUNGANUR TOWERS

    # PUNGANUR STR OFC BREAKS
    
    pgrstrcnt = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).count()   
    pgrstr_duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pgrstrofc = round(pgrstr_duration['downtime'],2)
    pgrstrofcper = round(pgrstrofc / pgrtotal * 100, 2)

    # PUNGANUR SSA OFC BREAKS

    pgrssacnt = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).count()   
    pgrssa_duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pgrssaofc = round(pgrssa_duration['downtime'],2)
    pgrssaofcper = round(pgrssaofc / pgrtotal * 100, 2)

    # PUNGANUR BUILTUP FAULTS

    pgrbltcnt = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).count()   
    pgrblt_duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pgrblt = round(pgrblt_duration['downtime'],2)
    pgrbltper = round(pgrblt / pgrtotal * 100, 2)

    # PUNGANUR RING FAULTS

    pgrringcnt = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).count()   
    pgrring_duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pgrring = round(pgrring_duration['downtime'],2)
    pgrringper = round(pgrring / pgrtotal * 100, 2)

    # PUNGANUR OF EQPT FAULTS

    pgrofeptcnt = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).count()   
    pgrofept_duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pgrofept = round(pgrofept_duration['downtime'],2)
    pgrofeptper = round(pgrofept / pgrtotal * 100, 2)

    # PUNGANUR TOTAL OUTAGE DUE TO MEDIA

    pgrtotmedia = round(pgrstrofc + pgrssaofc + pgrblt + pgrring + pgrofept, 2)
    pgrtotmediaper = round(pgrtotmedia / pgrtotal * 100, 2)

    # PUNGANUR POWER SUPPLY FAULTS

    pgrpsfcnt = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).count()   
    pgrpsf_duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pgrpsf = round(pgrpsf_duration['downtime'],2)
    pgrpsfper = round(pgrpsf / pgrtotal * 100, 2)

    # PUNGANUR POWER PLANT FAULTS

    pgrppfcnt = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).count()   
    pgrppf_duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pgrppf = round(pgrppf_duration['downtime'],2)
    pgrppfper = round(pgrppf / pgrtotal * 100, 2)

    # PUNGANUR DG SET FAULTS

    pgrdgcnt = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).count()   
    pgrdg_duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pgrdg = round(pgrdg_duration['downtime'],2)
    pgrdgper = round(pgrdg / pgrtotal * 100, 2)

    # PUNGANUR DG START BATTERY FAULTS

    pgrdgbattcnt = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - DG Startup Batt Faulty']).count()   
    pgrdgbatt_duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pgrdgbatt = round(pgrdgbatt_duration['downtime'],2)
    pgrdgbattper = round(pgrdgbatt / pgrtotal * 100, 2)

    # PUNGANUR LOW BATTERY BACKUP FAULTS

    pgrlbattcnt = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).count()   
    pgrlbatt_duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pgrlbatt = round(pgrlbatt_duration['downtime'],2)
    pgrlbattper = round(pgrlbatt / pgrtotal * 100, 2)

    # PUNGANUR NO DG SET FAULTS

    pgrnodgcnt = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - Power Problem ,No DG']).count()   
    pgrnodg_duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pgrnodg = round(pgrnodg_duration['downtime'],2)
    pgrnodgper = round(pgrnodg / pgrtotal * 100, 2)

    # PUNGANUR NO DIESEL FAULTS

    pgrnodslcnt = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - Power Problem,No Diesel in D.G']).count()   
    pgrnodsl_duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pgrnodsl = round(pgrnodsl_duration['downtime'],2)
    pgrnodslper = round(pgrnodsl / pgrtotal * 100, 2)

    # PUNGANUR TOTAL OUTAGE DUE TO POWER

    pgrtotpwr = round(pgrpsf + pgrppf + pgrdg + pgrdgbatt + pgrlbatt + pgrnodg + pgrnodsl, 2)
    pgrtotpwrper = round(pgrtotpwr / pgrtotal * 100, 2)

    # PUNGANUR HARDWARE FAULTS

    pgrhwbtscnt = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).count()   
    pgrhwbts_duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pgrhwbts = round(pgrhwbts_duration['downtime'],2)
    pgrhwbtsper = round(pgrhwbts / pgrtotal * 100, 2)

    # PUNGANUR MISC FAULTS

    pgrmisccnt = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).count()   
    pgrmisc_duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    pgrmisc = round(pgrmisc_duration['downtime'],2)
    pgrmiscper = round(pgrmisc / pgrtotal * 100, 2)

    # PUNGANUR TOTAL OUTAGE DUE TO HARDWARE & MISC

    pgrtothwmisc = round(pgrhwbts + pgrmisc, 2)
    pgrtothwmiscper = round(pgrtothwmisc / pgrtotal * 100, 2)


        # Queries & Calculations for PUTTUR SDCA

    ptr_tot_duration = interruptions_table.objects.filter(SDCA='PUTTUR').aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ptrtotal = round(ptr_tot_duration['downtime'],2)
    ptravg = round(ptrtotal / 51, 2)  # PUTTUR TOWERS

    # PUTTUR STR OFC BREAKS
    
    ptrstrcnt = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).count()   
    ptrstr_duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ptrstrofc = round(ptrstr_duration['downtime'],2)
    ptrstrofcper = round(ptrstrofc / ptrtotal * 100, 2)

    # PUTTUR SSA OFC BREAKS

    ptrssacnt = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).count()   
    ptrssa_duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ptrssaofc = round(ptrssa_duration['downtime'],2)
    ptrssaofcper = round(ptrssaofc / ptrtotal * 100, 2)

    # PUTTUR BUILTUP FAULTS

    ptrbltcnt = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).count()   
    ptrblt_duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ptrblt = round(ptrblt_duration['downtime'],2)
    ptrbltper = round(ptrblt / ptrtotal * 100, 2)

    # PUTTUR RING FAULTS

    ptrringcnt = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).count()   
    ptrring_duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ptrring = round(ptrring_duration['downtime'],2)
    ptrringper = round(ptrring / ptrtotal * 100, 2)

    # PUTTUR OF EQPT FAULTS

    ptrofeptcnt = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).count()   
    ptrofept_duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ptrofept = round(ptrofept_duration['downtime'],2)
    ptrofeptper = round(ptrofept / ptrtotal * 100, 2)

    # PUTTUR TOTAL OUTAGE DUE TO MEDIA

    ptrtotmedia = round(ptrstrofc + ptrssaofc + ptrblt + ptrring + ptrofept, 2)
    ptrtotmediaper = round(ptrtotmedia / ptrtotal * 100, 2)

    # PUTTUR POWER SUPPLY FAULTS

    ptrpsfcnt = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).count()   
    ptrpsf_duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ptrpsf = round(ptrpsf_duration['downtime'],2)
    ptrpsfper = round(ptrpsf / ptrtotal * 100, 2)

    # PUTTUR POWER PLANT FAULTS

    ptrppfcnt = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).count()   
    ptrppf_duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ptrppf = round(ptrppf_duration['downtime'],2)
    ptrppfper = round(ptrppf / ptrtotal * 100, 2)

    # PUTTUR DG SET FAULTS

    ptrdgcnt = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).count()   
    ptrdg_duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ptrdg = round(ptrdg_duration['downtime'],2)
    ptrdgper = round(ptrdg / ptrtotal * 100, 2)

    # PUTTUR DG START BATTERY FAULTS

    ptrdgbattcnt = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - DG Startup Batt Faulty']).count()   
    ptrdgbatt_duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ptrdgbatt = round(ptrdgbatt_duration['downtime'],2)
    ptrdgbattper = round(ptrdgbatt / ptrtotal * 100, 2)

    # PUTTUR LOW BATTERY BACKUP FAULTS

    ptrlbattcnt = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).count()   
    ptrlbatt_duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ptrlbatt = round(ptrlbatt_duration['downtime'],2)
    ptrlbattper = round(ptrlbatt / ptrtotal * 100, 2)

    # PUTTUR NO DG SET FAULTS

    ptrnodgcnt = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - Power Problem ,No DG']).count()   
    ptrnodg_duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ptrnodg = round(ptrnodg_duration['downtime'],2)
    ptrnodgper = round(ptrnodg / ptrtotal * 100, 2)

    # PUTTUR NO DIESEL FAULTS

    ptrnodslcnt = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - Power Problem,No Diesel in D.G']).count()   
    ptrnodsl_duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ptrnodsl = round(ptrnodsl_duration['downtime'],2)
    ptrnodslper = round(ptrnodsl / ptrtotal * 100, 2)

    # PUTTUR TOTAL OUTAGE DUE TO POWER

    ptrtotpwr = round(ptrpsf + ptrppf + ptrdg + ptrdgbatt + ptrlbatt + ptrnodg + ptrnodsl, 2)
    ptrtotpwrper = round(ptrtotpwr / ptrtotal * 100, 2)

    # PUTTUR HARDWARE FAULTS

    ptrhwbtscnt = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).count()   
    ptrhwbts_duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ptrhwbts = round(ptrhwbts_duration['downtime'],2)
    ptrhwbtsper = round(ptrhwbts / ptrtotal * 100, 2)

    # PUTTUR MISC FAULTS

    ptrmisccnt = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).count()   
    ptrmisc_duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    ptrmisc = round(ptrmisc_duration['downtime'],2)
    ptrmiscper = round(ptrmisc / ptrtotal * 100, 2)

    # PUTTUR TOTAL OUTAGE DUE TO HARDWARE & MISC

    ptrtothwmisc = round(ptrhwbts + ptrmisc, 2)
    ptrtothwmiscper = round(ptrtothwmisc / ptrtotal * 100, 2)


        # Queries & Calculations for SATYAVEDU SDCA

    svd_tot_duration = interruptions_table.objects.filter(SDCA='SATYAVEDU').aggregate(downtime=Coalesce(Sum('DURATION'),0))
    svdtotal = round(svd_tot_duration['downtime'],2)
    svdavg = round(svdtotal / 26, 2)  # SATYAVEDU TOWERS

    # SATYAVEDU STR OFC BREAKS
    
    svdstrcnt = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).count()   
    svdstr_duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    svdstrofc = round(svdstr_duration['downtime'],2)
    svdstrofcper = round(svdstrofc / svdtotal * 100, 2)

    # SATYAVEDU SSA OFC BREAKS

    svdssacnt = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).count()   
    svdssa_duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    svdssaofc = round(svdssa_duration['downtime'],2)
    svdssaofcper = round(svdssaofc / svdtotal * 100, 2)

    # SATYAVEDU BUILTUP FAULTS

    svdbltcnt = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).count()   
    svdblt_duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    svdblt = round(svdblt_duration['downtime'],2)
    svdbltper = round(svdblt / svdtotal * 100, 2)

    # SATYAVEDU RING FAULTS

    svdringcnt = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).count()   
    svdring_duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    svdring = round(svdring_duration['downtime'],2)
    svdringper = round(svdring / svdtotal * 100, 2)

    # SATYAVEDU OF EQPT FAULTS

    svdofeptcnt = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).count()   
    svdofept_duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    svdofept = round(svdofept_duration['downtime'],2)
    svdofeptper = round(svdofept / svdtotal * 100, 2)

    # SATYAVEDU TOTAL OUTAGE DUE TO MEDIA

    svdtotmedia = round(svdstrofc + svdssaofc + svdblt + svdring + svdofept, 2)
    svdtotmediaper = round(svdtotmedia / svdtotal * 100, 2)

    # SATYAVEDU POWER SUPPLY FAULTS

    svdpsfcnt = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).count()   
    svdpsf_duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    svdpsf = round(svdpsf_duration['downtime'],2)
    svdpsfper = round(svdpsf / svdtotal * 100, 2)

    # SATYAVEDU POWER PLANT FAULTS

    svdppfcnt = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).count()   
    svdppf_duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    svdppf = round(svdppf_duration['downtime'],2)
    svdppfper = round(svdppf / svdtotal * 100, 2)

    # SATYAVEDU DG SET FAULTS

    svddgcnt = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).count()   
    svddg_duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    svddg = round(svddg_duration['downtime'],2)
    svddgper = round(svddg / svdtotal * 100, 2)

    # SATYAVEDU DG START BATTERY FAULTS

    svddgbattcnt = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - DG Startup Batt Faulty']).count()   
    svddgbatt_duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    svddgbatt = round(svddgbatt_duration['downtime'],2)
    svddgbattper = round(svddgbatt / svdtotal * 100, 2)

    # SATYAVEDU LOW BATTERY BACKUP FAULTS

    svdlbattcnt = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).count()   
    svdlbatt_duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    svdlbatt = round(svdlbatt_duration['downtime'],2)
    svdlbattper = round(svdlbatt / svdtotal * 100, 2)

    # SATYAVEDU NO DG SET FAULTS

    svdnodgcnt = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - Power Problem ,No DG']).count()   
    svdnodg_duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    svdnodg = round(svdnodg_duration['downtime'],2)
    svdnodgper = round(svdnodg / svdtotal * 100, 2)

    # SATYAVEDU NO DIESEL FAULTS

    svdnodslcnt = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - Power Problem,No Diesel in D.G']).count()   
    svdnodsl_duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    svdnodsl = round(svdnodsl_duration['downtime'],2)
    svdnodslper = round(svdnodsl / svdtotal * 100, 2)

    # SATYAVEDU TOTAL OUTAGE DUE TO POWER

    svdtotpwr = round(svdpsf + svdppf + svddg + svddgbatt + svdlbatt + svdnodg + svdnodsl, 2)
    svdtotpwrper = round(svdtotpwr / svdtotal * 100, 2)

    # SATYAVEDU HARDWARE FAULTS

    svdhwbtscnt = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).count()   
    svdhwbts_duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    svdhwbts = round(svdhwbts_duration['downtime'],2)
    svdhwbtsper = round(svdhwbts / svdtotal * 100, 2)

    # SATYAVEDU MISC FAULTS

    svdmisccnt = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).count()   
    svdmisc_duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    svdmisc = round(svdmisc_duration['downtime'],2)
    svdmiscper = round(svdmisc / svdtotal * 100, 2)

    # SATYAVEDU TOTAL OUTAGE DUE TO HARDWARE & MISC

    svdtothwmisc = round(svdhwbts + svdmisc, 2)
    svdtothwmiscper = round(svdtothwmisc / svdtotal * 100, 2)


        # Queries & Calculations for SODAM SDCA

    sdm_tot_duration = interruptions_table.objects.filter(SDCA='SODAM').aggregate(downtime=Coalesce(Sum('DURATION'),0))
    sdmtotal = round(sdm_tot_duration['downtime'],2)
    sdmavg = round(sdmtotal / 3, 2)  # SODAM TOWERS

    # SODAM STR OFC BREAKS
    
    sdmstrcnt = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).count()   
    sdmstr_duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    sdmstrofc = round(sdmstr_duration['downtime'],2)
    sdmstrofcper = round(sdmstrofc / sdmtotal * 100, 2)

    # SODAM SSA OFC BREAKS

    sdmssacnt = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).count()   
    sdmssa_duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    sdmssaofc = round(sdmssa_duration['downtime'],2)
    sdmssaofcper = round(sdmssaofc / sdmtotal * 100, 2)

    # SODAM BUILTUP FAULTS

    sdmbltcnt = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).count()   
    sdmblt_duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    sdmblt = round(sdmblt_duration['downtime'],2)
    sdmbltper = round(sdmblt / sdmtotal * 100, 2)

    # SODAM RING FAULTS

    sdmringcnt = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).count()   
    sdmring_duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    sdmring = round(sdmring_duration['downtime'],2)
    sdmringper = round(sdmring / sdmtotal * 100, 2)

    # SODAM OF EQPT FAULTS

    sdmofeptcnt = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).count()   
    sdmofept_duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    sdmofept = round(sdmofept_duration['downtime'],2)
    sdmofeptper = round(sdmofept / sdmtotal * 100, 2)

    # SODAM TOTAL OUTAGE DUE TO MEDIA

    sdmtotmedia = round(sdmstrofc + sdmssaofc + sdmblt + sdmring + sdmofept, 2)
    sdmtotmediaper = round(sdmtotmedia / sdmtotal * 100, 2)

    # SODAM POWER SUPPLY FAULTS

    sdmpsfcnt = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).count()   
    sdmpsf_duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    sdmpsf = round(sdmpsf_duration['downtime'],2)
    sdmpsfper = round(sdmpsf / sdmtotal * 100, 2)

    # SODAM POWER PLANT FAULTS

    sdmppfcnt = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).count()   
    sdmppf_duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    sdmppf = round(sdmppf_duration['downtime'],2)
    sdmppfper = round(sdmppf / sdmtotal * 100, 2)

    # SODAM DG SET FAULTS

    sdmdgcnt = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).count()   
    sdmdg_duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    sdmdg = round(sdmdg_duration['downtime'],2)
    sdmdgper = round(sdmdg / sdmtotal * 100, 2)

    # SODAM DG START BATTERY FAULTS

    sdmdgbattcnt = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - DG Startup Batt Faulty']).count()   
    sdmdgbatt_duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    sdmdgbatt = round(sdmdgbatt_duration['downtime'],2)
    sdmdgbattper = round(sdmdgbatt / sdmtotal * 100, 2)

    # SODAM LOW BATTERY BACKUP FAULTS

    sdmlbattcnt = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).count()   
    sdmlbatt_duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    sdmlbatt = round(sdmlbatt_duration['downtime'],2)
    sdmlbattper = round(sdmlbatt / sdmtotal * 100, 2)

    # SODAM NO DG SET FAULTS

    sdmnodgcnt = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - Power Problem ,No DG']).count()   
    sdmnodg_duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    sdmnodg = round(sdmnodg_duration['downtime'],2)
    sdmnodgper = round(sdmnodg / sdmtotal * 100, 2)

    # SODAM NO DIESEL FAULTS

    sdmnodslcnt = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - Power Problem,No Diesel in D.G']).count()   
    sdmnodsl_duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    sdmnodsl = round(sdmnodsl_duration['downtime'],2)
    sdmnodslper = round(sdmnodsl / sdmtotal * 100, 2)

    # SODAM TOTAL OUTAGE DUE TO POWER

    sdmtotpwr = round(sdmpsf + sdmppf + sdmdg + sdmdgbatt + sdmlbatt + sdmnodg + sdmnodsl, 2)
    sdmtotpwrper = round(sdmtotpwr / sdmtotal * 100, 2)

    # SODAM HARDWARE FAULTS

    sdmhwbtscnt = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).count()   
    sdmhwbts_duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    sdmhwbts = round(sdmhwbts_duration['downtime'],2)
    sdmhwbtsper = round(sdmhwbts / sdmtotal * 100, 2)

    # SODAM MISC FAULTS

    sdmmisccnt = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).count()   
    sdmmisc_duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    sdmmisc = round(sdmmisc_duration['downtime'],2)
    sdmmiscper = round(sdmmisc / sdmtotal * 100, 2)

    # SODAM TOTAL OUTAGE DUE TO HARDWARE & MISC

    sdmtothwmisc = round(sdmhwbts + sdmmisc, 2)
    sdmtothwmiscper = round(sdmtothwmisc / sdmtotal * 100, 2)


        # Queries & Calculations for SRIKALAHASTI SDCA

    skht_tot_duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI').aggregate(downtime=Coalesce(Sum('DURATION'),0))
    skhttotal = round(skht_tot_duration['downtime'],2)
    skhtavg = round(skhttotal / 38, 2)  # SRIKALAHASTI TOWERS

    # SRIKALAHASTI STR OFC BREAKS
    
    skhtstrcnt = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).count()   
    skhtstr_duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    skhtstrofc = round(skhtstr_duration['downtime'],2)
    skhtstrofcper = round(skhtstrofc / skhttotal * 100, 2)

    # SRIKALAHASTI SSA OFC BREAKS

    skhtssacnt = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).count()   
    skhtssa_duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    skhtssaofc = round(skhtssa_duration['downtime'],2)
    skhtssaofcper = round(skhtssaofc / skhttotal * 100, 2)

    # SRIKALAHASTI BUILTUP FAULTS

    skhtbltcnt = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).count()   
    skhtblt_duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    skhtblt = round(skhtblt_duration['downtime'],2)
    skhtbltper = round(skhtblt / skhttotal * 100, 2)

    # SRIKALAHASTI RING FAULTS

    skhtringcnt = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).count()   
    skhtring_duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    skhtring = round(skhtring_duration['downtime'],2)
    skhtringper = round(skhtring / skhttotal * 100, 2)

    # SRIKALAHASTI OF EQPT FAULTS

    skhtofeptcnt = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).count()   
    skhtofept_duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    skhtofept = round(skhtofept_duration['downtime'],2)
    skhtofeptper = round(skhtofept / skhttotal * 100, 2)

    # SRIKALAHASTI TOTAL OUTAGE DUE TO MEDIA

    skhttotmedia = round(skhtstrofc + skhtssaofc + skhtblt + skhtring + skhtofept, 2)
    skhttotmediaper = round(skhttotmedia / skhttotal * 100, 2)

    # SRIKALAHASTI POWER SUPPLY FAULTS

    skhtpsfcnt = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).count()   
    skhtpsf_duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    skhtpsf = round(skhtpsf_duration['downtime'],2)
    skhtpsfper = round(skhtpsf / skhttotal * 100, 2)

    # SRIKALAHASTI POWER PLANT FAULTS

    skhtppfcnt = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).count()   
    skhtppf_duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    skhtppf = round(skhtppf_duration['downtime'],2)
    skhtppfper = round(skhtppf / skhttotal * 100, 2)

    # SRIKALAHASTI DG SET FAULTS

    skhtdgcnt = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).count()   
    skhtdg_duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    skhtdg = round(skhtdg_duration['downtime'],2)
    skhtdgper = round(skhtdg / skhttotal * 100, 2)

    # SRIKALAHASTI DG START BATTERY FAULTS

    skhtdgbattcnt = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - DG Startup Batt Faulty']).count()   
    skhtdgbatt_duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    skhtdgbatt = round(skhtdgbatt_duration['downtime'],2)
    skhtdgbattper = round(skhtdgbatt / skhttotal * 100, 2)

    # SRIKALAHASTI LOW BATTERY BACKUP FAULTS

    skhtlbattcnt = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).count()   
    skhtlbatt_duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    skhtlbatt = round(skhtlbatt_duration['downtime'],2)
    skhtlbattper = round(skhtlbatt / skhttotal * 100, 2)

    # SRIKALAHASTI NO DG SET FAULTS

    skhtnodgcnt = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - Power Problem ,No DG']).count()   
    skhtnodg_duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    skhtnodg = round(skhtnodg_duration['downtime'],2)
    skhtnodgper = round(skhtnodg / skhttotal * 100, 2)

    # SRIKALAHASTI NO DIESEL FAULTS

    skhtnodslcnt = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - Power Problem,No Diesel in D.G']).count()   
    skhtnodsl_duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    skhtnodsl = round(skhtnodsl_duration['downtime'],2)
    skhtnodslper = round(skhtnodsl / skhttotal * 100, 2)

    # SRIKALAHASTI TOTAL OUTAGE DUE TO POWER

    skhttotpwr = round(skhtpsf + skhtppf + skhtdg + skhtdgbatt + skhtlbatt + skhtnodg + skhtnodsl, 2)
    skhttotpwrper = round(skhttotpwr / skhttotal * 100, 2)

    # SRIKALAHASTI HARDWARE FAULTS

    skhthwbtscnt = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).count()   
    skhthwbts_duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    skhthwbts = round(skhthwbts_duration['downtime'],2)
    skhthwbtsper = round(skhthwbts / skhttotal * 100, 2)

    # SRIKALAHASTI MISC FAULTS

    skhtmisccnt = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).count()   
    skhtmisc_duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    skhtmisc = round(skhtmisc_duration['downtime'],2)
    skhtmiscper = round(skhtmisc / skhttotal * 100, 2)

    # SRIKALAHASTI TOTAL OUTAGE DUE TO HARDWARE & MISC

    skhttothwmisc = round(skhthwbts + skhtmisc, 2)
    skhttothwmiscper = round(skhttothwmisc / skhttotal * 100, 2)


        # Queries & Calculations for VAYALPADU SDCA

    vpd_tot_duration = interruptions_table.objects.filter(SDCA='VAYALPADU').aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vpdtotal = round(vpd_tot_duration['downtime'],2)
    vpdavg = round(vpdtotal / 23, 2)  # VAYALPADU TOWERS

    # VAYALPADU STR OFC BREAKS
    
    vpdstrcnt = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).count()   
    vpdstr_duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vpdstrofc = round(vpdstr_duration['downtime'],2)
    vpdstrofcper = round(vpdstrofc / vpdtotal * 100, 2)

    # VAYALPADU SSA OFC BREAKS

    vpdssacnt = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).count()   
    vpdssa_duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vpdssaofc = round(vpdssa_duration['downtime'],2)
    vpdssaofcper = round(vpdssaofc / vpdtotal * 100, 2)

    # VAYALPADU BUILTUP FAULTS

    vpdbltcnt = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).count()   
    vpdblt_duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vpdblt = round(vpdblt_duration['downtime'],2)
    vpdbltper = round(vpdblt / vpdtotal * 100, 2)

    # VAYALPADU RING FAULTS

    vpdringcnt = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).count()   
    vpdring_duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vpdring = round(vpdring_duration['downtime'],2)
    vpdringper = round(vpdring / vpdtotal * 100, 2)

    # VAYALPADU OF EQPT FAULTS

    vpdofeptcnt = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).count()   
    vpdofept_duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vpdofept = round(vpdofept_duration['downtime'],2)
    vpdofeptper = round(vpdofept / vpdtotal * 100, 2)

    # VAYALPADU TOTAL OUTAGE DUE TO MEDIA

    vpdtotmedia = round(vpdstrofc + vpdssaofc + vpdblt + vpdring + vpdofept, 2)
    vpdtotmediaper = round(vpdtotmedia / vpdtotal * 100, 2)

    # VAYALPADU POWER SUPPLY FAULTS

    vpdpsfcnt = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).count()   
    vpdpsf_duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vpdpsf = round(vpdpsf_duration['downtime'],2)
    vpdpsfper = round(vpdpsf / vpdtotal * 100, 2)

    # VAYALPADU POWER PLANT FAULTS

    vpdppfcnt = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).count()   
    vpdppf_duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vpdppf = round(vpdppf_duration['downtime'],2)
    vpdppfper = round(vpdppf / vpdtotal * 100, 2)

    # VAYALPADU DG SET FAULTS

    vpddgcnt = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).count()   
    vpddg_duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vpddg = round(vpddg_duration['downtime'],2)
    vpddgper = round(vpddg / vpdtotal * 100, 2)

    # VAYALPADU DG START BATTERY FAULTS

    vpddgbattcnt = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - DG Startup Batt Faulty']).count()   
    vpddgbatt_duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vpddgbatt = round(vpddgbatt_duration['downtime'],2)
    vpddgbattper = round(vpddgbatt / vpdtotal * 100, 2)

    # VAYALPADU LOW BATTERY BACKUP FAULTS

    vpdlbattcnt = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).count()   
    vpdlbatt_duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vpdlbatt = round(vpdlbatt_duration['downtime'],2)
    vpdlbattper = round(vpdlbatt / vpdtotal * 100, 2)

    # VAYALPADU NO DG SET FAULTS

    vpdnodgcnt = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - Power Problem ,No DG']).count()   
    vpdnodg_duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vpdnodg = round(vpdnodg_duration['downtime'],2)
    vpdnodgper = round(vpdnodg / vpdtotal * 100, 2)

    # VAYALPADU NO DIESEL FAULTS

    vpdnodslcnt = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - Power Problem,No Diesel in D.G']).count()   
    vpdnodsl_duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vpdnodsl = round(vpdnodsl_duration['downtime'],2)
    vpdnodslper = round(vpdnodsl / vpdtotal * 100, 2)

    # VAYALPADU TOTAL OUTAGE DUE TO POWER

    vpdtotpwr = round(vpdpsf + vpdppf + vpddg + vpddgbatt + vpdlbatt + vpdnodg + vpdnodsl, 2)
    vpdtotpwrper = round(vpdtotpwr / vpdtotal * 100, 2)

    # VAYALPADU HARDWARE FAULTS

    vpdhwbtscnt = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).count()   
    vpdhwbts_duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vpdhwbts = round(vpdhwbts_duration['downtime'],2)
    vpdhwbtsper = round(vpdhwbts / vpdtotal * 100, 2)

    # VAYALPADU MISC FAULTS

    vpdmisccnt = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).count()   
    vpdmisc_duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vpdmisc = round(vpdmisc_duration['downtime'],2)
    vpdmiscper = round(vpdmisc / vpdtotal * 100, 2)

    # VAYALPADU TOTAL OUTAGE DUE TO HARDWARE & MISC

    vpdtothwmisc = round(vpdhwbts + vpdmisc, 2)
    vpdtothwmiscper = round(vpdtothwmisc / vpdtotal * 100, 2)


        # Queries & Calculations for VENKATAGIRIKOTA SDCA

    vkt_tot_duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA').aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vkttotal = round(vkt_tot_duration['downtime'],2)
    vktavg = round(vkttotal / 7, 2)  # VENKATAGIRIKOTA TOWERS

    # VENKATAGIRIKOTA STR OFC BREAKS
    
    vktstrcnt = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).count()   
    vktstr_duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vktstrofc = round(vktstr_duration['downtime'],2)
    vktstrofcper = round(vktstrofc / vkttotal * 100, 2)

    # VENKATAGIRIKOTA SSA OFC BREAKS

    vktssacnt = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).count()   
    vktssa_duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vktssaofc = round(vktssa_duration['downtime'],2)
    vktssaofcper = round(vktssaofc / vkttotal * 100, 2)

    # VENKATAGIRIKOTA BUILTUP FAULTS

    vktbltcnt = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).count()   
    vktblt_duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vktblt = round(vktblt_duration['downtime'],2)
    vktbltper = round(vktblt / vkttotal * 100, 2)

    # VENKATAGIRIKOTA RING FAULTS

    vktringcnt = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).count()   
    vktring_duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vktring = round(vktring_duration['downtime'],2)
    vktringper = round(vktring / vkttotal * 100, 2)

    # VENKATAGIRIKOTA OF EQPT FAULTS

    vktofeptcnt = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).count()   
    vktofept_duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vktofept = round(vktofept_duration['downtime'],2)
    vktofeptper = round(vktofept / vkttotal * 100, 2)

    # VENKATAGIRIKOTA TOTAL OUTAGE DUE TO MEDIA

    vkttotmedia = round(vktstrofc + vktssaofc + vktblt + vktring + vktofept, 2)
    vkttotmediaper = round(vkttotmedia / vkttotal * 100, 2)

    # VENKATAGIRIKOTA POWER SUPPLY FAULTS

    vktpsfcnt = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).count()   
    vktpsf_duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vktpsf = round(vktpsf_duration['downtime'],2)
    vktpsfper = round(vktpsf / vkttotal * 100, 2)

    # VENKATAGIRIKOTA POWER PLANT FAULTS

    vktppfcnt = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).count()   
    vktppf_duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vktppf = round(vktppf_duration['downtime'],2)
    vktppfper = round(vktppf / vkttotal * 100, 2)

    # VENKATAGIRIKOTA DG SET FAULTS

    vktdgcnt = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).count()   
    vktdg_duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vktdg = round(vktdg_duration['downtime'],2)
    vktdgper = round(vktdg / vkttotal * 100, 2)

    # VENKATAGIRIKOTA DG START BATTERY FAULTS

    vktdgbattcnt = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - DG Startup Batt Faulty']).count()   
    vktdgbatt_duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vktdgbatt = round(vktdgbatt_duration['downtime'],2)
    vktdgbattper = round(vktdgbatt / vkttotal * 100, 2)

    # VENKATAGIRIKOTA LOW BATTERY BACKUP FAULTS

    vktlbattcnt = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).count()   
    vktlbatt_duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vktlbatt = round(vktlbatt_duration['downtime'],2)
    vktlbattper = round(vktlbatt / vkttotal * 100, 2)

    # VENKATAGIRIKOTA NO DG SET FAULTS

    vktnodgcnt = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - Power Problem ,No DG']).count()   
    vktnodg_duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vktnodg = round(vktnodg_duration['downtime'],2)
    vktnodgper = round(vktnodg / vkttotal * 100, 2)

    # VENKATAGIRIKOTA NO DIESEL FAULTS

    vktnodslcnt = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - Power Problem,No Diesel in D.G']).count()   
    vktnodsl_duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vktnodsl = round(vktnodsl_duration['downtime'],2)
    vktnodslper = round(vktnodsl / vkttotal * 100, 2)

    # VENKATAGIRIKOTA TOTAL OUTAGE DUE TO POWER

    vkttotpwr = round(vktpsf + vktppf + vktdg + vktdgbatt + vktlbatt + vktnodg + vktnodsl, 2)
    vkttotpwrper = round(vkttotpwr / vkttotal * 100, 2)

    # VENKATAGIRIKOTA HARDWARE FAULTS

    vkthwbtscnt = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).count()   
    vkthwbts_duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vkthwbts = round(vkthwbts_duration['downtime'],2)
    vkthwbtsper = round(vkthwbts / vkttotal * 100, 2)

    # VENKATAGIRIKOTA MISC FAULTS

    vktmisccnt = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).count()   
    vktmisc_duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
    vktmisc = round(vktmisc_duration['downtime'],2)
    vktmiscper = round(vktmisc / vkttotal * 100, 2)

    # VENKATAGIRIKOTA TOTAL OUTAGE DUE TO HARDWARE & MISC

    vkttothwmisc = round(vkthwbts + vktmisc, 2)
    vkttothwmiscper = round(vkttothwmisc / vkttotal * 100, 2)

    # GRAND TOTAL SECTION

    total_duration = interruptions_table.objects.all().aggregate(downtime=Coalesce(Sum('DURATION'),0))
    totaldntime = round(total_duration['downtime'],2)
    totavgdntime = round(totaldntime/635,2) # TOTAL AVERAGE DOWN TIME
    



    grandtotstrcnt = round(bkkstrcnt +
                        bgpstrcnt +
                        cdrstrcnt +
                        ctrstrcnt +
                        kupstrcnt +
                        mdpstrcnt +
                        pakstrcnt +
                        plmstrcnt +
                        plrstrcnt +
                        pgrstrcnt +
                        ptrstrcnt +
                        svdstrcnt +
                        sdmstrcnt +
                        skhtstrcnt +
                        vpdstrcnt +
                        vktstrcnt, 2)

    grandtotstroutage = round(bkkstrofc +
                            bgpstrofc +
                            cdrstrofc +
                            ctrstrofc +
                            kupstrofc +
                            mdpstrofc +
                            pakstrofc +
                            plmstrofc +
                            plrstrofc +
                            pgrstrofc +
                            ptrstrofc +
                            svdstrofc +
                            sdmstrofc +
                            skhtstrofc +
                            vpdstrofc +
                            vktstrofc, 2)

    grandtotstrper = round(grandtotstroutage/totaldntime*100, 2)

    grandtotssacnt = round(bkkssacnt +
                        bgpssacnt +
                        cdrssacnt +
                        ctrssacnt +
                        kupssacnt +
                        mdpssacnt +
                        pakssacnt +
                        plmssacnt +
                        plrssacnt +
                        pgrssacnt +
                        ptrssacnt +
                        svdssacnt +
                        sdmssacnt +
                        skhtssacnt +
                        vpdssacnt +
                        vktssacnt, 2)

    grandtotssaoutage = round(bkkssaofc +
                            bgpssaofc +
                            cdrssaofc +
                            ctrssaofc +
                            kupssaofc +
                            mdpssaofc +
                            pakssaofc +
                            plmssaofc +
                            plrssaofc +
                            pgrssaofc +
                            ptrssaofc +
                            svdssaofc +
                            sdmssaofc +
                            skhtssaofc +
                            vpdssaofc +
                            vktssaofc, 2)

    grandtotssaper = round(grandtotssaoutage/totaldntime*100, 2)

    grandtotbltcnt = round(bkkbltcnt +
                        bgpbltcnt +
                        cdrbltcnt +
                        ctrbltcnt +
                        kupbltcnt +
                        mdpbltcnt +
                        pakbltcnt +
                        plmbltcnt +
                        plrbltcnt +
                        pgrbltcnt +
                        ptrbltcnt +
                        svdbltcnt +
                        sdmbltcnt +
                        skhtbltcnt +
                        vpdbltcnt +
                        vktbltcnt, 2)

    grandtotbltoutage = round(bkkblt +
                            bgpblt +
                            cdrblt +
                            ctrblt +
                            kupblt +
                            mdpblt +
                            pakblt +
                            plmblt +
                            plrblt +
                            pgrblt +
                            ptrblt +
                            svdblt +
                            sdmblt +
                            skhtblt +
                            vpdblt +
                            vktblt, 2)

    grandtotbltper = round(grandtotbltoutage/totaldntime*100, 2)

    grandtotringcnt = round(bkkringcnt +
                        bgpringcnt +
                        cdrringcnt +
                        ctrringcnt +
                        kupringcnt +
                        mdpringcnt +
                        pakringcnt +
                        plmringcnt +
                        plrringcnt +
                        pgrringcnt +
                        ptrringcnt +
                        svdringcnt +
                        sdmringcnt +
                        skhtringcnt +
                        vpdringcnt +
                        vktringcnt, 2)

    grandtotringoutage = round(bkkring +
                            bgpring +
                            cdrring +
                            ctrring +
                            kupring +
                            mdpring +
                            pakring +
                            plmring +
                            plrring +
                            pgrring +
                            ptrring +
                            svdring +
                            sdmring +
                            skhtring +
                            vpdring +
                            vktring, 2)

    grandtotringper = round(grandtotringoutage/totaldntime*100, 2)

    grandtotofeptcnt = round(bkkofeptcnt +
                        bgpofeptcnt +
                        cdrofeptcnt +
                        ctrofeptcnt +
                        kupofeptcnt +
                        mdpofeptcnt +
                        pakofeptcnt +
                        plmofeptcnt +
                        plrofeptcnt +
                        pgrofeptcnt +
                        ptrofeptcnt +
                        svdofeptcnt +
                        sdmofeptcnt +
                        skhtofeptcnt +
                        vpdofeptcnt +
                        vktofeptcnt, 2)

    grandtotofeptoutage = round(bkkofept +
                            bgpofept +
                            cdrofept +
                            ctrofept +
                            kupofept +
                            mdpofept +
                            pakofept +
                            plmofept +
                            plrofept +
                            pgrofept +
                            ptrofept +
                            svdofept +
                            sdmofept +
                            skhtofept +
                            vpdofept +
                            vktofept, 2)

    grandtotofeptper = round(grandtotofeptoutage/totaldntime*100, 2)

    grandtotpsfcnt = round(bkkpsfcnt +
                        bgppsfcnt +
                        cdrpsfcnt +
                        ctrpsfcnt +
                        kuppsfcnt +
                        mdppsfcnt +
                        pakpsfcnt +
                        plmpsfcnt +
                        plrpsfcnt +
                        pgrpsfcnt +
                        ptrpsfcnt +
                        svdpsfcnt +
                        sdmpsfcnt +
                        skhtpsfcnt +
                        vpdpsfcnt +
                        vktpsfcnt, 2)

    grandtotpsfoutage = round(bkkpsf +
                            bgppsf +
                            cdrpsf +
                            ctrpsf +
                            kuppsf +
                            mdppsf +
                            pakpsf +
                            plmpsf +
                            plrpsf +
                            pgrpsf +
                            ptrpsf +
                            svdpsf +
                            sdmpsf +
                            skhtpsf +
                            vpdpsf +
                            vktpsf, 2)

    grandtotpsfper = round(grandtotpsfoutage/totaldntime*100, 2)

    grandtotppfcnt = round(bkkppfcnt +
                        bgpppfcnt +
                        cdrppfcnt +
                        ctrppfcnt +
                        kupppfcnt +
                        mdpppfcnt +
                        pakppfcnt +
                        plmppfcnt +
                        plrppfcnt +
                        pgrppfcnt +
                        ptrppfcnt +
                        svdppfcnt +
                        sdmppfcnt +
                        skhtppfcnt +
                        vpdppfcnt +
                        vktppfcnt, 2)

    grandtotppfoutage = round(bkkppf +
                            bgpppf +
                            cdrppf +
                            ctrppf +
                            kupppf +
                            mdpppf +
                            pakppf +
                            plmppf +
                            plrppf +
                            pgrppf +
                            ptrppf +
                            svdppf +
                            sdmppf +
                            skhtppf +
                            vpdppf +
                            vktppf, 2)

    grandtotppfper = round(grandtotppfoutage/totaldntime*100, 2)

    grandtotdgcnt = round(bkkdgcnt +
                        bgpdgcnt +
                        cdrdgcnt +
                        ctrdgcnt +
                        kupdgcnt +
                        mdpdgcnt +
                        pakdgcnt +
                        plmdgcnt +
                        plrdgcnt +
                        pgrdgcnt +
                        ptrdgcnt +
                        svddgcnt +
                        sdmdgcnt +
                        skhtdgcnt +
                        vpddgcnt +
                        vktdgcnt, 2)

    grandtotdgoutage = round(bkkdg +
                        bgpdg +
                        cdrdg +
                        ctrdg +
                        kupdg +
                        mdpdg +
                        pakdg +
                        plmdg +
                        plrdg +
                        pgrdg +
                        ptrdg +
                        svddg +
                        sdmdg +
                        skhtdg +
                        vpddg +
                        vktdg, 2)

    grandtotdgper = round(grandtotdgoutage/totaldntime*100, 2)

    grandtotdgbattcnt = round(bkkdgbattcnt +
                            bgpdgbattcnt +
                            cdrdgbattcnt +
                            ctrdgbattcnt +
                            kupdgbattcnt +
                            mdpdgbattcnt +
                            pakdgbattcnt +
                            plmdgbattcnt +
                            plrdgbattcnt +
                            pgrdgbattcnt +
                            ptrdgbattcnt +
                            svddgbattcnt +
                            sdmdgbattcnt +
                            skhtdgbattcnt +
                            vpddgbattcnt +
                            vktdgbattcnt, 2)

    grandtotdgbattoutage = round(bkkdgbatt +
                            bgpdgbatt +
                            cdrdgbatt +
                            ctrdgbatt +
                            kupdgbatt +
                            mdpdgbatt +
                            pakdgbatt +
                            plmdgbatt +
                            plrdgbatt +
                            pgrdgbatt +
                            ptrdgbatt +
                            svddgbatt +
                            sdmdgbatt +
                            skhtdgbatt +
                            vpddgbatt +
                            vktdgbatt, 2)

    grandtotdgbattper = round(grandtotdgbattoutage/totaldntime*100, 2)

    grandtotlbattcnt = round(bkklbattcnt +
                        bgplbattcnt +
                        cdrlbattcnt +
                        ctrlbattcnt +
                        kuplbattcnt +
                        mdplbattcnt +
                        paklbattcnt +
                        plmlbattcnt +
                        plrlbattcnt +
                        pgrlbattcnt +
                        ptrlbattcnt +
                        svdlbattcnt +
                        sdmlbattcnt +
                        skhtlbattcnt +
                        vpdlbattcnt +
                        vktlbattcnt, 2)

    grandtotlbattoutage = round(bkklbatt +
                            bgplbatt +
                            cdrlbatt +
                            ctrlbatt +
                            kuplbatt +
                            mdplbatt +
                            paklbatt +
                            plmlbatt +
                            plrlbatt +
                            pgrlbatt +
                            ptrlbatt +
                            svdlbatt +
                            sdmlbatt +
                            skhtlbatt +
                            vpdlbatt +
                            vktlbatt,2)

    grandtotlbattper = round(grandtotlbattoutage/totaldntime*100, 2)

    grandtotnodgcnt = round(bkknodgcnt +
                        bgpnodgcnt +
                        cdrnodgcnt +
                        ctrnodgcnt +
                        kupnodgcnt +
                        mdpnodgcnt +
                        paknodgcnt +
                        plmnodgcnt +
                        plrnodgcnt +
                        pgrnodgcnt +
                        ptrnodgcnt +
                        svdnodgcnt +
                        sdmnodgcnt +
                        skhtnodgcnt +
                        vpdnodgcnt +
                        vktnodgcnt, 2)

    grandtotnodgoutage = round(bkknodg +
                            bgpnodg +
                            cdrnodg +
                            ctrnodg +
                            kupnodg +
                            mdpnodg +
                            paknodg +
                            plmnodg +
                            plrnodg +
                            pgrnodg +
                            ptrnodg +
                            svdnodg +
                            sdmnodg +
                            skhtnodg +
                            vpdnodg +
                            vktnodg, 2)

    grandtotnodgper = round(grandtotnodgoutage/totaldntime*100, 2)

    grandtotnodslcnt = round(bkknodslcnt +
                        bgpnodslcnt +
                        cdrnodslcnt +
                        ctrnodslcnt +
                        kupnodslcnt +
                        mdpnodslcnt +
                        paknodslcnt +
                        plmnodslcnt +
                        plrnodslcnt +
                        pgrnodslcnt +
                        ptrnodslcnt +
                        svdnodslcnt +
                        sdmnodslcnt +
                        skhtnodslcnt +
                        vpdnodslcnt +
                        vktnodslcnt, 2)

    grandtotnodsloutage = round(bkknodsl +
                            bgpnodsl +
                            cdrnodsl +
                            ctrnodsl +
                            kupnodsl +
                            mdpnodsl +
                            paknodsl +
                            plmnodsl +
                            plrnodsl +
                            pgrnodsl +
                            ptrnodsl +
                            svdnodsl +
                            sdmnodsl +
                            skhtnodsl +
                            vpdnodsl +
                            vktnodsl, 2)

    grandtotnodslper = round(grandtotnodsloutage/totaldntime*100, 2)

    grandtothwbtscnt = round(bkkhwbtscnt +
                        bgphwbtscnt +
                        cdrhwbtscnt +
                        ctrhwbtscnt +
                        kuphwbtscnt +
                        mdphwbtscnt +
                        pakhwbtscnt +
                        plmhwbtscnt +
                        plrhwbtscnt +
                        pgrhwbtscnt +
                        ptrhwbtscnt +
                        svdhwbtscnt +
                        sdmhwbtscnt +
                        skhthwbtscnt +
                        vpdhwbtscnt +
                        vkthwbtscnt, 2)

    grandtothwbtsoutage = round(bkkhwbts +
                            bgphwbts +
                            cdrhwbts +
                            ctrhwbts +
                            kuphwbts +
                            mdphwbts +
                            pakhwbts +
                            plmhwbts +
                            plrhwbts +
                            pgrhwbts +
                            ptrhwbts +
                            svdhwbts +
                            sdmhwbts +
                            skhthwbts +
                            vpdhwbts +
                            vkthwbts, 2)

    grandtothwbtsper = round(grandtothwbtsoutage/totaldntime*100, 2)

    grandtotmisccnt = round(bkkmisccnt +
                        bgpmisccnt +
                        cdrmisccnt +
                        ctrmisccnt +
                        kupmisccnt +
                        mdpmisccnt +
                        pakmisccnt +
                        plmmisccnt +
                        plrmisccnt +
                        pgrmisccnt +
                        ptrmisccnt +
                        svdmisccnt +
                        sdmmisccnt +
                        skhtmisccnt +
                        vpdmisccnt +
                        vktmisccnt, 2)

    grandtotmiscoutage = round(bkkmisc +
                            bgpmisc +
                            cdrmisc +
                            ctrmisc +
                            kupmisc +
                            mdpmisc +
                            pakmisc +
                            plmmisc +
                            plrmisc +
                            pgrmisc +
                            ptrmisc +
                            svdmisc +
                            sdmmisc +
                            skhtmisc +
                            vpdmisc +
                            vktmisc, 2)

    grandtotmiscper = round(grandtotmiscoutage/totaldntime*100, 2)



    mediagrandtotoutage = round(grandtotstroutage + grandtotssaoutage + grandtotbltoutage + grandtotringoutage + grandtotofeptoutage, 2)

    mediagrandtotper = round(mediagrandtotoutage / totaldntime * 100, 2)

    powergrandtotoutage = round(grandtotpsfoutage + grandtotppfoutage + grandtotdgoutage + grandtotdgbattoutage + grandtotlbattoutage + grandtotnodgoutage + grandtotnodsloutage, 2)

    powergrandtotper = round(powergrandtotoutage/totaldntime*100, 2)

    hwmiscgrandtotoutage = round(grandtothwbtsoutage + grandtotmiscoutage, 2)

    hwmiscgrandtotper = round(hwmiscgrandtotoutage/totaldntime*100, 2)


    dict2g3g = {
        'bkktotal': bkktotal,
        'bkkavg': bkkavg,

        'bkkstrcnt': bkkstrcnt,
        'bkkstrofc': bkkstrofc,
        'bkkstrofcper': bkkstrofcper,

        'bkkssacnt': bkkssacnt,
        'bkkssaofc': bkkssaofc,
        'bkkssaofcper': bkkssaofcper,

        'bkkbltcnt': bkkbltcnt,
        'bkkblt': bkkblt,
        'bkkbltper': bkkbltper,

        'bkkringcnt': bkkringcnt,
        'bkkring': bkkring,
        'bkkringper': bkkringper,

        'bkkofeptcnt': bkkofeptcnt,
        'bkkofept': bkkofept,
        'bkkofeptper': bkkofeptper,

        'bkktotmedia': bkktotmedia,
        'bkktotmediaper': bkktotmediaper,

        'bkkpsfcnt': bkkpsfcnt,
        'bkkpsf': bkkpsf,
        'bkkpsfper': bkkpsfper,

        'bkkppfcnt': bkkppfcnt,
        'bkkppf': bkkppf,
        'bkkppfper': bkkppfper,

        'bkkdgcnt': bkkdgcnt,
        'bkkdg': bkkdg,
        'bkkdgper': bkkdgper,

        'bkkdgbattcnt': bkkdgbattcnt,
        'bkkdgbatt': bkkdgbatt,
        'bkkdgbattper': bkkdgbattper,

        'bkklbattcnt': bkklbattcnt,
        'bkklbatt': bkklbatt,
        'bkklbattper': bkklbattper,

        'bkknodgcnt': bkknodgcnt,
        'bkknodg': bkknodg,
        'bkknodgper': bkknodgper,

        'bkknodslcnt': bkknodslcnt,
        'bkknodsl': bkknodsl,
        'bkknodslper': bkknodslper,

        'bkktotpwr': bkktotpwr,
        'bkktotpwrper': bkktotpwrper,

        'bkkhwbtscnt': bkkhwbtscnt,
        'bkkhwbts': bkkhwbts,
        'bkkhwbtsper': bkkhwbtsper,

        'bkkmisccnt': bkkmisccnt,
        'bkkmisc': bkkmisc,
        'bkkmiscper': bkkmiscper,

        'bkktothwmisc': bkktothwmisc,
        'bkktothwmiscper': bkktothwmiscper,

        'bgptotal': bgptotal,
        'bgpavg': bgpavg,

        'bgpstrcnt': bgpstrcnt,
        'bgpstrofc': bgpstrofc,
        'bgpstrofcper': bgpstrofcper,

        'bgpssacnt': bgpssacnt,
        'bgpssaofc': bgpssaofc,
        'bgpssaofcper': bgpssaofcper,

        'bgpbltcnt': bgpbltcnt,
        'bgpblt': bgpblt,
        'bgpbltper': bgpbltper,

        'bgpringcnt': bgpringcnt,
        'bgpring': bgpring,
        'bgpringper': bgpringper,

        'bgpofeptcnt': bgpofeptcnt,
        'bgpofept': bgpofept,
        'bgpofeptper': bgpofeptper,

        'bgptotmedia': bgptotmedia,
        'bgptotmediaper': bgptotmediaper,

        'bgppsfcnt': bgppsfcnt,
        'bgppsf': bgppsf,
        'bgppsfper': bgppsfper,

        'bgpppfcnt': bgpppfcnt,
        'bgpppf': bgpppf,
        'bgpppfper': bgpppfper,

        'bgpdgcnt': bgpdgcnt,
        'bgpdg': bgpdg,
        'bgpdgper': bgpdgper,

        'bgpdgbattcnt': bgpdgbattcnt,
        'bgpdgbatt': bgpdgbatt,
        'bgpdgbattper': bgpdgbattper,

        'bgplbattcnt': bgplbattcnt,
        'bgplbatt': bgplbatt,
        'bgplbattper': bgplbattper,

        'bgpnodgcnt': bgpnodgcnt,
        'bgpnodg': bgpnodg,
        'bgpnodgper': bgpnodgper,

        'bgpnodslcnt': bgpnodslcnt,
        'bgpnodsl': bgpnodsl,
        'bgpnodslper': bgpnodslper,

        'bgptotpwr': bgptotpwr,
        'bgptotpwrper': bgptotpwrper,

        'bgphwbtscnt': bgphwbtscnt,
        'bgphwbts': bgphwbts,
        'bgphwbtsper': bgphwbtsper,

        'bgpmisccnt': bgpmisccnt,
        'bgpmisc': bgpmisc,
        'bgpmiscper': bgpmiscper,

        'bgptothwmisc': bgptothwmisc,
        'bgptothwmiscper': bgptothwmiscper,

        'cdrtotal': cdrtotal,
        'cdravg': cdravg,

        'cdrstrcnt': cdrstrcnt,
        'cdrstrofc': cdrstrofc,
        'cdrstrofcper': cdrstrofcper,

        'cdrssacnt': cdrssacnt,
        'cdrssaofc': cdrssaofc,
        'cdrssaofcper': cdrssaofcper,

        'cdrbltcnt': cdrbltcnt,
        'cdrblt': cdrblt,
        'cdrbltper': cdrbltper,

        'cdrringcnt': cdrringcnt,
        'cdrring': cdrring,
        'cdrringper': cdrringper,

        'cdrofeptcnt': cdrofeptcnt,
        'cdrofept': cdrofept,
        'cdrofeptper': cdrofeptper,

        'cdrtotmedia': cdrtotmedia,
        'cdrtotmediaper': cdrtotmediaper,

        'cdrpsfcnt': cdrpsfcnt,
        'cdrpsf': cdrpsf,
        'cdrpsfper': cdrpsfper,

        'cdrppfcnt': cdrppfcnt,
        'cdrppf': cdrppf,
        'cdrppfper': cdrppfper,

        'cdrdgcnt': cdrdgcnt,
        'cdrdg': cdrdg,
        'cdrdgper': cdrdgper,

        'cdrdgbattcnt': cdrdgbattcnt,
        'cdrdgbatt': cdrdgbatt,
        'cdrdgbattper': cdrdgbattper,

        'cdrlbattcnt': cdrlbattcnt,
        'cdrlbatt': cdrlbatt,
        'cdrlbattper': cdrlbattper,

        'cdrnodgcnt': cdrnodgcnt,
        'cdrnodg': cdrnodg,
        'cdrnodgper': cdrnodgper,

        'cdrnodslcnt': cdrnodslcnt,
        'cdrnodsl': cdrnodsl,
        'cdrnodslper': cdrnodslper,

        'cdrtotpwr': cdrtotpwr,
        'cdrtotpwrper': cdrtotpwrper,

        'cdrhwbtscnt': cdrhwbtscnt,
        'cdrhwbts': cdrhwbts,
        'cdrhwbtsper': cdrhwbtsper,

        'cdrmisccnt': cdrmisccnt,
        'cdrmisc': cdrmisc,
        'cdrmiscper': cdrmiscper,

        'cdrtothwmisc': cdrtothwmisc,
        'cdrtothwmiscper': cdrtothwmiscper,

        'ctrtotal': ctrtotal,
        'ctravg': ctravg,

        'ctrstrcnt': ctrstrcnt,
        'ctrstrofc': ctrstrofc,
        'ctrstrofcper': ctrstrofcper,

        'ctrssacnt': ctrssacnt,
        'ctrssaofc': ctrssaofc,
        'ctrssaofcper': ctrssaofcper,

        'ctrbltcnt': ctrbltcnt,
        'ctrblt': ctrblt,
        'ctrbltper': ctrbltper,

        'ctrringcnt': ctrringcnt,
        'ctrring': ctrring,
        'ctrringper': ctrringper,

        'ctrofeptcnt': ctrofeptcnt,
        'ctrofept': ctrofept,
        'ctrofeptper': ctrofeptper,

        'ctrtotmedia': ctrtotmedia,
        'ctrtotmediaper': ctrtotmediaper,

        'ctrpsfcnt': ctrpsfcnt,
        'ctrpsf': ctrpsf,
        'ctrpsfper': ctrpsfper,

        'ctrppfcnt': ctrppfcnt,
        'ctrppf': ctrppf,
        'ctrppfper': ctrppfper,

        'ctrdgcnt': ctrdgcnt,
        'ctrdg': ctrdg,
        'ctrdgper': ctrdgper,

        'ctrdgbattcnt': ctrdgbattcnt,
        'ctrdgbatt': ctrdgbatt,
        'ctrdgbattper': ctrdgbattper,

        'ctrlbattcnt': ctrlbattcnt,
        'ctrlbatt': ctrlbatt,
        'ctrlbattper': ctrlbattper,

        'ctrnodgcnt': ctrnodgcnt,
        'ctrnodg': ctrnodg,
        'ctrnodgper': ctrnodgper,

        'ctrnodslcnt': ctrnodslcnt,
        'ctrnodsl': ctrnodsl,
        'ctrnodslper': ctrnodslper,

        'ctrtotpwr': ctrtotpwr,
        'ctrtotpwrper': ctrtotpwrper,

        'ctrhwbtscnt': ctrhwbtscnt,
        'ctrhwbts': ctrhwbts,
        'ctrhwbtsper': ctrhwbtsper,

        'ctrmisccnt': ctrmisccnt,
        'ctrmisc': ctrmisc,
        'ctrmiscper': ctrmiscper,

        'ctrtothwmisc': ctrtothwmisc,
        'ctrtothwmiscper': ctrtothwmiscper,

        'kuptotal': kuptotal,
        'kupavg': kupavg,

        'kupstrcnt': kupstrcnt,
        'kupstrofc': kupstrofc,
        'kupstrofcper': kupstrofcper,

        'kupssacnt': kupssacnt,
        'kupssaofc': kupssaofc,
        'kupssaofcper': kupssaofcper,

        'kupbltcnt': kupbltcnt,
        'kupblt': kupblt,
        'kupbltper': kupbltper,

        'kupringcnt': kupringcnt,
        'kupring': kupring,
        'kupringper': kupringper,

        'kupofeptcnt': kupofeptcnt,
        'kupofept': kupofept,
        'kupofeptper': kupofeptper,

        'kuptotmedia': kuptotmedia,
        'kuptotmediaper': kuptotmediaper,

        'kuppsfcnt': kuppsfcnt,
        'kuppsf': kuppsf,
        'kuppsfper': kuppsfper,

        'kupppfcnt': kupppfcnt,
        'kupppf': kupppf,
        'kupppfper': kupppfper,

        'kupdgcnt': kupdgcnt,
        'kupdg': kupdg,
        'kupdgper': kupdgper,

        'kupdgbattcnt': kupdgbattcnt,
        'kupdgbatt': kupdgbatt,
        'kupdgbattper': kupdgbattper,

        'kuplbattcnt': kuplbattcnt,
        'kuplbatt': kuplbatt,
        'kuplbattper': kuplbattper,

        'kupnodgcnt': kupnodgcnt,
        'kupnodg': kupnodg,
        'kupnodgper': kupnodgper,

        'kupnodslcnt': kupnodslcnt,
        'kupnodsl': kupnodsl,
        'kupnodslper': kupnodslper,

        'kuptotpwr': kuptotpwr,
        'kuptotpwrper': kuptotpwrper,

        'kuphwbtscnt': kuphwbtscnt,
        'kuphwbts': kuphwbts,
        'kuphwbtsper': kuphwbtsper,

        'kupmisccnt': kupmisccnt,
        'kupmisc': kupmisc,
        'kupmiscper': kupmiscper,

        'kuptothwmisc': kuptothwmisc,
        'kuptothwmiscper': kuptothwmiscper,

        'mdptotal': mdptotal,
        'mdpavg': mdpavg,

        'mdpstrcnt': mdpstrcnt,
        'mdpstrofc': mdpstrofc,
        'mdpstrofcper': mdpstrofcper,

        'mdpssacnt': mdpssacnt,
        'mdpssaofc': mdpssaofc,
        'mdpssaofcper': mdpssaofcper,

        'mdpbltcnt': mdpbltcnt,
        'mdpblt': mdpblt,
        'mdpbltper': mdpbltper,

        'mdpringcnt': mdpringcnt,
        'mdpring': mdpring,
        'mdpringper': mdpringper,

        'mdpofeptcnt': mdpofeptcnt,
        'mdpofept': mdpofept,
        'mdpofeptper': mdpofeptper,

        'mdptotmedia': mdptotmedia,
        'mdptotmediaper': mdptotmediaper,

        'mdppsfcnt': mdppsfcnt,
        'mdppsf': mdppsf,
        'mdppsfper': mdppsfper,

        'mdpppfcnt': mdpppfcnt,
        'mdpppf': mdpppf,
        'mdpppfper': mdpppfper,

        'mdpdgcnt': mdpdgcnt,
        'mdpdg': mdpdg,
        'mdpdgper': mdpdgper,

        'mdpdgbattcnt': mdpdgbattcnt,
        'mdpdgbatt': mdpdgbatt,
        'mdpdgbattper': mdpdgbattper,

        'mdplbattcnt': mdplbattcnt,
        'mdplbatt': mdplbatt,
        'mdplbattper': mdplbattper,

        'mdpnodgcnt': mdpnodgcnt,
        'mdpnodg': mdpnodg,
        'mdpnodgper': mdpnodgper,

        'mdpnodslcnt': mdpnodslcnt,
        'mdpnodsl': mdpnodsl,
        'mdpnodslper': mdpnodslper,

        'mdptotpwr': mdptotpwr,
        'mdptotpwrper': mdptotpwrper,

        'mdphwbtscnt': mdphwbtscnt,
        'mdphwbts': mdphwbts,
        'mdphwbtsper': mdphwbtsper,

        'mdpmisccnt': mdpmisccnt,
        'mdpmisc': mdpmisc,
        'mdpmiscper': mdpmiscper,

        'mdptothwmisc': mdptothwmisc,
        'mdptothwmiscper': mdptothwmiscper,

        'paktotal': paktotal,
        'pakavg': pakavg,

        'pakstrcnt': pakstrcnt,
        'pakstrofc': pakstrofc,
        'pakstrofcper': pakstrofcper,

        'pakssacnt': pakssacnt,
        'pakssaofc': pakssaofc,
        'pakssaofcper': pakssaofcper,

        'pakbltcnt': pakbltcnt,
        'pakblt': pakblt,
        'pakbltper': pakbltper,

        'pakringcnt': pakringcnt,
        'pakring': pakring,
        'pakringper': pakringper,

        'pakofeptcnt': pakofeptcnt,
        'pakofept': pakofept,
        'pakofeptper': pakofeptper,

        'paktotmedia': paktotmedia,
        'paktotmediaper': paktotmediaper,

        'pakpsfcnt': pakpsfcnt,
        'pakpsf': pakpsf,
        'pakpsfper': pakpsfper,

        'pakppfcnt': pakppfcnt,
        'pakppf': pakppf,
        'pakppfper': pakppfper,

        'pakdgcnt': pakdgcnt,
        'pakdg': pakdg,
        'pakdgper': pakdgper,

        'pakdgbattcnt': pakdgbattcnt,
        'pakdgbatt': pakdgbatt,
        'pakdgbattper': pakdgbattper,

        'paklbattcnt': paklbattcnt,
        'paklbatt': paklbatt,
        'paklbattper': paklbattper,

        'paknodgcnt': paknodgcnt,
        'paknodg': paknodg,
        'paknodgper': paknodgper,

        'paknodslcnt': paknodslcnt,
        'paknodsl': paknodsl,
        'paknodslper': paknodslper,

        'paktotpwr': paktotpwr,
        'paktotpwrper': paktotpwrper,

        'pakhwbtscnt': pakhwbtscnt,
        'pakhwbts': pakhwbts,
        'pakhwbtsper': pakhwbtsper,

        'pakmisccnt': pakmisccnt,
        'pakmisc': pakmisc,
        'pakmiscper': pakmiscper,

        'paktothwmisc': paktothwmisc,
        'paktothwmiscper': paktothwmiscper,

        'plmtotal': plmtotal,
        'plmavg': plmavg,

        'plmstrcnt': plmstrcnt,
        'plmstrofc': plmstrofc,
        'plmstrofcper': plmstrofcper,

        'plmssacnt': plmssacnt,
        'plmssaofc': plmssaofc,
        'plmssaofcper': plmssaofcper,

        'plmbltcnt': plmbltcnt,
        'plmblt': plmblt,
        'plmbltper': plmbltper,

        'plmringcnt': plmringcnt,
        'plmring': plmring,
        'plmringper': plmringper,

        'plmofeptcnt': plmofeptcnt,
        'plmofept': plmofept,
        'plmofeptper': plmofeptper,

        'plmtotmedia': plmtotmedia,
        'plmtotmediaper': plmtotmediaper,

        'plmpsfcnt': plmpsfcnt,
        'plmpsf': plmpsf,
        'plmpsfper': plmpsfper,

        'plmppfcnt': plmppfcnt,
        'plmppf': plmppf,
        'plmppfper': plmppfper,

        'plmdgcnt': plmdgcnt,
        'plmdg': plmdg,
        'plmdgper': plmdgper,

        'plmdgbattcnt': plmdgbattcnt,
        'plmdgbatt': plmdgbatt,
        'plmdgbattper': plmdgbattper,

        'plmlbattcnt': plmlbattcnt,
        'plmlbatt': plmlbatt,
        'plmlbattper': plmlbattper,

        'plmnodgcnt': plmnodgcnt,
        'plmnodg': plmnodg,
        'plmnodgper': plmnodgper,

        'plmnodslcnt': plmnodslcnt,
        'plmnodsl': plmnodsl,
        'plmnodslper': plmnodslper,

        'plmtotpwr': plmtotpwr,
        'plmtotpwrper': plmtotpwrper,

        'plmhwbtscnt': plmhwbtscnt,
        'plmhwbts': plmhwbts,
        'plmhwbtsper': plmhwbtsper,

        'plmmisccnt': plmmisccnt,
        'plmmisc': plmmisc,
        'plmmiscper': plmmiscper,

        'plmtothwmisc': plmtothwmisc,
        'plmtothwmiscper': plmtothwmiscper,

        'plrtotal': plrtotal,
        'plravg': plravg,

        'plrstrcnt': plrstrcnt,
        'plrstrofc': plrstrofc,
        'plrstrofcper': plrstrofcper,

        'plrssacnt': plrssacnt,
        'plrssaofc': plrssaofc,
        'plrssaofcper': plrssaofcper,

        'plrbltcnt': plrbltcnt,
        'plrblt': plrblt,
        'plrbltper': plrbltper,

        'plrringcnt': plrringcnt,
        'plrring': plrring,
        'plrringper': plrringper,

        'plrofeptcnt': plrofeptcnt,
        'plrofept': plrofept,
        'plrofeptper': plrofeptper,

        'plrtotmedia': plrtotmedia,
        'plrtotmediaper': plrtotmediaper,

        'plrpsfcnt': plrpsfcnt,
        'plrpsf': plrpsf,
        'plrpsfper': plrpsfper,

        'plrppfcnt': plrppfcnt,
        'plrppf': plrppf,
        'plrppfper': plrppfper,

        'plrdgcnt': plrdgcnt,
        'plrdg': plrdg,
        'plrdgper': plrdgper,

        'plrdgbattcnt': plrdgbattcnt,
        'plrdgbatt': plrdgbatt,
        'plrdgbattper': plrdgbattper,

        'plrlbattcnt': plrlbattcnt,
        'plrlbatt': plrlbatt,
        'plrlbattper': plrlbattper,

        'plrnodgcnt': plrnodgcnt,
        'plrnodg': plrnodg,
        'plrnodgper': plrnodgper,

        'plrnodslcnt': plrnodslcnt,
        'plrnodsl': plrnodsl,
        'plrnodslper': plrnodslper,

        'plrtotpwr': plrtotpwr,
        'plrtotpwrper': plrtotpwrper,

        'plrhwbtscnt': plrhwbtscnt,
        'plrhwbts': plrhwbts,
        'plrhwbtsper': plrhwbtsper,

        'plrmisccnt': plrmisccnt,
        'plrmisc': plrmisc,
        'plrmiscper': plrmiscper,

        'plrtothwmisc': plrtothwmisc,
        'plrtothwmiscper': plrtothwmiscper,

        'pgrtotal': pgrtotal,
        'pgravg': pgravg,

        'pgrstrcnt': pgrstrcnt,
        'pgrstrofc': pgrstrofc,
        'pgrstrofcper': pgrstrofcper,

        'pgrssacnt': pgrssacnt,
        'pgrssaofc': pgrssaofc,
        'pgrssaofcper': pgrssaofcper,

        'pgrbltcnt': pgrbltcnt,
        'pgrblt': pgrblt,
        'pgrbltper': pgrbltper,

        'pgrringcnt': pgrringcnt,
        'pgrring': pgrring,
        'pgrringper': pgrringper,

        'pgrofeptcnt': pgrofeptcnt,
        'pgrofept': pgrofept,
        'pgrofeptper': pgrofeptper,

        'pgrtotmedia': pgrtotmedia,
        'pgrtotmediaper': pgrtotmediaper,

        'pgrpsfcnt': pgrpsfcnt,
        'pgrpsf': pgrpsf,
        'pgrpsfper': pgrpsfper,

        'pgrppfcnt': pgrppfcnt,
        'pgrppf': pgrppf,
        'pgrppfper': pgrppfper,

        'pgrdgcnt': pgrdgcnt,
        'pgrdg': pgrdg,
        'pgrdgper': pgrdgper,

        'pgrdgbattcnt': pgrdgbattcnt,
        'pgrdgbatt': pgrdgbatt,
        'pgrdgbattper': pgrdgbattper,

        'pgrlbattcnt': pgrlbattcnt,
        'pgrlbatt': pgrlbatt,
        'pgrlbattper': pgrlbattper,

        'pgrnodgcnt': pgrnodgcnt,
        'pgrnodg': pgrnodg,
        'pgrnodgper': pgrnodgper,

        'pgrnodslcnt': pgrnodslcnt,
        'pgrnodsl': pgrnodsl,
        'pgrnodslper': pgrnodslper,

        'pgrtotpwr': pgrtotpwr,
        'pgrtotpwrper': pgrtotpwrper,

        'pgrhwbtscnt': pgrhwbtscnt,
        'pgrhwbts': pgrhwbts,
        'pgrhwbtsper': pgrhwbtsper,

        'pgrmisccnt': pgrmisccnt,
        'pgrmisc': pgrmisc,
        'pgrmiscper': pgrmiscper,

        'pgrtothwmisc': pgrtothwmisc,
        'pgrtothwmiscper': pgrtothwmiscper,

        'ptrtotal': ptrtotal,
        'ptravg': ptravg,

        'ptrstrcnt': ptrstrcnt,
        'ptrstrofc': ptrstrofc,
        'ptrstrofcper': ptrstrofcper,

        'ptrssacnt': ptrssacnt,
        'ptrssaofc': ptrssaofc,
        'ptrssaofcper': ptrssaofcper,

        'ptrbltcnt': ptrbltcnt,
        'ptrblt': ptrblt,
        'ptrbltper': ptrbltper,

        'ptrringcnt': ptrringcnt,
        'ptrring': ptrring,
        'ptrringper': ptrringper,

        'ptrofeptcnt': ptrofeptcnt,
        'ptrofept': ptrofept,
        'ptrofeptper': ptrofeptper,

        'ptrtotmedia': ptrtotmedia,
        'ptrtotmediaper': ptrtotmediaper,

        'ptrpsfcnt': ptrpsfcnt,
        'ptrpsf': ptrpsf,
        'ptrpsfper': ptrpsfper,

        'ptrppfcnt': ptrppfcnt,
        'ptrppf': ptrppf,
        'ptrppfper': ptrppfper,

        'ptrdgcnt': ptrdgcnt,
        'ptrdg': ptrdg,
        'ptrdgper': ptrdgper,

        'ptrdgbattcnt': ptrdgbattcnt,
        'ptrdgbatt': ptrdgbatt,
        'ptrdgbattper': ptrdgbattper,

        'ptrlbattcnt': ptrlbattcnt,
        'ptrlbatt': ptrlbatt,
        'ptrlbattper': ptrlbattper,

        'ptrnodgcnt': ptrnodgcnt,
        'ptrnodg': ptrnodg,
        'ptrnodgper': ptrnodgper,

        'ptrnodslcnt': ptrnodslcnt,
        'ptrnodsl': ptrnodsl,
        'ptrnodslper': ptrnodslper,

        'ptrtotpwr': ptrtotpwr,
        'ptrtotpwrper': ptrtotpwrper,

        'ptrhwbtscnt': ptrhwbtscnt,
        'ptrhwbts': ptrhwbts,
        'ptrhwbtsper': ptrhwbtsper,

        'ptrmisccnt': ptrmisccnt,
        'ptrmisc': ptrmisc,
        'ptrmiscper': ptrmiscper,

        'ptrtothwmisc': ptrtothwmisc,
        'ptrtothwmiscper': ptrtothwmiscper,

        'svdtotal': svdtotal,
        'svdavg': svdavg,

        'svdstrcnt': svdstrcnt,
        'svdstrofc': svdstrofc,
        'svdstrofcper': svdstrofcper,

        'svdssacnt': svdssacnt,
        'svdssaofc': svdssaofc,
        'svdssaofcper': svdssaofcper,

        'svdbltcnt': svdbltcnt,
        'svdblt': svdblt,
        'svdbltper': svdbltper,

        'svdringcnt': svdringcnt,
        'svdring': svdring,
        'svdringper': svdringper,

        'svdofeptcnt': svdofeptcnt,
        'svdofept': svdofept,
        'svdofeptper': svdofeptper,

        'svdtotmedia': svdtotmedia,
        'svdtotmediaper': svdtotmediaper,

        'svdpsfcnt': svdpsfcnt,
        'svdpsf': svdpsf,
        'svdpsfper': svdpsfper,

        'svdppfcnt': svdppfcnt,
        'svdppf': svdppf,
        'svdppfper': svdppfper,

        'svddgcnt': svddgcnt,
        'svddg': svddg,
        'svddgper': svddgper,

        'svddgbattcnt': svddgbattcnt,
        'svddgbatt': svddgbatt,
        'svddgbattper': svddgbattper,

        'svdlbattcnt': svdlbattcnt,
        'svdlbatt': svdlbatt,
        'svdlbattper': svdlbattper,

        'svdnodgcnt': svdnodgcnt,
        'svdnodg': svdnodg,
        'svdnodgper': svdnodgper,

        'svdnodslcnt': svdnodslcnt,
        'svdnodsl': svdnodsl,
        'svdnodslper': svdnodslper,

        'svdtotpwr': svdtotpwr,
        'svdtotpwrper': svdtotpwrper,

        'svdhwbtscnt': svdhwbtscnt,
        'svdhwbts': svdhwbts,
        'svdhwbtsper': svdhwbtsper,

        'svdmisccnt': svdmisccnt,
        'svdmisc': svdmisc,
        'svdmiscper': svdmiscper,

        'svdtothwmisc': svdtothwmisc,
        'svdtothwmiscper': svdtothwmiscper,

        'sdmtotal': sdmtotal,
        'sdmavg': sdmavg,

        'sdmstrcnt': sdmstrcnt,
        'sdmstrofc': sdmstrofc,
        'sdmstrofcper': sdmstrofcper,

        'sdmssacnt': sdmssacnt,
        'sdmssaofc': sdmssaofc,
        'sdmssaofcper': sdmssaofcper,

        'sdmbltcnt': sdmbltcnt,
        'sdmblt': sdmblt,
        'sdmbltper': sdmbltper,

        'sdmringcnt': sdmringcnt,
        'sdmring': sdmring,
        'sdmringper': sdmringper,

        'sdmofeptcnt': sdmofeptcnt,
        'sdmofept': sdmofept,
        'sdmofeptper': sdmofeptper,

        'sdmtotmedia': sdmtotmedia,
        'sdmtotmediaper': sdmtotmediaper,

        'sdmpsfcnt': sdmpsfcnt,
        'sdmpsf': sdmpsf,
        'sdmpsfper': sdmpsfper,

        'sdmppfcnt': sdmppfcnt,
        'sdmppf': sdmppf,
        'sdmppfper': sdmppfper,

        'sdmdgcnt': sdmdgcnt,
        'sdmdg': sdmdg,
        'sdmdgper': sdmdgper,

        'sdmdgbattcnt': sdmdgbattcnt,
        'sdmdgbatt': sdmdgbatt,
        'sdmdgbattper': sdmdgbattper,

        'sdmlbattcnt': sdmlbattcnt,
        'sdmlbatt': sdmlbatt,
        'sdmlbattper': sdmlbattper,

        'sdmnodgcnt': sdmnodgcnt,
        'sdmnodg': sdmnodg,
        'sdmnodgper': sdmnodgper,

        'sdmnodslcnt': sdmnodslcnt,
        'sdmnodsl': sdmnodsl,
        'sdmnodslper': sdmnodslper,

        'sdmtotpwr': sdmtotpwr,
        'sdmtotpwrper': sdmtotpwrper,

        'sdmhwbtscnt': sdmhwbtscnt,
        'sdmhwbts': sdmhwbts,
        'sdmhwbtsper': sdmhwbtsper,

        'sdmmisccnt': sdmmisccnt,
        'sdmmisc': sdmmisc,
        'sdmmiscper': sdmmiscper,

        'sdmtothwmisc': sdmtothwmisc,
        'sdmtothwmiscper': sdmtothwmiscper,

        'skhttotal': skhttotal,
        'skhtavg': skhtavg,

        'skhtstrcnt': skhtstrcnt,
        'skhtstrofc': skhtstrofc,
        'skhtstrofcper': skhtstrofcper,

        'skhtssacnt': skhtssacnt,
        'skhtssaofc': skhtssaofc,
        'skhtssaofcper': skhtssaofcper,

        'skhtbltcnt': skhtbltcnt,
        'skhtblt': skhtblt,
        'skhtbltper': skhtbltper,

        'skhtringcnt': skhtringcnt,
        'skhtring': skhtring,
        'skhtringper': skhtringper,

        'skhtofeptcnt': skhtofeptcnt,
        'skhtofept': skhtofept,
        'skhtofeptper': skhtofeptper,

        'skhttotmedia': skhttotmedia,
        'skhttotmediaper': skhttotmediaper,

        'skhtpsfcnt': skhtpsfcnt,
        'skhtpsf': skhtpsf,
        'skhtpsfper': skhtpsfper,

        'skhtppfcnt': skhtppfcnt,
        'skhtppf': skhtppf,
        'skhtppfper': skhtppfper,

        'skhtdgcnt': skhtdgcnt,
        'skhtdg': skhtdg,
        'skhtdgper': skhtdgper,

        'skhtdgbattcnt': skhtdgbattcnt,
        'skhtdgbatt': skhtdgbatt,
        'skhtdgbattper': skhtdgbattper,

        'skhtlbattcnt': skhtlbattcnt,
        'skhtlbatt': skhtlbatt,
        'skhtlbattper': skhtlbattper,

        'skhtnodgcnt': skhtnodgcnt,
        'skhtnodg': skhtnodg,
        'skhtnodgper': skhtnodgper,

        'skhtnodslcnt': skhtnodslcnt,
        'skhtnodsl': skhtnodsl,
        'skhtnodslper': skhtnodslper,

        'skhttotpwr': skhttotpwr,
        'skhttotpwrper': skhttotpwrper,

        'skhthwbtscnt': skhthwbtscnt,
        'skhthwbts': skhthwbts,
        'skhthwbtsper': skhthwbtsper,

        'skhtmisccnt': skhtmisccnt,
        'skhtmisc': skhtmisc,
        'skhtmiscper': skhtmiscper,

        'skhttothwmisc': skhttothwmisc,
        'skhttothwmiscper': skhttothwmiscper,

        'vpdtotal': vpdtotal,
        'vpdavg': vpdavg,

        'vpdstrcnt': vpdstrcnt,
        'vpdstrofc': vpdstrofc,
        'vpdstrofcper': vpdstrofcper,

        'vpdssacnt': vpdssacnt,
        'vpdssaofc': vpdssaofc,
        'vpdssaofcper': vpdssaofcper,

        'vpdbltcnt': vpdbltcnt,
        'vpdblt': vpdblt,
        'vpdbltper': vpdbltper,

        'vpdringcnt': vpdringcnt,
        'vpdring': vpdring,
        'vpdringper': vpdringper,

        'vpdofeptcnt': vpdofeptcnt,
        'vpdofept': vpdofept,
        'vpdofeptper': vpdofeptper,

        'vpdtotmedia': vpdtotmedia,
        'vpdtotmediaper': vpdtotmediaper,

        'vpdpsfcnt': vpdpsfcnt,
        'vpdpsf': vpdpsf,
        'vpdpsfper': vpdpsfper,

        'vpdppfcnt': vpdppfcnt,
        'vpdppf': vpdppf,
        'vpdppfper': vpdppfper,

        'vpddgcnt': vpddgcnt,
        'vpddg': vpddg,
        'vpddgper': vpddgper,

        'vpddgbattcnt': vpddgbattcnt,
        'vpddgbatt': vpddgbatt,
        'vpddgbattper': vpddgbattper,

        'vpdlbattcnt': vpdlbattcnt,
        'vpdlbatt': vpdlbatt,
        'vpdlbattper': vpdlbattper,

        'vpdnodgcnt': vpdnodgcnt,
        'vpdnodg': vpdnodg,
        'vpdnodgper': vpdnodgper,

        'vpdnodslcnt': vpdnodslcnt,
        'vpdnodsl': vpdnodsl,
        'vpdnodslper': vpdnodslper,

        'vpdtotpwr': vpdtotpwr,
        'vpdtotpwrper': vpdtotpwrper,

        'vpdhwbtscnt': vpdhwbtscnt,
        'vpdhwbts': vpdhwbts,
        'vpdhwbtsper': vpdhwbtsper,

        'vpdmisccnt': vpdmisccnt,
        'vpdmisc': vpdmisc,
        'vpdmiscper': vpdmiscper,

        'vpdtothwmisc': vpdtothwmisc,
        'vpdtothwmiscper': vpdtothwmiscper,

        'vkttotal': vkttotal,
        'vktavg': vktavg,

        'vktstrcnt': vktstrcnt,
        'vktstrofc': vktstrofc,
        'vktstrofcper': vktstrofcper,

        'vktssacnt': vktssacnt,
        'vktssaofc': vktssaofc,
        'vktssaofcper': vktssaofcper,

        'vktbltcnt': vktbltcnt,
        'vktblt': vktblt,
        'vktbltper': vktbltper,

        'vktringcnt': vktringcnt,
        'vktring': vktring,
        'vktringper': vktringper,

        'vktofeptcnt': vktofeptcnt,
        'vktofept': vktofept,
        'vktofeptper': vktofeptper,

        'vkttotmedia': vkttotmedia,
        'vkttotmediaper': vkttotmediaper,

        'vktpsfcnt': vktpsfcnt,
        'vktpsf': vktpsf,
        'vktpsfper': vktpsfper,

        'vktppfcnt': vktppfcnt,
        'vktppf': vktppf,
        'vktppfper': vktppfper,

        'vktdgcnt': vktdgcnt,
        'vktdg': vktdg,
        'vktdgper': vktdgper,

        'vktdgbattcnt': vktdgbattcnt,
        'vktdgbatt': vktdgbatt,
        'vktdgbattper': vktdgbattper,

        'vktlbattcnt': vktlbattcnt,
        'vktlbatt': vktlbatt,
        'vktlbattper': vktlbattper,

        'vktnodgcnt': vktnodgcnt,
        'vktnodg': vktnodg,
        'vktnodgper': vktnodgper,

        'vktnodslcnt': vktnodslcnt,
        'vktnodsl': vktnodsl,
        'vktnodslper': vktnodslper,

        'vkttotpwr': vkttotpwr,
        'vkttotpwrper': vkttotpwrper,

        'vkthwbtscnt': vkthwbtscnt,
        'vkthwbts': vkthwbts,
        'vkthwbtsper': vkthwbtsper,

        'vktmisccnt': vktmisccnt,
        'vktmisc': vktmisc,
        'vktmiscper': vktmiscper,

        'vkttothwmisc': vkttothwmisc,
        'vkttothwmiscper': vkttothwmiscper,

        'grandtotstrcnt': grandtotstrcnt,
        'grandtotstroutage': grandtotstroutage,
        'grandtotstrper': grandtotstrper,

        'grandtotssacnt': grandtotssacnt,
        'grandtotssaoutage': grandtotssaoutage,
        'grandtotssaper': grandtotssaper,

        'grandtotbltcnt': grandtotbltcnt,
        'grandtotbltoutage': grandtotbltoutage,
        'grandtotbltper': grandtotbltper,

        'grandtotringcnt': grandtotringcnt,
        'grandtotringoutage': grandtotringoutage,
        'grandtotringper': grandtotringper,

        'grandtotofeptcnt': grandtotofeptcnt,
        'grandtotofeptoutage': grandtotofeptoutage,
        'grandtotofeptper': grandtotofeptper,

        'grandtotpsfcnt': grandtotpsfcnt,
        'grandtotpsfoutage': grandtotpsfoutage,
        'grandtotpsfper': grandtotpsfper,


        'grandtotppfcnt': grandtotppfcnt,
        'grandtotppfoutage': grandtotppfoutage,
        'grandtotppfper': grandtotppfper,


        'grandtotdgcnt': grandtotdgcnt,
        'grandtotdgoutage': grandtotdgoutage,
        'grandtotdgper': grandtotdgper,


        'grandtotdgbattcnt': grandtotdgbattcnt,
        'grandtotdgbattoutage': grandtotdgbattoutage,
        'grandtotdgbattper': grandtotdgbattper,


        'grandtotlbattcnt': grandtotlbattcnt,
        'grandtotlbattoutage': grandtotlbattoutage,
        'grandtotlbattper': grandtotlbattper,


        'grandtotnodgcnt': grandtotnodgcnt,
        'grandtotnodgoutage': grandtotnodgoutage,
        'grandtotnodgper': grandtotnodgper,


        'grandtotnodslcnt': grandtotnodslcnt,
        'grandtotnodsloutage': grandtotnodsloutage,
        'grandtotnodslper': grandtotnodslper,


        'grandtothwbtscnt': grandtothwbtscnt,
        'grandtothwbtsoutage': grandtothwbtsoutage,
        'grandtothwbtsper': grandtothwbtsper,


        'grandtotmisccnt': grandtotmisccnt,
        'grandtotmiscoutage': grandtotmiscoutage,
        'grandtotmiscper': grandtotmiscper,

        'mediagrandtotoutage' : mediagrandtotoutage,
        'mediagrandtotper': mediagrandtotper,

        'powergrandtotoutage': powergrandtotoutage,
        'powergrandtotper': powergrandtotper,

        'hwmiscgrandtotoutage': hwmiscgrandtotoutage,
        'hwmiscgrandtotper': hwmiscgrandtotper,

        'totaldntime': totaldntime,
        'totavgdntime': totavgdntime,


    }

    return render(request, 'interruption_analysis/2g&3g_analysis.html', context = dict2g3g)


def analysis_2g3gnsn(request):
    return render(request, 'interruption_analysis/nsn2g&3g_analysis.html')

def dt_history(request):
    return render(request, 'interruption_analysis/dt_history.html')

def repeat_faults(request):  

    result = interruptions_table.objects.values('SDCA','BTS_NAME').annotate(count=Count('BTS_NAME'), sum=Sum('DURATION')).filter(count__gt=5).order_by('-count')
    bts_list = [i['BTS_NAME'] for i in result]
    repeatdetails = interruptions_table.objects.filter(BTS_NAME__in = bts_list).order_by('BTS_NAME','-DURATION')    
    repeatdict = {'result':result ,'repeatdetails':repeatdetails}
    return render(request, 'interruption_analysis/repeat_faults.html', context= repeatdict)

def strtot(request):

        # STR OFC BREAKS QUERY

        result = interruptions_table.objects.filter(REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).order_by('-DURATION') 
        duration = interruptions_table.objects.filter(REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        total = round(duration["downtime"],2)
        return render(request, 'interruption_analysis/strtot.html', {'queryset':result,'queryset1':total} )


def ssatot(request):
    
        # SSA OFC BREAKS QUERY

        result = interruptions_table.objects.filter(REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).order_by('-DURATION') 
        duration = interruptions_table.objects.filter(REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        total = round(duration["downtime"],2)
        return render(request, 'interruption_analysis/ssatot.html', {'queryset': result, 'queryset1': total})


def blttot(request):
 
        # BLT FAULTS QUERY

        result = interruptions_table.objects.filter(REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).order_by('-DURATION') 
        duration = interruptions_table.objects.filter(REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        total = round(duration["downtime"],2)
        return render(request, 'interruption_analysis/blttot.html', {'queryset': result, 'queryset1': total})


def ringtot(request):
    
        # RING FAULTS QUERY

        result = interruptions_table.objects.filter(REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).order_by('-DURATION') 
        duration = interruptions_table.objects.filter(REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        total = round(duration["downtime"],2)
        return render(request, 'interruption_analysis/ringtot.html', {'queryset': result, 'queryset1': total})


def ofepttot(request):
    
        # OF EQPT FAULTS QUERY

        result = interruptions_table.objects.filter(REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).order_by('-DURATION') 
        duration = interruptions_table.objects.filter(REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        total = round(duration["downtime"],2)
        return render(request, 'interruption_analysis/ofepttot.html', {'queryset': result, 'queryset1': total})


def psftot(request):
    
        # PSF FAULTS QUERY

        result = interruptions_table.objects.filter(REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).order_by('-DURATION') 
        duration = interruptions_table.objects.filter(REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        total = round(duration["downtime"],2)
        return render(request, 'interruption_analysis/psftot.html', {'queryset': result, 'queryset1': total})


def ppftot(request):
    
        # PPF FAULTS QUERY

        result = interruptions_table.objects.filter(REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).order_by('-DURATION') 
        duration = interruptions_table.objects.filter(REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        total = round(duration["downtime"],2)
        return render(request, 'interruption_analysis/ppftot.html', {'queryset': result, 'queryset1': total})


def dgtot(request):
    
        # DG FAULTS QUERY

        result = interruptions_table.objects.filter(REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).order_by('-DURATION') 
        duration = interruptions_table.objects.filter(REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        total = round(duration["downtime"],2)
        return render(request, 'interruption_analysis/dgtot.html', {'queryset': result, 'queryset1': total})


def dgbatttot(request):
    
        # DG BATT FAULTS QUERY

        result = interruptions_table.objects.filter(REASON__in=['Power - DG Startup Batt Faulty']).order_by('-DURATION') 
        duration = interruptions_table.objects.filter(REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        total = round(duration["downtime"],2)
        return render(request, 'interruption_analysis/dgbatttot.html', {'queryset': result, 'queryset1': total})


def lbatttot(request):
    
        # DG LOW BATT FAULTS QUERY

        result = interruptions_table.objects.filter(REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).order_by('-DURATION') 
        duration = interruptions_table.objects.filter(REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        total = round(duration["downtime"],2)
        return render(request, 'interruption_analysis/lbatttot.html', {'queryset': result, 'queryset1': total})


def nodgtot(request):
    
        # NO DG FAULTS QUERY

        result = interruptions_table.objects.filter(REASON__in=['Power - Power Problem ,No DG']).order_by('-DURATION') 
        duration = interruptions_table.objects.filter(REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        total = round(duration["downtime"],2)
        return render(request, 'interruption_analysis/nodgtot.html', {'queryset': result, 'queryset1': total})


def nodsltot(request):
    
        # NO DIESEL FAULTS QUERY

        result = interruptions_table.objects.filter(REASON__in=['Power - Power Problem,No Diesel in D.G']).order_by('-DURATION') 
        duration = interruptions_table.objects.filter(REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        total = round(duration["downtime"],2)
        return render(request, 'interruption_analysis/nodsltot.html', {'queryset': result, 'queryset1': total})


def hwtot(request):
    
        # HW FAULTS QUERY

        result = interruptions_table.objects.filter(REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).order_by('-DURATION') 
        duration = interruptions_table.objects.filter(REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        total = round(duration["downtime"],2)
        return render(request, 'interruption_analysis/hwtot.html', {'queryset': result, 'queryset1': total})


def misctot(request):
    
        # MISC FAULTS QUERY

        result = interruptions_table.objects.filter(REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).order_by('-DURATION') 
        duration = interruptions_table.objects.filter(REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        total = round(duration["downtime"],2)
        return render(request, 'interruption_analysis/misctot.html', {'queryset': result, 'queryset1': total})


def bkkdet(request):

        # B.KOTHAKOTA STR OFC BREAKS QUERY

        strresult = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bkkstr = round(duration['downtime'],2)    

        # B.KOTHAKOTA SSA OFC BREAKS QUERY

        ssaresult = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bkkssa = round(duration['downtime'],2)    

        # B.KOTHAKOTA BUILT-UP FAULTS QUERY

        bltresult = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bkkblt = round(duration['downtime'],2) 

        # B.KOTHAKOTA OFC RING FAULTS QUERY

        ringresult = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bkkring = round(duration['downtime'],2) 

        # B.KOTHAKOTA OFC EQPT FAULTS QUERY

        ofeptresult = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bkkofept = round(duration['downtime'],2) 

        # B.KOTHAKOTA POWER SUPPLY FAULTS QUERY

        psfresult = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bkkpsf = round(duration['downtime'],2) 

        # B.KOTHAKOTA POWER PLANT FAULTS QUERY

        ppfresult = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bkkppf = round(duration['downtime'],2) 

        # B.KOTHAKOTA DG SET FAULTS QUERY

        dgresult = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bkkdg = round(duration['downtime'],2) 

        # B.KOTHAKOTA DG BATT FAULTS QUERY

        dgbattresult = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - DG Startup Batt Faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bkkdgbatt = round(duration['downtime'],2) 

        # B.KOTHAKOTA BATTERY BACKUP FAULTS QUERY

        lbattresult = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bkklbatt = round(duration['downtime'],2) 

        # B.KOTHAKOTA NO DG SET FAULTS QUERY

        nodgresult = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - Power Problem ,No DG']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bkknodg = round(duration['downtime'],2) 

        # B.KOTHAKOTA NO DIESEL FAULTS QUERY

        nodslresult = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - Power Problem,No Diesel in D.G']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bkknodsl = round(duration['downtime'],2) 

        # B.KOTHAKOTA BTS HW FAULTS QUERY

        hwresult = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bkkhw = round(duration['downtime'],2) 

        # B.KOTHAKOTA MISC FAULTS QUERY

        miscresult = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='B.KOTHAKOTA' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bkkmisc = round(duration['downtime'],2) 

        dictdet = {

        'strresult': strresult,
        'bkkstr': bkkstr,
        'ssaresult': ssaresult,
        'bkkssa': bkkssa,
        'bltresult': bltresult,
        'bkkblt': bkkblt,
        'ringresult': ringresult,
        'bkkring': bkkring,
        'ofeptresult': ofeptresult,
        'bkkofept': bkkofept,
        'psfresult': psfresult,
        'bkkpsf': bkkpsf,
        'ppfresult': ppfresult,
        'bkkppf': bkkppf,
        'dgresult': dgresult,
        'bkkdg': bkkdg,
        'dgbattresult': dgbattresult,
        'bkkdgbatt': bkkdgbatt,
        'lbattresult': lbattresult,
        'bkklbatt': bkklbatt,
        'nodgresult': nodgresult,
        'bkknodg': bkknodg,
        'nodslresult': nodslresult,
        'bkknodsl': bkknodsl,
        'hwresult': hwresult,
        'bkkhw': bkkhw,
        'miscresult': miscresult,
        'bkkmisc': bkkmisc,

        }

        return render(request, 'interruption_analysis/bkkdet.html', context = dictdet)


def bgpdet(request):

        # BANGARUPALEM STR OFC BREAKS QUERY

        strresult = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bgpstr = round(duration['downtime'],2)    

        # BANGARUPALEM SSA OFC BREAKS QUERY

        ssaresult = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bgpssa = round(duration['downtime'],2)    

        # BANGARUPALEM BUILT-UP FAULTS QUERY

        bltresult = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bgpblt = round(duration['downtime'],2) 

        # BANGARUPALEM OFC RING FAULTS QUERY

        ringresult = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bgpring = round(duration['downtime'],2) 

        # BANGARUPALEM OFC EQPT FAULTS QUERY

        ofeptresult = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bgpofept = round(duration['downtime'],2) 

        # BANGARUPALEM POWER SUPPLY FAULTS QUERY

        psfresult = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bgppsf = round(duration['downtime'],2) 

        # BANGARUPALEM POWER PLANT FAULTS QUERY

        ppfresult = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bgpppf = round(duration['downtime'],2) 

        # BANGARUPALEM DG SET FAULTS QUERY

        dgresult = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bgpdg = round(duration['downtime'],2) 

        # BANGARUPALEM DG BATT FAULTS QUERY

        dgbattresult = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - DG Startup Batt Faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bgpdgbatt = round(duration['downtime'],2) 

        # BANGARUPALEM BATTERY BACKUP FAULTS QUERY

        lbattresult = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bgplbatt = round(duration['downtime'],2) 

        # BANGARUPALEM NO DG SET FAULTS QUERY

        nodgresult = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - Power Problem ,No DG']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bgpnodg = round(duration['downtime'],2) 

        # BANGARUPALEM NO DIESEL FAULTS QUERY

        nodslresult = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - Power Problem,No Diesel in D.G']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bgpnodsl = round(duration['downtime'],2) 

        # BANGARUPALEM BTS HW FAULTS QUERY

        hwresult = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bgphw = round(duration['downtime'],2) 

        # BANGARUPALEM MISC FAULTS QUERY

        miscresult = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='BANGARUPALEM' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        bgpmisc = round(duration['downtime'],2) 

        dictdet = {

        'strresult': strresult,
        'bgpstr': bgpstr,
        'ssaresult': ssaresult,
        'bgpssa': bgpssa,
        'bltresult': bltresult,
        'bgpblt': bgpblt,
        'ringresult': ringresult,
        'bgpring': bgpring,
        'ofeptresult': ofeptresult,
        'bgpofept': bgpofept,
        'psfresult': psfresult,
        'bgppsf': bgppsf,
        'ppfresult': ppfresult,
        'bgpppf': bgpppf,
        'dgresult': dgresult,
        'bgpdg': bgpdg,
        'dgbattresult': dgbattresult,
        'bgpdgbatt': bgpdgbatt,
        'lbattresult': lbattresult,
        'bgplbatt': bgplbatt,
        'nodgresult': nodgresult,
        'bgpnodg': bgpnodg,
        'nodslresult': nodslresult,
        'bgpnodsl': bgpnodsl,
        'hwresult': hwresult,
        'bgphw': bgphw,
        'miscresult': miscresult,
        'bgpmisc': bgpmisc,

        }

        return render(request, 'interruption_analysis/bgpdet.html', context = dictdet)


def cdrdet(request):

        # CHANDRAGIRI STR OFC BREAKS QUERY

        strresult = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        cdrstr = round(duration['downtime'],2)    

        # CHANDRAGIRI SSA OFC BREAKS QUERY

        ssaresult = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        cdrssa = round(duration['downtime'],2)    

        # CHANDRAGIRI BUILT-UP FAULTS QUERY

        bltresult = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        cdrblt = round(duration['downtime'],2) 

        # CHANDRAGIRI OFC RING FAULTS QUERY

        ringresult = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        cdrring = round(duration['downtime'],2) 

        # CHANDRAGIRI OFC EQPT FAULTS QUERY

        ofeptresult = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        cdrofept = round(duration['downtime'],2) 

        # CHANDRAGIRI POWER SUPPLY FAULTS QUERY

        psfresult = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        cdrpsf = round(duration['downtime'],2) 

        # CHANDRAGIRI POWER PLANT FAULTS QUERY

        ppfresult = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        cdrppf = round(duration['downtime'],2) 

        # CHANDRAGIRI DG SET FAULTS QUERY

        dgresult = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        cdrdg = round(duration['downtime'],2) 

        # CHANDRAGIRI DG BATT FAULTS QUERY

        dgbattresult = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - DG Startup Batt Faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        cdrdgbatt = round(duration['downtime'],2) 

        # CHANDRAGIRI BATTERY BACKUP FAULTS QUERY

        lbattresult = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        cdrlbatt = round(duration['downtime'],2) 

        # CHANDRAGIRI NO DG SET FAULTS QUERY

        nodgresult = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - Power Problem ,No DG']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        cdrnodg = round(duration['downtime'],2) 

        # CHANDRAGIRI NO DIESEL FAULTS QUERY

        nodslresult = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - Power Problem,No Diesel in D.G']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        cdrnodsl = round(duration['downtime'],2) 

        # CHANDRAGIRI BTS HW FAULTS QUERY

        hwresult = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        cdrhw = round(duration['downtime'],2) 

        # CHANDRAGIRI MISC FAULTS QUERY

        miscresult = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHANDRAGIRI' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        cdrmisc = round(duration['downtime'],2) 

        dictdet = {

        'strresult': strresult,
        'cdrstr': cdrstr,
        'ssaresult': ssaresult,
        'cdrssa': cdrssa,
        'bltresult': bltresult,
        'cdrblt': cdrblt,
        'ringresult': ringresult,
        'cdrring': cdrring,
        'ofeptresult': ofeptresult,
        'cdrofept': cdrofept,
        'psfresult': psfresult,
        'cdrpsf': cdrpsf,
        'ppfresult': ppfresult,
        'cdrppf': cdrppf,
        'dgresult': dgresult,
        'cdrdg': cdrdg,
        'dgbattresult': dgbattresult,
        'cdrdgbatt': cdrdgbatt,
        'lbattresult': lbattresult,
        'cdrlbatt': cdrlbatt,
        'nodgresult': nodgresult,
        'cdrnodg': cdrnodg,
        'nodslresult': nodslresult,
        'cdrnodsl': cdrnodsl,
        'hwresult': hwresult,
        'cdrhw': cdrhw,
        'miscresult': miscresult,
        'cdrmisc': cdrmisc,

        }

        return render(request, 'interruption_analysis/cdrdet.html', context = dictdet)


def ctrdet(request):

        # CHITTOOR STR OFC BREAKS QUERY

        strresult = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ctrstr = round(duration['downtime'],2)    

        # CHITTOOR SSA OFC BREAKS QUERY

        ssaresult = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ctrssa = round(duration['downtime'],2)    

        # CHITTOOR BUILT-UP FAULTS QUERY

        bltresult = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ctrblt = round(duration['downtime'],2) 

        # CHITTOOR OFC RING FAULTS QUERY

        ringresult = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ctrring = round(duration['downtime'],2) 

        # CHITTOOR OFC EQPT FAULTS QUERY

        ofeptresult = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ctrofept = round(duration['downtime'],2) 

        # CHITTOOR POWER SUPPLY FAULTS QUERY

        psfresult = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ctrpsf = round(duration['downtime'],2) 

        # CHITTOOR POWER PLANT FAULTS QUERY

        ppfresult = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ctrppf = round(duration['downtime'],2) 

        # CHITTOOR DG SET FAULTS QUERY

        dgresult = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ctrdg = round(duration['downtime'],2) 

        # CHITTOOR DG BATT FAULTS QUERY

        dgbattresult = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - DG Startup Batt Faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ctrdgbatt = round(duration['downtime'],2) 

        # CHITTOOR BATTERY BACKUP FAULTS QUERY

        lbattresult = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ctrlbatt = round(duration['downtime'],2) 

        # CHITTOOR NO DG SET FAULTS QUERY

        nodgresult = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - Power Problem ,No DG']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ctrnodg = round(duration['downtime'],2) 

        # CHITTOOR NO DIESEL FAULTS QUERY

        nodslresult = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - Power Problem,No Diesel in D.G']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ctrnodsl = round(duration['downtime'],2) 

        # CHITTOOR BTS HW FAULTS QUERY

        hwresult = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ctrhw = round(duration['downtime'],2) 

        # CHITTOOR MISC FAULTS QUERY

        miscresult = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='CHITTOOR' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ctrmisc = round(duration['downtime'],2) 

        dictdet = {

        'strresult': strresult,
        'ctrstr': ctrstr,
        'ssaresult': ssaresult,
        'ctrssa': ctrssa,
        'bltresult': bltresult,
        'ctrblt': ctrblt,
        'ringresult': ringresult,
        'ctrring': ctrring,
        'ofeptresult': ofeptresult,
        'ctrofept': ctrofept,
        'psfresult': psfresult,
        'ctrpsf': ctrpsf,
        'ppfresult': ppfresult,
        'ctrppf': ctrppf,
        'dgresult': dgresult,
        'ctrdg': ctrdg,
        'dgbattresult': dgbattresult,
        'ctrdgbatt': ctrdgbatt,
        'lbattresult': lbattresult,
        'ctrlbatt': ctrlbatt,
        'nodgresult': nodgresult,
        'ctrnodg': ctrnodg,
        'nodslresult': nodslresult,
        'ctrnodsl': ctrnodsl,
        'hwresult': hwresult,
        'ctrhw': ctrhw,
        'miscresult': miscresult,
        'ctrmisc': ctrmisc,

        }

        return render(request, 'interruption_analysis/ctrdet.html', context = dictdet)



def kupdet(request):

        # KUPPAM STR OFC BREAKS QUERY

        strresult = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        kupstr = round(duration['downtime'],2)    

        # KUPPAM SSA OFC BREAKS QUERY

        ssaresult = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        kupssa = round(duration['downtime'],2)    

        # KUPPAM BUILT-UP FAULTS QUERY

        bltresult = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        kupblt = round(duration['downtime'],2) 

        # KUPPAM OFC RING FAULTS QUERY

        ringresult = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        kupring = round(duration['downtime'],2) 

        # KUPPAM OFC EQPT FAULTS QUERY

        ofeptresult = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        kupofept = round(duration['downtime'],2) 

        # KUPPAM POWER SUPPLY FAULTS QUERY

        psfresult = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        kuppsf = round(duration['downtime'],2) 

        # KUPPAM POWER PLANT FAULTS QUERY

        ppfresult = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        kupppf = round(duration['downtime'],2) 

        # KUPPAM DG SET FAULTS QUERY

        dgresult = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        kupdg = round(duration['downtime'],2) 

        # KUPPAM DG BATT FAULTS QUERY

        dgbattresult = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - DG Startup Batt Faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        kupdgbatt = round(duration['downtime'],2) 

        # KUPPAM BATTERY BACKUP FAULTS QUERY

        lbattresult = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        kuplbatt = round(duration['downtime'],2) 

        # KUPPAM NO DG SET FAULTS QUERY

        nodgresult = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - Power Problem ,No DG']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        kupnodg = round(duration['downtime'],2) 

        # KUPPAM NO DIESEL FAULTS QUERY

        nodslresult = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - Power Problem,No Diesel in D.G']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        kupnodsl = round(duration['downtime'],2) 

        # KUPPAM BTS HW FAULTS QUERY

        hwresult = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        kuphw = round(duration['downtime'],2) 

        # KUPPAM MISC FAULTS QUERY

        miscresult = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='KUPPAM' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        kupmisc = round(duration['downtime'],2) 

        dictdet = {

        'strresult': strresult,
        'kupstr': kupstr,
        'ssaresult': ssaresult,
        'kupssa': kupssa,
        'bltresult': bltresult,
        'kupblt': kupblt,
        'ringresult': ringresult,
        'kupring': kupring,
        'ofeptresult': ofeptresult,
        'kupofept': kupofept,
        'psfresult': psfresult,
        'kuppsf': kuppsf,
        'ppfresult': ppfresult,
        'kupppf': kupppf,
        'dgresult': dgresult,
        'kupdg': kupdg,
        'dgbattresult': dgbattresult,
        'kupdgbatt': kupdgbatt,
        'lbattresult': lbattresult,
        'kuplbatt': kuplbatt,
        'nodgresult': nodgresult,
        'kupnodg': kupnodg,
        'nodslresult': nodslresult,
        'kupnodsl': kupnodsl,
        'hwresult': hwresult,
        'kuphw': kuphw,
        'miscresult': miscresult,
        'kupmisc': kupmisc,

        }

        return render(request, 'interruption_analysis/kupdet.html', context = dictdet)



def mdpdet(request):

        # MADANAPALLI STR OFC BREAKS QUERY

        strresult = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        mdpstr = round(duration['downtime'],2)    

        # MADANAPALLI SSA OFC BREAKS QUERY

        ssaresult = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        mdpssa = round(duration['downtime'],2)    

        # MADANAPALLI BUILT-UP FAULTS QUERY

        bltresult = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        mdpblt = round(duration['downtime'],2) 

        # MADANAPALLI OFC RING FAULTS QUERY

        ringresult = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        mdpring = round(duration['downtime'],2) 

        # MADANAPALLI OFC EQPT FAULTS QUERY

        ofeptresult = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        mdpofept = round(duration['downtime'],2) 

        # MADANAPALLI POWER SUPPLY FAULTS QUERY

        psfresult = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        mdppsf = round(duration['downtime'],2) 

        # MADANAPALLI POWER PLANT FAULTS QUERY

        ppfresult = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        mdpppf = round(duration['downtime'],2) 

        # MADANAPALLI DG SET FAULTS QUERY

        dgresult = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        mdpdg = round(duration['downtime'],2) 

        # MADANAPALLI DG BATT FAULTS QUERY

        dgbattresult = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - DG Startup Batt Faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        mdpdgbatt = round(duration['downtime'],2) 

        # MADANAPALLI BATTERY BACKUP FAULTS QUERY

        lbattresult = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        mdplbatt = round(duration['downtime'],2) 

        # MADANAPALLI NO DG SET FAULTS QUERY

        nodgresult = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - Power Problem ,No DG']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        mdpnodg = round(duration['downtime'],2) 

        # MADANAPALLI NO DIESEL FAULTS QUERY

        nodslresult = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - Power Problem,No Diesel in D.G']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        mdpnodsl = round(duration['downtime'],2) 

        # MADANAPALLI BTS HW FAULTS QUERY

        hwresult = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        mdphw = round(duration['downtime'],2) 

        # MADANAPALLI MISC FAULTS QUERY

        miscresult = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='MADANAPALLI' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        mdpmisc = round(duration['downtime'],2) 

        dictdet = {

        'strresult': strresult,
        'mdpstr': mdpstr,
        'ssaresult': ssaresult,
        'mdpssa': mdpssa,
        'bltresult': bltresult,
        'mdpblt': mdpblt,
        'ringresult': ringresult,
        'mdpring': mdpring,
        'ofeptresult': ofeptresult,
        'mdpofept': mdpofept,
        'psfresult': psfresult,
        'mdppsf': mdppsf,
        'ppfresult': ppfresult,
        'mdpppf': mdpppf,
        'dgresult': dgresult,
        'mdpdg': mdpdg,
        'dgbattresult': dgbattresult,
        'mdpdgbatt': mdpdgbatt,
        'lbattresult': lbattresult,
        'mdplbatt': mdplbatt,
        'nodgresult': nodgresult,
        'mdpnodg': mdpnodg,
        'nodslresult': nodslresult,
        'mdpnodsl': mdpnodsl,
        'hwresult': hwresult,
        'mdphw': mdphw,
        'miscresult': miscresult,
        'mdpmisc': mdpmisc,

        }

        return render(request, 'interruption_analysis/mdpdet.html', context = dictdet)


def pakdet(request):

        # PAKALA STR OFC BREAKS QUERY

        strresult = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pakstr = round(duration['downtime'],2)    

        # PAKALA SSA OFC BREAKS QUERY

        ssaresult = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pakssa = round(duration['downtime'],2)    

        # PAKALA BUILT-UP FAULTS QUERY

        bltresult = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pakblt = round(duration['downtime'],2) 

        # PAKALA OFC RING FAULTS QUERY

        ringresult = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pakring = round(duration['downtime'],2) 

        # PAKALA OFC EQPT FAULTS QUERY

        ofeptresult = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pakofept = round(duration['downtime'],2) 

        # PAKALA POWER SUPPLY FAULTS QUERY

        psfresult = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pakpsf = round(duration['downtime'],2) 

        # PAKALA POWER PLANT FAULTS QUERY

        ppfresult = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pakppf = round(duration['downtime'],2) 

        # PAKALA DG SET FAULTS QUERY

        dgresult = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pakdg = round(duration['downtime'],2) 

        # PAKALA DG BATT FAULTS QUERY

        dgbattresult = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - DG Startup Batt Faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pakdgbatt = round(duration['downtime'],2) 

        # PAKALA BATTERY BACKUP FAULTS QUERY

        lbattresult = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        paklbatt = round(duration['downtime'],2) 

        # PAKALA NO DG SET FAULTS QUERY

        nodgresult = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - Power Problem ,No DG']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        paknodg = round(duration['downtime'],2) 

        # PAKALA NO DIESEL FAULTS QUERY

        nodslresult = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - Power Problem,No Diesel in D.G']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        paknodsl = round(duration['downtime'],2) 

        # PAKALA BTS HW FAULTS QUERY

        hwresult = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pakhw = round(duration['downtime'],2) 

        # PAKALA MISC FAULTS QUERY

        miscresult = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PAKALA' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pakmisc = round(duration['downtime'],2) 

        dictdet = {

        'strresult': strresult,
        'pakstr': pakstr,
        'ssaresult': ssaresult,
        'pakssa': pakssa,
        'bltresult': bltresult,
        'pakblt': pakblt,
        'ringresult': ringresult,
        'pakring': pakring,
        'ofeptresult': ofeptresult,
        'pakofept': pakofept,
        'psfresult': psfresult,
        'pakpsf': pakpsf,
        'ppfresult': ppfresult,
        'pakppf': pakppf,
        'dgresult': dgresult,
        'pakdg': pakdg,
        'dgbattresult': dgbattresult,
        'pakdgbatt': pakdgbatt,
        'lbattresult': lbattresult,
        'paklbatt': paklbatt,
        'nodgresult': nodgresult,
        'paknodg': paknodg,
        'nodslresult': nodslresult,
        'paknodsl': paknodsl,
        'hwresult': hwresult,
        'pakhw': pakhw,
        'miscresult': miscresult,
        'pakmisc': pakmisc,

        }

        return render(request, 'interruption_analysis/pakdet.html', context = dictdet)


def plmdet(request):

        # PALAMANER STR OFC BREAKS QUERY

        strresult = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plmstr = round(duration['downtime'],2)    

        # PALAMANER SSA OFC BREAKS QUERY

        ssaresult = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plmssa = round(duration['downtime'],2)    

        # PALAMANER BUILT-UP FAULTS QUERY

        bltresult = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plmblt = round(duration['downtime'],2) 

        # PALAMANER OFC RING FAULTS QUERY

        ringresult = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plmring = round(duration['downtime'],2) 

        # PALAMANER OFC EQPT FAULTS QUERY

        ofeptresult = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plmofept = round(duration['downtime'],2) 

        # PALAMANER POWER SUPPLY FAULTS QUERY

        psfresult = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plmpsf = round(duration['downtime'],2) 

        # PALAMANER POWER PLANT FAULTS QUERY

        ppfresult = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plmppf = round(duration['downtime'],2) 

        # PALAMANER DG SET FAULTS QUERY

        dgresult = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plmdg = round(duration['downtime'],2) 

        # PALAMANER DG BATT FAULTS QUERY

        dgbattresult = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - DG Startup Batt Faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plmdgbatt = round(duration['downtime'],2) 

        # PALAMANER BATTERY BACKUP FAULTS QUERY

        lbattresult = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plmlbatt = round(duration['downtime'],2) 

        # PALAMANER NO DG SET FAULTS QUERY

        nodgresult = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - Power Problem ,No DG']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plmnodg = round(duration['downtime'],2) 

        # PALAMANER NO DIESEL FAULTS QUERY

        nodslresult = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - Power Problem,No Diesel in D.G']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plmnodsl = round(duration['downtime'],2) 

        # PALAMANER BTS HW FAULTS QUERY

        hwresult = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plmhw = round(duration['downtime'],2) 

        # PALAMANER MISC FAULTS QUERY

        miscresult = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PALAMANER' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plmmisc = round(duration['downtime'],2) 

        dictdet = {

        'strresult': strresult,
        'plmstr': plmstr,
        'ssaresult': ssaresult,
        'plmssa': plmssa,
        'bltresult': bltresult,
        'plmblt': plmblt,
        'ringresult': ringresult,
        'plmring': plmring,
        'ofeptresult': ofeptresult,
        'plmofept': plmofept,
        'psfresult': psfresult,
        'plmpsf': plmpsf,
        'ppfresult': ppfresult,
        'plmppf': plmppf,
        'dgresult': dgresult,
        'plmdg': plmdg,
        'dgbattresult': dgbattresult,
        'plmdgbatt': plmdgbatt,
        'lbattresult': lbattresult,
        'plmlbatt': plmlbatt,
        'nodgresult': nodgresult,
        'plmnodg': plmnodg,
        'nodslresult': nodslresult,
        'plmnodsl': plmnodsl,
        'hwresult': hwresult,
        'plmhw': plmhw,
        'miscresult': miscresult,
        'plmmisc': plmmisc,

        }

        return render(request, 'interruption_analysis/plmdet.html', context = dictdet)



def plrdet(request):

        # PILER STR OFC BREAKS QUERY

        strresult = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plrstr = round(duration['downtime'],2)    

        # PILER SSA OFC BREAKS QUERY

        ssaresult = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plrssa = round(duration['downtime'],2)    

        # PILER BUILT-UP FAULTS QUERY

        bltresult = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plrblt = round(duration['downtime'],2) 

        # PILER OFC RING FAULTS QUERY

        ringresult = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plrring = round(duration['downtime'],2) 

        # PILER OFC EQPT FAULTS QUERY

        ofeptresult = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plrofept = round(duration['downtime'],2) 

        # PILER POWER SUPPLY FAULTS QUERY

        psfresult = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plrpsf = round(duration['downtime'],2) 

        # PILER POWER PLANT FAULTS QUERY

        ppfresult = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plrppf = round(duration['downtime'],2) 

        # PILER DG SET FAULTS QUERY

        dgresult = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plrdg = round(duration['downtime'],2) 

        # PILER DG BATT FAULTS QUERY

        dgbattresult = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - DG Startup Batt Faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plrdgbatt = round(duration['downtime'],2) 

        # PILER BATTERY BACKUP FAULTS QUERY

        lbattresult = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plrlbatt = round(duration['downtime'],2) 

        # PILER NO DG SET FAULTS QUERY

        nodgresult = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - Power Problem ,No DG']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plrnodg = round(duration['downtime'],2) 

        # PILER NO DIESEL FAULTS QUERY

        nodslresult = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - Power Problem,No Diesel in D.G']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plrnodsl = round(duration['downtime'],2) 

        # PILER BTS HW FAULTS QUERY

        hwresult = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plrhw = round(duration['downtime'],2) 

        # PILER MISC FAULTS QUERY

        miscresult = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PILER' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        plrmisc = round(duration['downtime'],2) 

        dictdet = {

        'strresult': strresult,
        'plrstr': plrstr,
        'ssaresult': ssaresult,
        'plrssa': plrssa,
        'bltresult': bltresult,
        'plrblt': plrblt,
        'ringresult': ringresult,
        'plrring': plrring,
        'ofeptresult': ofeptresult,
        'plrofept': plrofept,
        'psfresult': psfresult,
        'plrpsf': plrpsf,
        'ppfresult': ppfresult,
        'plrppf': plrppf,
        'dgresult': dgresult,
        'plrdg': plrdg,
        'dgbattresult': dgbattresult,
        'plrdgbatt': plrdgbatt,
        'lbattresult': lbattresult,
        'plrlbatt': plrlbatt,
        'nodgresult': nodgresult,
        'plrnodg': plrnodg,
        'nodslresult': nodslresult,
        'plrnodsl': plrnodsl,
        'hwresult': hwresult,
        'plrhw': plrhw,
        'miscresult': miscresult,
        'plrmisc': plrmisc,

        }

        return render(request, 'interruption_analysis/plrdet.html', context = dictdet)



def pgrdet(request):

        # PUNGANUR STR OFC BREAKS QUERY

        strresult = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pgrstr = round(duration['downtime'],2)    

        # PUNGANUR SSA OFC BREAKS QUERY

        ssaresult = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pgrssa = round(duration['downtime'],2)    

        # PUNGANUR BUILT-UP FAULTS QUERY

        bltresult = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pgrblt = round(duration['downtime'],2) 

        # PUNGANUR OFC RING FAULTS QUERY

        ringresult = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pgrring = round(duration['downtime'],2) 

        # PUNGANUR OFC EQPT FAULTS QUERY

        ofeptresult = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pgrofept = round(duration['downtime'],2) 

        # PUNGANUR POWER SUPPLY FAULTS QUERY

        psfresult = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pgrpsf = round(duration['downtime'],2) 

        # PUNGANUR POWER PLANT FAULTS QUERY

        ppfresult = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pgrppf = round(duration['downtime'],2) 

        # PUNGANUR DG SET FAULTS QUERY

        dgresult = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pgrdg = round(duration['downtime'],2) 

        # PUNGANUR DG BATT FAULTS QUERY

        dgbattresult = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - DG Startup Batt Faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pgrdgbatt = round(duration['downtime'],2) 

        # PUNGANUR BATTERY BACKUP FAULTS QUERY

        lbattresult = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pgrlbatt = round(duration['downtime'],2) 

        # PUNGANUR NO DG SET FAULTS QUERY

        nodgresult = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - Power Problem ,No DG']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pgrnodg = round(duration['downtime'],2) 

        # PUNGANUR NO DIESEL FAULTS QUERY

        nodslresult = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - Power Problem,No Diesel in D.G']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pgrnodsl = round(duration['downtime'],2) 

        # PUNGANUR BTS HW FAULTS QUERY

        hwresult = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pgrhw = round(duration['downtime'],2) 

        # PUNGANUR MISC FAULTS QUERY

        miscresult = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUNGANUR' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        pgrmisc = round(duration['downtime'],2) 

        dictdet = {

        'strresult': strresult,
        'pgrstr': pgrstr,
        'ssaresult': ssaresult,
        'pgrssa': pgrssa,
        'bltresult': bltresult,
        'pgrblt': pgrblt,
        'ringresult': ringresult,
        'pgrring': pgrring,
        'ofeptresult': ofeptresult,
        'pgrofept': pgrofept,
        'psfresult': psfresult,
        'pgrpsf': pgrpsf,
        'ppfresult': ppfresult,
        'pgrppf': pgrppf,
        'dgresult': dgresult,
        'pgrdg': pgrdg,
        'dgbattresult': dgbattresult,
        'pgrdgbatt': pgrdgbatt,
        'lbattresult': lbattresult,
        'pgrlbatt': pgrlbatt,
        'nodgresult': nodgresult,
        'pgrnodg': pgrnodg,
        'nodslresult': nodslresult,
        'pgrnodsl': pgrnodsl,
        'hwresult': hwresult,
        'pgrhw': pgrhw,
        'miscresult': miscresult,
        'pgrmisc': pgrmisc,

        }

        return render(request, 'interruption_analysis/pgrdet.html', context = dictdet)



def ptrdet(request):

        # PUTTUR STR OFC BREAKS QUERY

        strresult = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ptrstr = round(duration['downtime'],2)    

        # PUTTUR SSA OFC BREAKS QUERY

        ssaresult = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ptrssa = round(duration['downtime'],2)    

        # PUTTUR BUILT-UP FAULTS QUERY

        bltresult = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ptrblt = round(duration['downtime'],2) 

        # PUTTUR OFC RING FAULTS QUERY

        ringresult = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ptrring = round(duration['downtime'],2) 

        # PUTTUR OFC EQPT FAULTS QUERY

        ofeptresult = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ptrofept = round(duration['downtime'],2) 

        # PUTTUR POWER SUPPLY FAULTS QUERY

        psfresult = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ptrpsf = round(duration['downtime'],2) 

        # PUTTUR POWER PLANT FAULTS QUERY

        ppfresult = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ptrppf = round(duration['downtime'],2) 

        # PUTTUR DG SET FAULTS QUERY

        dgresult = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ptrdg = round(duration['downtime'],2) 

        # PUTTUR DG BATT FAULTS QUERY

        dgbattresult = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - DG Startup Batt Faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ptrdgbatt = round(duration['downtime'],2) 

        # PUTTUR BATTERY BACKUP FAULTS QUERY

        lbattresult = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ptrlbatt = round(duration['downtime'],2) 

        # PUTTUR NO DG SET FAULTS QUERY

        nodgresult = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - Power Problem ,No DG']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ptrnodg = round(duration['downtime'],2) 

        # PUTTUR NO DIESEL FAULTS QUERY

        nodslresult = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - Power Problem,No Diesel in D.G']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ptrnodsl = round(duration['downtime'],2) 

        # PUTTUR BTS HW FAULTS QUERY

        hwresult = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ptrhw = round(duration['downtime'],2) 

        # PUTTUR MISC FAULTS QUERY

        miscresult = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='PUTTUR' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        ptrmisc = round(duration['downtime'],2) 

        dictdet = {

        'strresult': strresult,
        'ptrstr': ptrstr,
        'ssaresult': ssaresult,
        'ptrssa': ptrssa,
        'bltresult': bltresult,
        'ptrblt': ptrblt,
        'ringresult': ringresult,
        'ptrring': ptrring,
        'ofeptresult': ofeptresult,
        'ptrofept': ptrofept,
        'psfresult': psfresult,
        'ptrpsf': ptrpsf,
        'ppfresult': ppfresult,
        'ptrppf': ptrppf,
        'dgresult': dgresult,
        'ptrdg': ptrdg,
        'dgbattresult': dgbattresult,
        'ptrdgbatt': ptrdgbatt,
        'lbattresult': lbattresult,
        'ptrlbatt': ptrlbatt,
        'nodgresult': nodgresult,
        'ptrnodg': ptrnodg,
        'nodslresult': nodslresult,
        'ptrnodsl': ptrnodsl,
        'hwresult': hwresult,
        'ptrhw': ptrhw,
        'miscresult': miscresult,
        'ptrmisc': ptrmisc,

        }

        return render(request, 'interruption_analysis/ptrdet.html', context = dictdet)



def svddet(request):

        # SATYAVEDU STR OFC BREAKS QUERY

        strresult = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        svdstr = round(duration['downtime'],2)    

        # SATYAVEDU SSA OFC BREAKS QUERY

        ssaresult = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        svdssa = round(duration['downtime'],2)    

        # SATYAVEDU BUILT-UP FAULTS QUERY

        bltresult = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        svdblt = round(duration['downtime'],2) 

        # SATYAVEDU OFC RING FAULTS QUERY

        ringresult = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        svdring = round(duration['downtime'],2) 

        # SATYAVEDU OFC EQPT FAULTS QUERY

        ofeptresult = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        svdofept = round(duration['downtime'],2) 

        # SATYAVEDU POWER SUPPLY FAULTS QUERY

        psfresult = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        svdpsf = round(duration['downtime'],2) 

        # SATYAVEDU POWER PLANT FAULTS QUERY

        ppfresult = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        svdppf = round(duration['downtime'],2) 

        # SATYAVEDU DG SET FAULTS QUERY

        dgresult = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        svddg = round(duration['downtime'],2) 

        # SATYAVEDU DG BATT FAULTS QUERY

        dgbattresult = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - DG Startup Batt Faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        svddgbatt = round(duration['downtime'],2) 

        # SATYAVEDU BATTERY BACKUP FAULTS QUERY

        lbattresult = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        svdlbatt = round(duration['downtime'],2) 

        # SATYAVEDU NO DG SET FAULTS QUERY

        nodgresult = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - Power Problem ,No DG']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        svdnodg = round(duration['downtime'],2) 

        # SATYAVEDU NO DIESEL FAULTS QUERY

        nodslresult = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - Power Problem,No Diesel in D.G']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        svdnodsl = round(duration['downtime'],2) 

        # SATYAVEDU BTS HW FAULTS QUERY

        hwresult = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        svdhw = round(duration['downtime'],2) 

        # SATYAVEDU MISC FAULTS QUERY

        miscresult = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SATYAVEDU' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        svdmisc = round(duration['downtime'],2) 

        dictdet = {

        'strresult': strresult,
        'svdstr': svdstr,
        'ssaresult': ssaresult,
        'svdssa': svdssa,
        'bltresult': bltresult,
        'svdblt': svdblt,
        'ringresult': ringresult,
        'svdring': svdring,
        'ofeptresult': ofeptresult,
        'svdofept': svdofept,
        'psfresult': psfresult,
        'svdpsf': svdpsf,
        'ppfresult': ppfresult,
        'svdppf': svdppf,
        'dgresult': dgresult,
        'svddg': svddg,
        'dgbattresult': dgbattresult,
        'svddgbatt': svddgbatt,
        'lbattresult': lbattresult,
        'svdlbatt': svdlbatt,
        'nodgresult': nodgresult,
        'svdnodg': svdnodg,
        'nodslresult': nodslresult,
        'svdnodsl': svdnodsl,
        'hwresult': hwresult,
        'svdhw': svdhw,
        'miscresult': miscresult,
        'svdmisc': svdmisc,

        }

        return render(request, 'interruption_analysis/svddet.html', context = dictdet)



def sdmdet(request):

        # SODAM STR OFC BREAKS QUERY

        strresult = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        sdmstr = round(duration['downtime'],2)    

        # SODAM SSA OFC BREAKS QUERY

        ssaresult = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        sdmssa = round(duration['downtime'],2)    

        # SODAM BUILT-UP FAULTS QUERY

        bltresult = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        sdmblt = round(duration['downtime'],2) 

        # SODAM OFC RING FAULTS QUERY

        ringresult = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        sdmring = round(duration['downtime'],2) 

        # SODAM OFC EQPT FAULTS QUERY

        ofeptresult = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        sdmofept = round(duration['downtime'],2) 

        # SODAM POWER SUPPLY FAULTS QUERY

        psfresult = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        sdmpsf = round(duration['downtime'],2) 

        # SODAM POWER PLANT FAULTS QUERY

        ppfresult = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        sdmppf = round(duration['downtime'],2) 

        # SODAM DG SET FAULTS QUERY

        dgresult = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        sdmdg = round(duration['downtime'],2) 

        # SODAM DG BATT FAULTS QUERY

        dgbattresult = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - DG Startup Batt Faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        sdmdgbatt = round(duration['downtime'],2) 

        # SODAM BATTERY BACKUP FAULTS QUERY

        lbattresult = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        sdmlbatt = round(duration['downtime'],2) 

        # SODAM NO DG SET FAULTS QUERY

        nodgresult = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - Power Problem ,No DG']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        sdmnodg = round(duration['downtime'],2) 

        # SODAM NO DIESEL FAULTS QUERY

        nodslresult = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - Power Problem,No Diesel in D.G']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        sdmnodsl = round(duration['downtime'],2) 

        # SODAM BTS HW FAULTS QUERY

        hwresult = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        sdmhw = round(duration['downtime'],2) 

        # SODAM MISC FAULTS QUERY

        miscresult = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SODAM' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        sdmmisc = round(duration['downtime'],2) 

        dictdet = {

        'strresult': strresult,
        'sdmstr': sdmstr,
        'ssaresult': ssaresult,
        'sdmssa': sdmssa,
        'bltresult': bltresult,
        'sdmblt': sdmblt,
        'ringresult': ringresult,
        'sdmring': sdmring,
        'ofeptresult': ofeptresult,
        'sdmofept': sdmofept,
        'psfresult': psfresult,
        'sdmpsf': sdmpsf,
        'ppfresult': ppfresult,
        'sdmppf': sdmppf,
        'dgresult': dgresult,
        'sdmdg': sdmdg,
        'dgbattresult': dgbattresult,
        'sdmdgbatt': sdmdgbatt,
        'lbattresult': lbattresult,
        'sdmlbatt': sdmlbatt,
        'nodgresult': nodgresult,
        'sdmnodg': sdmnodg,
        'nodslresult': nodslresult,
        'sdmnodsl': sdmnodsl,
        'hwresult': hwresult,
        'sdmhw': sdmhw,
        'miscresult': miscresult,
        'sdmmisc': sdmmisc,

        }

        return render(request, 'interruption_analysis/sdmdet.html', context = dictdet)


def skhtdet(request):

        # SRIKALAHASTI STR OFC BREAKS QUERY

        strresult = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        skhtstr = round(duration['downtime'],2)    

        # SRIKALAHASTI SSA OFC BREAKS QUERY

        ssaresult = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        skhtssa = round(duration['downtime'],2)    

        # SRIKALAHASTI BUILT-UP FAULTS QUERY

        bltresult = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        skhtblt = round(duration['downtime'],2) 

        # SRIKALAHASTI OFC RING FAULTS QUERY

        ringresult = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        skhtring = round(duration['downtime'],2) 

        # SRIKALAHASTI OFC EQPT FAULTS QUERY

        ofeptresult = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        skhtofept = round(duration['downtime'],2) 

        # SRIKALAHASTI POWER SUPPLY FAULTS QUERY

        psfresult = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        skhtpsf = round(duration['downtime'],2) 

        # SRIKALAHASTI POWER PLANT FAULTS QUERY

        ppfresult = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        skhtppf = round(duration['downtime'],2) 

        # SRIKALAHASTI DG SET FAULTS QUERY

        dgresult = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        skhtdg = round(duration['downtime'],2) 

        # SRIKALAHASTI DG BATT FAULTS QUERY

        dgbattresult = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - DG Startup Batt Faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        skhtdgbatt = round(duration['downtime'],2) 

        # SRIKALAHASTI BATTERY BACKUP FAULTS QUERY

        lbattresult = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        skhtlbatt = round(duration['downtime'],2) 

        # SRIKALAHASTI NO DG SET FAULTS QUERY

        nodgresult = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - Power Problem ,No DG']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        skhtnodg = round(duration['downtime'],2) 

        # SRIKALAHASTI NO DIESEL FAULTS QUERY

        nodslresult = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - Power Problem,No Diesel in D.G']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        skhtnodsl = round(duration['downtime'],2) 

        # SRIKALAHASTI BTS HW FAULTS QUERY

        hwresult = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        skhthw = round(duration['downtime'],2) 

        # SRIKALAHASTI MISC FAULTS QUERY

        miscresult = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='SRIKALAHASTI' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        skhtmisc = round(duration['downtime'],2) 

        dictdet = {

        'strresult': strresult,
        'skhtstr': skhtstr,
        'ssaresult': ssaresult,
        'skhtssa': skhtssa,
        'bltresult': bltresult,
        'skhtblt': skhtblt,
        'ringresult': ringresult,
        'skhtring': skhtring,
        'ofeptresult': ofeptresult,
        'skhtofept': skhtofept,
        'psfresult': psfresult,
        'skhtpsf': skhtpsf,
        'ppfresult': ppfresult,
        'skhtppf': skhtppf,
        'dgresult': dgresult,
        'skhtdg': skhtdg,
        'dgbattresult': dgbattresult,
        'skhtdgbatt': skhtdgbatt,
        'lbattresult': lbattresult,
        'skhtlbatt': skhtlbatt,
        'nodgresult': nodgresult,
        'skhtnodg': skhtnodg,
        'nodslresult': nodslresult,
        'skhtnodsl': skhtnodsl,
        'hwresult': hwresult,
        'skhthw': skhthw,
        'miscresult': miscresult,
        'skhtmisc': skhtmisc,

        }

        return render(request, 'interruption_analysis/skhtdet.html', context = dictdet)



def vpddet(request):

        # VAYALPADU STR OFC BREAKS QUERY

        strresult = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vpdstr = round(duration['downtime'],2)    

        # VAYALPADU SSA OFC BREAKS QUERY

        ssaresult = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vpdssa = round(duration['downtime'],2)    

        # VAYALPADU BUILT-UP FAULTS QUERY

        bltresult = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vpdblt = round(duration['downtime'],2) 

        # VAYALPADU OFC RING FAULTS QUERY

        ringresult = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vpdring = round(duration['downtime'],2) 

        # VAYALPADU OFC EQPT FAULTS QUERY

        ofeptresult = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vpdofept = round(duration['downtime'],2) 

        # VAYALPADU POWER SUPPLY FAULTS QUERY

        psfresult = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vpdpsf = round(duration['downtime'],2) 

        # VAYALPADU POWER PLANT FAULTS QUERY

        ppfresult = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vpdppf = round(duration['downtime'],2) 

        # VAYALPADU DG SET FAULTS QUERY

        dgresult = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vpddg = round(duration['downtime'],2) 

        # VAYALPADU DG BATT FAULTS QUERY

        dgbattresult = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - DG Startup Batt Faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vpddgbatt = round(duration['downtime'],2) 

        # VAYALPADU BATTERY BACKUP FAULTS QUERY

        lbattresult = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vpdlbatt = round(duration['downtime'],2) 

        # VAYALPADU NO DG SET FAULTS QUERY

        nodgresult = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - Power Problem ,No DG']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vpdnodg = round(duration['downtime'],2) 

        # VAYALPADU NO DIESEL FAULTS QUERY

        nodslresult = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - Power Problem,No Diesel in D.G']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vpdnodsl = round(duration['downtime'],2) 

        # VAYALPADU BTS HW FAULTS QUERY

        hwresult = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vpdhw = round(duration['downtime'],2) 

        # VAYALPADU MISC FAULTS QUERY

        miscresult = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VAYALPADU' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vpdmisc = round(duration['downtime'],2) 

        dictdet = {

        'strresult': strresult,
        'vpdstr': vpdstr,
        'ssaresult': ssaresult,
        'vpdssa': vpdssa,
        'bltresult': bltresult,
        'vpdblt': vpdblt,
        'ringresult': ringresult,
        'vpdring': vpdring,
        'ofeptresult': ofeptresult,
        'vpdofept': vpdofept,
        'psfresult': psfresult,
        'vpdpsf': vpdpsf,
        'ppfresult': ppfresult,
        'vpdppf': vpdppf,
        'dgresult': dgresult,
        'vpddg': vpddg,
        'dgbattresult': dgbattresult,
        'vpddgbatt': vpddgbatt,
        'lbattresult': lbattresult,
        'vpdlbatt': vpdlbatt,
        'nodgresult': nodgresult,
        'vpdnodg': vpdnodg,
        'nodslresult': nodslresult,
        'vpdnodsl': vpdnodsl,
        'hwresult': hwresult,
        'vpdhw': vpdhw,
        'miscresult': miscresult,
        'vpdmisc': vpdmisc,

        }

        return render(request, 'interruption_analysis/vpddet.html', context = dictdet)



def vktdet(request):

        # VENKATAGIRIKOTA STR OFC BREAKS QUERY

        strresult = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Media - STR&SSA  OFC Double Break','Media - STR Linear OFC Break','Media - STR Double OFC Break','Media - STR OFC Break','Media - OFC Double Cut','Media - STR Double OFC Break','Media - STR Linear OFC Break','Media - STR&SSA OFC Double Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vktstr = round(duration['downtime'],2)    

        # VENKATAGIRIKOTA SSA OFC BREAKS QUERY

        ssaresult = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Media - SSA OFC Break','Media - OTHER SSA OFC Break','Media - RPR Media Break']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vktssa = round(duration['downtime'],2)    

        # VENKATAGIRIKOTA BUILT-UP FAULTS QUERY

        bltresult = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Media - Rat Bite','Media - Private Leased in Fiber Break','Media - Fibre Patch cords problem','Media - DSLAM Media Break','Media - Loss in Fiber','Misc - Built-up-Fault','Media - DMW Link Problem','Media - Stream Problem','Media - DSLAM Media Break','Media - Fibre Patch cords problem','Media - Loss in Fiber','Media - Media issue at Built up site','Media - Private Leased in Fiber Break','Media - Rat Bite','Misc - Built-up-Media-Fault','Misc - Built-up-Power-Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vktblt = round(duration['downtime'],2) 

        # VENKATAGIRIKOTA OFC RING FAULTS QUERY

        ringresult = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Media - OFC Ring Problem','Media - RPR Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vktring = round(duration['downtime'],2) 

        # VENKATAGIRIKOTA OFC EQPT FAULTS QUERY

        ofeptresult = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Misc - DSLAM HW FAULT','Media - CPE Problem','Media - DMW System Fault','Media - DSLAM OCLAN FAULT','Media - GE Port Problem','Media - LAN Switch Problem','Media - MADM System Problem','Media - OFC System Fault','Media - Optical Modem Fault','Media - Radio modem fault','Media - CPAN Port Problem','Media - CPAN Ring Problem']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vktofept = round(duration['downtime'],2) 

        # VENKATAGIRIKOTA POWER SUPPLY FAULTS QUERY

        psfresult = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - APSEB Dis due to NP','Power - APSEB Exntension Problem','Power - HT Fuse Fault','Power - I/C supply fault','Power - MCB Tripped','Power - Transformer Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vktpsf = round(duration['downtime'],2) 

        # VENKATAGIRIKOTA POWER PLANT FAULTS QUERY

        ppfresult = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - Power Plant Modules Fault','Infra - Power Plant faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vktppf = round(duration['downtime'],2) 

        # VENKATAGIRIKOTA DG SET FAULTS QUERY

        dgresult = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - DG Faulty','Power - DG Manual','Power - DG Not started']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vktdg = round(duration['downtime'],2) 

        # VENKATAGIRIKOTA DG BATT FAULTS QUERY

        dgbattresult = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - DG Startup Batt Faulty']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - DG Startup Batt Faulty']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vktdgbatt = round(duration['downtime'],2) 

        # VENKATAGIRIKOTA BATTERY BACKUP FAULTS QUERY

        lbattresult = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - Low Battery Backup','Power - BTS/NodeB Siwtched off due to Low batt backup','Power - BTS/NodeB Switched off']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vktlbatt = round(duration['downtime'],2) 

        # VENKATAGIRIKOTA NO DG SET FAULTS QUERY

        nodgresult = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - Power Problem ,No DG']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - Power Problem ,No DG']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vktnodg = round(duration['downtime'],2) 

        # VENKATAGIRIKOTA NO DIESEL FAULTS QUERY

        nodslresult = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - Power Problem,No Diesel in D.G']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Power - Power Problem,No Diesel in D.G']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vktnodsl = round(duration['downtime'],2) 

        # VENKATAGIRIKOTA BTS HW FAULTS QUERY

        hwresult = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Misc - Sector Fault','Hardware - BTS/NodeB  Hanged','Hardware - BTS/NodeB Hanged','Hardware - BTS/NodeB Hardware Fault','Misc - BSC H_W Problem','Media - CPRI Cable Fault']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vkthw = round(duration['downtime'],2) 

        # VENKATAGIRIKOTA MISC FAULTS QUERY

        miscresult = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).order_by('-DURATION')
        duration = interruptions_table.objects.filter(SDCA='VENKATAGIRIKOTA' , REASON__in=['Misc - IP Vendor Infra/Power Fault','Infra - AC Units Faulty','Misc - BTS Re-homed','Misc - BTS Swaped','Misc - BTS Switched off for n/w optimization','Misc - BTS/NodeB Switched Off','Misc - Down due to Cyclone','Misc - Down due to Floods','Misc - Maintenace Work','Misc - Owner Issue','Misc - RF Cable Theft','Misc - Site DOWN or CLOSED due to IP Issue','Misc - Tower Fallen','Software - BTS/NodeB S/W Corrupted','Infra - Room temp high, BTS Malfunctioning','Infra - Room temp high, Tx system Malfunctioning','Infra - Room Temp high,Tx system/IDU Hanged','Misc - Site Integration Pending','Update','']).aggregate(downtime=Coalesce(Sum('DURATION'),0))
        vktmisc = round(duration['downtime'],2) 

        dictdet = {

        'strresult': strresult,
        'vktstr': vktstr,
        'ssaresult': ssaresult,
        'vktssa': vktssa,
        'bltresult': bltresult,
        'vktblt': vktblt,
        'ringresult': ringresult,
        'vktring': vktring,
        'ofeptresult': ofeptresult,
        'vktofept': vktofept,
        'psfresult': psfresult,
        'vktpsf': vktpsf,
        'ppfresult': ppfresult,
        'vktppf': vktppf,
        'dgresult': dgresult,
        'vktdg': vktdg,
        'dgbattresult': dgbattresult,
        'vktdgbatt': vktdgbatt,
        'lbattresult': lbattresult,
        'vktlbatt': vktlbatt,
        'nodgresult': nodgresult,
        'vktnodg': vktnodg,
        'nodslresult': nodslresult,
        'vktnodsl': vktnodsl,
        'hwresult': hwresult,
        'vkthw': vkthw,
        'miscresult': miscresult,
        'vktmisc': vktmisc,

        }

        return render(request, 'interruption_analysis/vktdet.html', context = dictdet)
