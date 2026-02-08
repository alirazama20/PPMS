from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render,redirect
from base.decorators import unauthenticated_user, allowed_users, admin_only
from .models import *
from .forms import *
import csv
import datetime
from .filters import PurchaseFilter,PurchaseFilterReport
from django.core.paginator import Paginator
from django.contrib import messages



@login_required(login_url='login')
def addpurchase(request):
    forms = PurchaseForm()
    if request.method == 'POST':
        forms = PurchaseForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Successfully Saved')
            return redirect('search-purchasebill-page')
    purchasebills = Purchase.objects.all()

    context = {'forms': forms,
               'purchasebills': purchasebills,
               }
    return render(request,'purchase/add_purchasebill.html',context)


@login_required(login_url='login')
def searchpurchase(request):
    purchasebills = Purchase.objects.all()
    myFilter = PurchaseFilter(request.GET, queryset=purchasebills)
    purchasebills = myFilter.qs

    paginator = Paginator(purchasebills,500)
    page = request.GET.get('page')
    purchasebills=paginator.get_page(page)

    context = {'purchasebills': purchasebills,
               'myFilter': myFilter
               }
    return render(request,'purchase/search_purchasebill.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','user'])
def updatepurchasebill(request, pk):
    purchase = Purchase.objects.get(id=pk)
    forms = PurchaseForm(instance=purchase)

    if request.method == 'POST':
        forms = PurchaseForm(request.POST, instance=purchase)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Successfully Update')
            return redirect('search-purchasebill-page')

    context = {'forms': forms}
    return render(request,'purchase/add_purchasebill.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','user'])
def deletepurchase(request, pk):
    purchase = Purchase.objects.get(id=pk)
    if request.method == 'POST':
        purchase.delete()
        messages.success(request, 'Successfully Delete')
        return redirect('search-purchasebill-page')
    context = {'item': purchase}
    return render(request,'purchase/deletepurchase.html',context)


@login_required(login_url='login')
def purchasebillreport(request):
    purchase = Purchase.objects.all()
    myFilter = PurchaseFilterReport(request.GET, queryset=purchase)
    purchase = myFilter.qs
    paginator = Paginator(purchase, 1500)
    page = request.GET.get('page')
    purchase = paginator.get_page(page)
    context = {'purchase': purchase,
               'myFilter': myFilter
               }
    return render(request,'report/purchase_report.html',context)






