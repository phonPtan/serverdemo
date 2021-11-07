from django.shortcuts import render
from django.http import HttpResponse
from .models import CarInfo
from .filters import CarFilter
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import datetime
import csv

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cardata(request):
    cardata_list = CarInfo.objects.all()
    # numberCar = cardata_list.count()
    page = request.GET.get('page',1)

    myfilter = CarFilter(request.GET, queryset=cardata_list)
    cardata = myfilter.qs
    numberCar = cardata.count()

    paginator = Paginator(cardata,4)
    try:
        cardata = paginator.page(page)
    except PageNotAnInteger:
        cardata = paginator.page(1)
    except EmptyPage:
        cardata = paginator.page(paginator.num_pages)
    
    context = {'cardata':cardata, 'myfilter':myfilter.form, 'numberCar':numberCar}
    # context = {'cardata':cardata, 'numberCar':numberCar}
    return render(request, 'cardata.html',context)


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    filename = str(datetime.datetime.now()) + '.csv'
    response['Content-Disposition']='attachment; filename= "' + filename + '"'

    writer = csv.writer(response)
    writer.writerow(['carID'])

    cardata_list = CarInfo.objects.all()
    myfilter = CarFilter(request.GET, queryset=cardata_list)
    cardata = myfilter.qs

    for cainfo in cardata:
        writer.writerow([cainfo.carid])

    return response