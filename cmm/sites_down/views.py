from django.shortcuts import render
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import mpld3


# Create your views here.

def sites_down(request):

    '''matplotlib.rcParams.update({'font.size': 22, 'font.family': 'calibri'})

    data = pd.read_html("http://10.31.241.176/omcr/currentbtsdown_list_durationwise_db.php?circle=AP&ssaname=CHITOOR&type=5",header=0)
      
    for row in data:
    
        df = pd.DataFrame(row)
       
    df['Cumm Down Time'] = df['Cumm Down Time'].str.replace(":",".")
    df['Cumm Down Time'] = df['Cumm Down Time'].map(lambda x: str(x)[:5])
    df['Cumm Down Time'] = df['Cumm Down Time'].astype(float)
    df = df.sort_values(by = ['Cumm Down Time'] , ascending=1)
    
    
    fig, ax = plt.subplots()

    df['Cumm Down Time'].plot.barh(ax=ax, subplots=0,figsize=(12,8),
                sharex=None, sharey=False, layout=None,  
                use_index=0, title='Cell Sites Currently Down', grid=0, legend=0, style=None, 
                logx=False, logy=False, loglog=False, xticks=None, yticks=None,
                xlim=None, ylim=None, rot=1, fontsize=13, colormap=None, color = 'orange',
                table=False, yerr=None, xerr=None, secondary_y=False, sort_columns=1)
    
    for i, v in enumerate(df['Cumm Down Time']):
        ax.text(v,i-0.2, str(v), color='black',fontsize=14,fontweight='bold')
    
    ax.set_yticklabels(df['BTS Name'])
    ax.set_xlabel("Down Time (Hrs)", fontsize=18)
    ax.set_ylabel("BTS Name", fontsize=18)
    plt.tight_layout()
	
    dia = mpld3.fig_to_html(fig, d3_url=None, mpld3_url= None , no_extras=False, template_type='general', figid=None, use_http=True) 
    # print(dia)'''
	

	
    # print("<b><h4>Details of Cell Sites Currently Down :</b></h4>")
    
    nt_hw_zte_tables = pd.read_html("http://10.31.241.176/omcr/currentbtsdown_list_durationwise_db.php?circle=AP&ssaname=CHITOOR&type=5",header=0)
    nt_hw_zte_table = nt_hw_zte_tables[0].to_html(header=1, index=0, justify='center',na_rep='---', classes="table table-bordered table-hover table-condensed")


    nsn_tables = pd.read_html("http://10.33.69.98/report/r1/CT/",header=0)
    nsn_table = nsn_tables[0].to_html(header=1, index=0, justify='center',na_rep='---', classes="table table-bordered table-hover table-condensed")


    sites_dn_dict = { 'nt_hw_zte': nt_hw_zte_table , 'nsn':nsn_table }

    return render(request, 'sites_down/sites_down.html' , context = sites_dn_dict)

