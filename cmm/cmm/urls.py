"""cmm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from home.views import home
from cell_sites.views import cell_sites
from sites_down.views import sites_down
from interruption_analysis.views import *
from traffic.views import *
from contacts.views import contacts
from tudafaults.views import *



urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home),

    path('cell_sites/', cell_sites),

    path('sites_down/', sites_down),

    path('2g&3g_analysis/', analysis_2g3g),

    path('nsn2g&3g_analysis/', analysis_2g3gnsn),

    path('dt_history/', dt_history),

    path('repeat_faults/', repeat_faults),

    path('nsn2g_traffic/', nsn2g_traffic),

    path('nsn3g_traffic/', nsn3g_traffic),

    path('zte3g_traffic/', zte3g_traffic),

    path('hw3g_traffic/', hw3g_traffic),

    path('nt2g_traffic/', nt2g_traffic),
	
	path('zte2g_traffic/', zte2g_traffic),

    path('contacts/', contacts),

    path('strtot/', strtot),
    path('ssatot/', ssatot),
    path('blttot/', blttot),
    path('ringtot/', ringtot),
    path('ofepttot/', ofepttot),
    path('psftot/', psftot),
    path('ppftot/', ppftot),
    path('dgtot/', dgtot),
    path('dgbatttot/', dgbatttot),
    path('lbatttot/', lbatttot),
    path('nodgtot/', nodgtot),
    path('nodsltot/', nodsltot),
    path('hwtot/', hwtot),
    path('misctot/', misctot),

    path('bkkdet/', bkkdet),
    path('bgpdet/', bgpdet),
    path('cdrdet/', cdrdet),
    path('ctrdet/', ctrdet),
    path('kupdet/', kupdet),
    path('mdpdet/', mdpdet),
    path('pakdet/', pakdet),
    path('plmdet/', plmdet),
    path('plrdet/', plrdet),
    path('pgrdet/', pgrdet),
    path('ptrdet/', ptrdet),
    path('svddet/', svddet),
    path('sdmdet/', sdmdet),
    path('skhtdet/', skhtdet),
    path('vpddet/', vpddet),
    path('vktdet/', vktdet),
    path('nsn3g_traffic/details', nsn3g_traffic_data),
    path('nsn2g_traffic/details', nsn2g_traffic_data),
    path('zte3g_traffic/details', zte3g_traffic_data),
    path('hw3g_traffic/details', hw3g_traffic_data),
    path('nt2g_traffic/details', nt2g_traffic_data),
	path('zte2g_traffic/details', zte2g_traffic_data),

    path('nortel2g_ajax/', nortel2g_ajax),
	
	path('tudafaults/', ll_faults),
	path('tmwise/', tt_faults),

	path('tuda_ll_query/', ll_query),
    path('tuda_ll_query/details', ll_query_data),




    ]