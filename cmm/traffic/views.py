from django.shortcuts import render
from traffic.models import nsn3g_table,zte3g_table
import pymysql


# Create your views here.

def nsn2g_traffic(request):

    return render(request, 'traffic/nsn2g_traffic.html')

def nsn2g_traffic_data(request):

    if request.POST:
        from_date = request.POST["from_date"]
        to_date = request.POST["to_date"]

        result = nsn3g_table.objects.filter(DATE__range=(from_date, to_date))
        #cursor.execute(("SELECT * FROM nsn2g WHERE DATE BETWEEN %s AND %s AND BTS_name REGEXP 'CT' ORDER BY BTS_name,DATE DESC"), (from_date,to_date))
        #result = cursor.fetchall()

    return render(request, 'traffic/nsn2g_traffic.html', {'result': result})



def nsn3g_traffic(request):

    return render(request, 'traffic/nsn3g_traffic.html')

def nsn3g_traffic_data(request):

    if request.POST:
        from_date = request.POST["from_date"]
        to_date = request.POST["to_date"]
        result = nsn3g_table.objects.filter(DATE__range=(from_date, to_date))        
    return render(request, 'traffic/nsn3g_traffic.html', {'result': result})


def zte3g_traffic(request):

    return render(request, 'traffic/zte3g_traffic.html')

def zte3g_traffic_data(request):

    if request.POST:
        from_date = request.POST["from_date"]
        to_date = request.POST["to_date"]
        result = zte3g_table.objects.filter(Date__range=(from_date, to_date))        
    return render(request, 'traffic/zte3g_traffic.html', {'result': result})


def hw3g_traffic(request):

    return render(request, 'traffic/hw3g_traffic.html')

def hw3g_traffic_data(request):

    con = pymysql.connect(host='localhost',
                          user='root',
                          password='',
                          database='bsnl')

    with con.cursor(pymysql.cursors.DictCursor) as cursor:
        if request.POST:
            from_date = request.POST["from_date"]
            to_date = request.POST["to_date"]

        cursor.execute(
            ("SELECT * FROM huawei WHERE Date BETWEEN %s AND %s AND CELL_NAME REGEXP 'CT' AND CELL_NAME REGEXP '102' ORDER BY CELL_NAME,DATE DESC"),(from_date, to_date))
        result = cursor.fetchall()

    return render(request, 'traffic/hw3g_traffic.html', {'result': result})

def nt2g_traffic(request):

    return render(request, 'traffic/nt2g_traffic.html')

def nt2g_traffic_data(request):

    con = pymysql.connect(host='localhost',
                          user='root',
                          password='',
                          database='bsnl')

    with con.cursor(pymysql.cursors.DictCursor) as cursor:
        if request.POST:
            from_date = request.POST["from_date"]
            to_date = request.POST["to_date"]

        cursor.execute(
            ("SELECT * FROM nortel WHERE Date BETWEEN %s AND %s AND Bts_Name REGEXP 'CT' ORDER BY Bts_Name,Date DESC"),(from_date, to_date))
        result = cursor.fetchall()

    return render(request, 'traffic/nt2g_traffic.html', {'result': result})



def nortel2g_ajax(request):

     if request.method == 'POST':


        from_date = request.POST["from_date"]
        to_date = request.POST["to_date"]
        column_name = request.POST["column_name"]
        order = request.POST["order"]

        if order == 'desc':
            order = 'asc'

        else:
            order = 'desc'

        con = pymysql.connect(host='localhost',
                               user='root',
                               password='',
                               database='bsnl')

        with con.cursor(pymysql.cursors.DictCursor) as cursor:

             cursor.execute(("SELECT * FROM nortel WHERE  BTS_name REGEXP 'CT' ORDER BY %s %s "),(column_name, order ))
             result = cursor.fetchall()

        return render(request, 'traffic/nt2g_ajax.html', {'result': result,'order':order})

     else:
         pass

		 
def zte2g_traffic(request):

    return render(request, 'traffic/zte2g_traffic.html')

def zte2g_traffic_data(request):

    con = pymysql.connect(host='localhost',
                          user='root',
                          password='',
                          database='bsnl')

    with con.cursor(pymysql.cursors.DictCursor) as cursor:
        if request.POST:
            from_date = request.POST["from_date"]
            to_date = request.POST["to_date"]

        cursor.execute(
            ("SELECT * FROM zte2g WHERE Date BETWEEN %s AND %s AND CELL_NAME REGEXP '283' ORDER BY CELL_NAME,DATE DESC"),(from_date, to_date))
        result = cursor.fetchall()

    return render(request, 'traffic/zte2g_traffic.html', {'result': result})
		 		 