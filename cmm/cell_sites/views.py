from django.shortcuts import render

# Create your views here.

def cell_sites(request):
    return render(request,'cell_sites/cell_sites.html')
