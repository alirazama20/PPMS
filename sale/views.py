from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from base.decorators import unauthenticated_user, allowed_users, admin_only

from .models import *
from .forms import *
from .filters import *
from master.models import Vechile, Commission,Item



def load_vechile(request):
    account_id = request.GET.get('account')
    vechile = Vechile.objects.filter(account_id=account_id).order_by('name')
    context = {
        'vechile': vechile,
    }
    return render(request, 'master/vechile_dropdown_list_options.html', context)

@login_required(login_url='login')
def add_salebill(request):
    forms = SaleForm()
    if request.method == 'POST':
        forms = SaleForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Successfully Saved')
            return redirect('search-salebillmade-page')
    salebills = Sale.objects.all()
    commission = Commission.objects.all()
    items = Item.objects.all()

    context = {'forms': forms,
               'salebills': salebills,
               'commission': commission,
               'items':items,
               }
    return render(request,'sale/sale_bill.html',context)


@login_required(login_url='login')
def Sumvale(request):
    total = Sale.objects.all().aggregate(Sum('totalAmount'))
    queryset = Sale.objects.values('account').annotate(remainingAmount=Sum('remainingAmount'),totalAmount=Sum('totalAmount'),paidAmount=Sum('paidAmount')).order_by(
        '-remainingAmount','-totalAmount','-paidAmount')

    context = {'total':total,
               'queryset':queryset,
               }
    return render(request,'sale/sumvaletest.html',context)




@login_required(login_url='login')
def searchsalebill(request):
    salebills = Sale.objects.all()
    myFilter = SaleBillFilter(request.GET, queryset=salebills)
    salebills = myFilter.qs
    paginator = Paginator(salebills, 1500)
    page = request.GET.get('page')
    salebills = paginator.get_page(page)
    context = {'salebills': salebills,
               'myFilter': myFilter
               }
    return render(request,'sale/search_sale.html',context)

@login_required(login_url='login')
def salebillmade(request):
    total_invoices = Sale.objects.count()
    salebills =  Sale.objects.order_by('-id')[:100]
    myFilter = SaleBillFilter(request.GET, queryset=salebills)
    salebills = myFilter.qs
    paginator = Paginator(salebills, 100)
    page = request.GET.get('page')
    salebills = paginator.get_page(page)
    context = {'salebills': salebills,
               'myFilter': myFilter,
               'total_invoices': total_invoices,
               }
    return render(request,'sale/salebillmade.html',context)

@login_required(login_url='login')
def searchsalebillreport(request):
    salebills = Sale.objects.all()
    myFilter = SaleBillReportFilter(request.GET, queryset=salebills)
    salebills = myFilter.qs
    paginator = Paginator(salebills, 1500)
    page = request.GET.get('page')
    salebills = paginator.get_page(page)
    context = {'salebills': salebills,
               'myFilter': myFilter
               }
    return render(request,'report/sale_report.html',context)

@login_required(login_url='login')
def searchprofit(request):
    salebills = Sale.objects.all()
    myFilter = SaleBillProfitFilter(request.GET, queryset=salebills)
    salebills = myFilter.qs
    paginator = Paginator(salebills, 1500)
    page = request.GET.get('page')
    salebills = paginator.get_page(page)
    context = {'salebills': salebills,
               'myFilter': myFilter
               }
    return render(request,'sale/search_profit.html',context)

@login_required(login_url='login')
def searchtyreprofit(request):
    tyresalebills = TyreSale.objects.all()
    myFilter = TyreSaleProfitFilter(request.GET, queryset=tyresalebills)
    tyresalebills = myFilter.qs
    paginator = Paginator(tyresalebills, 1500)
    page = request.GET.get('page')
    tyresalebills = paginator.get_page(page)
    context = {'tyresalebills': tyresalebills,
               'myFilter': myFilter
               }
    return render(request,'sale/search_tyre_profit.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','user'])
def updatesalebill(request, pk):
    salebills = Sale.objects.get(id=pk)
    forms = SaleForm(instance=salebills)

    if request.method == 'POST':
        forms = SaleForm(request.POST, instance=salebills)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Successfully Update')
            return redirect('search-salebillmade-page')

    context = {'forms': forms}
    return render(request,'sale/sale_bill.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','user'])
def deletesalebill(request, pk):
    salebills = Sale.objects.get(id=pk)
    if request.method == 'POST':
        salebills.delete()
        messages.success(request, 'Successfully Delete')
        return redirect('search-salebill-page')
    context = {'item': salebills}
    return render(request,'sale/delete_salebill.html',context)



@login_required(login_url='login')
def add_Tyresalebill(request):
    forms = TyreSaleForm()
    if request.method == 'POST':
        forms = TyreSaleForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Successfully Saved')
            return redirect('search-tyresalebill-page')
    tyresalebills = TyreSale.objects.all()
    commission = Commission.objects.all()
    context = {'forms': forms,
               'tyresalebills': tyresalebills,
               'commission': commission}
    return render(request,'sale/Tyre_sale_bill.html',context)


@login_required(login_url='login')
def searchTyresalebill(request):
    tyresalebills = TyreSale.objects.all()
    myFilter = TyreSaleFilter(request.GET, queryset=tyresalebills)
    tyresalebills = myFilter.qs
    paginator = Paginator(tyresalebills, 1500)
    page = request.GET.get('page')
    tyresalebills = paginator.get_page(page)
    context = {'tyresalebills': tyresalebills,
               'myFilter': myFilter
               }
    return render(request,'sale/Tyre_search_sale.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','user'])
def updateTyresalebill(request, pk):
    tyresalebills = TyreSale.objects.get(id=pk)
    forms = TyreSaleForm(instance=tyresalebills)
    if request.method == 'POST':
        forms = TyreSaleForm(request.POST, instance=tyresalebills)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Successfully Update')
            return redirect('search-tyresalebill-page')
    context = {'forms': forms}
    return render(request,'sale/Tyre_sale_bill.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','user'])
def deleteTyresalebill(request, pk):
    tyresalebills = TyreSale.objects.get(id=pk)
    if request.method == 'POST':
        tyresalebills.delete()
        messages.success(request, 'Successfully Delete')
        return redirect('search-tyresalebill-page')
    context = {'item': tyresalebills}
    return render(request,'sale/delete_Tyre_salebill.html',context)

@login_required(login_url='login')
def searchTyresalebillreport(request):
    tyresalebills = TyreSale.objects.all()
    myFilter = TyreSaleReportFilter(request.GET, queryset=tyresalebills)
    tyresalebills = myFilter.qs
    paginator = Paginator(tyresalebills, 1500)
    page = request.GET.get('page')
    tyresalebills = paginator.get_page(page)
    context = {'tyresalebills': tyresalebills,
               'myFilter': myFilter
               }
    return render(request,'report/tyre_sale_report.html',context)

@login_required(login_url='login')
def Sale_Chart(request):
    commission = Commission.objects.all()
    context={'commission':commission}
    return render(request,'report/sale_chart.html',context)

@login_required(login_url='login')
def Tyre_Sale_Chart(request):
    commission = Commission.objects.all()
    context = {'commission': commission}
    return render(request,'report/tyre_sale_chart.html',context)

@login_required(login_url='login')
def Account_chart(request):
    labels = []
    data = []
    queryset = Sale.objects.values('account').annotate(remainingAmount=Sum('remainingAmount')).order_by('-remainingAmount')
    for entry in queryset:
        labels.append(entry['account'])
        data.append(entry['remainingAmount'])
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

@login_required(login_url='login')
def T_Account_chart(request):
    labels = []
    data = []
    queryset = TyreSale.objects.values('account').annotate(remainingAmount=Sum('remainingAmount')).order_by('-remainingAmount')
    for entry in queryset:
        labels.append(entry['account'])
        data.append(entry['remainingAmount'])
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })