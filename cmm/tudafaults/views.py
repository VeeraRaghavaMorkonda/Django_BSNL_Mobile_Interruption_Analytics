from django.shortcuts import render
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import mpld3
import pymysql
from tudafaults.models import cfa_wl,cfa_bb

# Create your views here.

def ll_faults(request):

	matplotlib.rcParams.update({'font.size': 22, 'font.family': 'calibri'})

	data = pd.read_html('http://10.34.2.100/reports/',header=0)
	df = pd.DataFrame(data[0])
	df1 = df[['Exchange', 'Phone No', 'Docket NO', 'Booked Date', 'JTO NAME','Mobile', 'No Of Days']]
	table = df1[df1['JTO NAME'] == 'VEERARAGHAVA-TUDA' ]

	table.set_index(['Phone No'],inplace=True)
	table['No Of Days'] = table['No Of Days'].astype(int)
	landline_wkg = pd.read_csv('D:/VEERA RAGHAVA/cmm/static/files/tuda ll 22-6-19.csv')
	landline_wkg.set_index(['Phone No'],inplace=True)
	final_table = pd.merge(table,landline_wkg,how='inner',left_index=True,right_index=True)
	fault_status = pd.DataFrame({"Current Status":['Dist CF','Pri CF','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed','Closed']})
	final_table.reset_index(inplace=True)
	op = final_table.join(fault_status)

	html = op.to_html(header=1, index=1,justify='center', classes="table table-bordered table-hover table-sm")

	fig, ax = plt.subplots()

	table['No Of Days'].plot.barh(ax=ax, subplots=False, 
				sharex=None, sharey=False, layout=None,  
				use_index=0, title='TUDA Pending Faults', grid=None, legend=0, style=None, 
				logx=False, logy=False, loglog=False, xticks=(0,0), yticks=None,
				xlim=None, ylim=None, rot=1, fontsize=13, colormap=None, 
				table=False, yerr=None, xerr=None, secondary_y=False, sort_columns=0)

	ax.set_yticklabels(table.index)

	# get_width pulls left or right; get_y pushes up or down

	for i in ax.patches:
		ax.text(i.get_width()+.1, i.get_y()+.31, \
			str(round((i.get_width()), 2)), fontsize=15, color='dimgrey')

	plt.xlabel('No.of.Days')
	plt.tight_layout()
	plt.figure(figsize=(10,10))

	dia = mpld3.fig_to_html(fig, d3_url=None, mpld3_url= None , no_extras=False, template_type='general', figid=None, use_http=True) 

	faults_dict = {'dn':html,'chart':dia }

	return render(request, 'tudafaults/tudafaults.html' , context = faults_dict)


def ll_query(request):
    return render(request, 'tudafaults/ll_query.html' )

def ll_query_data(request):

        if request.POST:
            tel_no = request.POST["telno"]

        ll_records = cfa_wl.objects.filter(PHONE_NO = tel_no)    
        bb_records = cfa_bb.objects.filter(PHONE_NO = tel_no)
        
        if ll_records:

            for i in ll_records:

                if i.LINEMAN_CODE == 'CHTTUDP0111505_OD':           
                    tt_name = "P CHENGANNA"
                    tt_mobile = "9491303871"
                elif i.LINEMAN_CODE == 'CHTTUDP0111506_OD': 
                    tt_name = "G MAHEEPAL"
                    tt_mobile = "9491303886"
                elif i.LINEMAN_CODE == 'CHTTUDP0111502_OD':
                    tt_name = "P SAMPATH"
                    tt_mobile = "9491303817"  
                elif i.LINEMAN_CODE == 'CHTTUDP0111504_OD':
                    tt_name = "K SURENDRA"
                    tt_mobile = "8985547778"
                elif i.LINEMAN_CODE == 'CHTTUDP0111503_OD':
                    tt_name = "P SREENIVASULU"
                    tt_mobile = "9491303913"
                elif i.LINEMAN_CODE == 'CHTTUDP0111501_OD':
                    tt_name = "D NAGARAJA"
                    tt_mobile = "9494365445"
                else:
                    tt_name = ""
                    tt_mobile = ""
                
                data = {'ll':ll_records , 'bb':bb_records ,'name':tt_name , 'cell':tt_mobile} 
        else:
            status = "No Data Available for Tel No :- " + tel_no + ", Please check Tel No..."
            data = {'status':status} 

        return render(request, 'tudafaults/ll_query.html' , context = data )
		

def tt_faults(request):

	matplotlib.rcParams.update({'font.size': 22, 'font.family': 'calibri'})

	data = pd.read_html('http://10.34.2.100/reports/',header=0)
	df = pd.DataFrame(data[0])
	df1 = df[['Phone No',  'Booked Date', 'JTO NAME', 'No Of Days']]
	table = df1[df1['JTO NAME'] == 'VEERARAGHAVA-TUDA' ]

	table.set_index(['Phone No'],inplace=True)
	table['No Of Days'] = table['No Of Days'].astype(int)
	landline_wkg = pd.read_csv('D:/VEERA RAGHAVA/cmm/static/files/tmwise.csv')	
	landline_wkg.set_index(['Phone No'],inplace=True)
	final_table = pd.merge(table,landline_wkg,how='inner',left_index=True,right_index=True)
	fault_status = pd.DataFrame({"Current Status":['Dist CF','Dist CF','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned','Assigned']})
	final_table.reset_index(inplace=True)
	x = final_table.join(fault_status)
	op = x[['Phone No','Lineman Code','No Of Days','Customer Name','House No','Address','Vertical','Pillar In','Pillar Out','DP','Mobile No']]
	
	
	maheepal = op[op['Lineman Code'] == 'G MAHEEPAL']
	maheepal_faults = maheepal.to_html(header=1, index=1,justify='center', classes="table table-bordered table-hover table-sm")
	maheepal_count = maheepal.shape[0]

	nagaraju = op[op['Lineman Code'] == 'D NAGARAJA']
	nagaraju_faults = nagaraju.to_html(header=1, index=1,justify='center', classes="table table-bordered table-hover table-sm")
	nagaraju_count = nagaraju.shape[0]

	sampath = op[op['Lineman Code'] == 'P SAMPATH']
	sampath_faults = sampath.to_html(header=1, index=1,justify='center', classes="table table-bordered table-hover table-sm")
	sampath_count = sampath.shape[0]
	
	surendra = op[op['Lineman Code'] == 'K SURENDRA']
	surendra_faults = surendra.to_html(header=1, index=1,justify='center', classes="table table-bordered table-hover table-sm")
	surendra_count = surendra.shape[0]

	seenu = op[op['Lineman Code'] == 'P SREENIVASULU']
	seenu_faults = seenu.to_html(header=1, index=1,justify='center', classes="table table-bordered table-hover table-sm")
	seenu_count = seenu.shape[0]

	chenganna = op[op['Lineman Code'] == 'P CHENGANNA']
	chenganna_faults = chenganna.to_html(header=1, index=1,justify='center', classes="table table-bordered table-hover table-sm")
	chenganna_count = chenganna.shape[0]
	
	faults_dict = {'maheepal':maheepal_faults,'maheepal_cnt':maheepal_count,'nagaraju':nagaraju_faults,'nagaraju_cnt':nagaraju_count,'sampath':sampath_faults,'sampath_cnt':sampath_count,'surendra':surendra_faults,'surendra_cnt':surendra_count,'seenu':seenu_faults,'seenu_cnt':seenu_count,'chenganna':chenganna_faults,'chenganna_cnt':chenganna_count}

	return render(request, 'tudafaults/tmwise.html' , context = faults_dict)
