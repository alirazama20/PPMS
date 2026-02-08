from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from .filters import MeterReadingFilter
from django.contrib import messages
from django.core.paginator import Paginator
from base.decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.

@login_required(login_url='login')
def add_meter_reading(request):
    forms = MeterReadingForm()
    if request.method == 'POST':
        forms = MeterReadingForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Successfully Saved')
            return redirect('serach-meter-detail-page')
    maetereading = MeterReading.objects.all()
    context = {'forms': forms, 'maetereading': maetereading}
    return render(request,'reading/add_meter_reading_detail.html',context)

@login_required(login_url='login')
def searchmeterdetail(request):
    maetereading = MeterReading.objects.all()
    myFilter = MeterReadingFilter(request.GET, queryset=maetereading)
    maetereading = myFilter.qs

    paginator = Paginator(maetereading, 500)
    page = request.GET.get('page')
    maetereading = paginator.get_page(page)

    context = {'maetereading': maetereading,
               'myFilter': myFilter
               }
    return render(request,'reading/search_meterdetail.html',context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','user'])
def updatereading(request, pk):
    meterreading = MeterReading.objects.get(id=pk)
    forms = MeterReadingForm(instance=meterreading)

    if request.method == 'POST':
        forms = MeterReadingForm(request.POST, instance=meterreading)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Successfully Update')
            return redirect('serach-meter-detail-page')

    context = {'forms': forms}
    return render(request, 'reading/add_meter_reading_detail.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','user'])
def deletereading(request, pk):
    transportdetails = MeterReading.objects.get(id=pk)
    if request.method == 'POST':
        transportdetails.delete()
        messages.success(request, 'Successfully Delete')
        return redirect('serach-meter-detail-page')
    context = {'item': transportdetails}
    return render(request,'reading/delete_reading.html',context)

