from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from .filters import DailyStockFilter
from django.core.paginator import Paginator
from django.contrib import messages
from base.decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.

@login_required(login_url='login')
def add_stock_page(request):
    forms = DailyStockForm()
    if request.method == 'POST':
        forms = DailyStockForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Successfully Saved')
            return redirect('search-stock-page')
    stock = DailyStock.objects.all()
    context = {'forms': forms, 'stock': stock}
    return render(request,'stock/add_stock.html',context)

@login_required(login_url='login')
def searchstock(request):
    stock = DailyStock.objects.all()
    myFilter = DailyStockFilter(request.GET, queryset=stock)
    stock = myFilter.qs

    paginator = Paginator(stock, 500)
    page = request.GET.get('page')
    stock = paginator.get_page(page)

    context = {'stock': stock,
               'myFilter': myFilter
               }
    return render(request,'stock/search_attock.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','user'])
def updatestock(request, pk):
    stock = DailyStock.objects.get(id=pk)
    forms = DailyStockForm(instance=stock)

    if request.method == 'POST':
        forms = DailyStockForm(request.POST, instance=stock)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Successfully Update')
            return redirect('search-stock-page')

    context = {'forms': forms}
    return render(request,'stock/add_stock.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','user'])
def deletestock(request, pk):
    stock = DailyStock.objects.get(id=pk)
    if request.method == 'POST':
        stock.delete()
        messages.success(request, 'Successfully Delete')
        return redirect('search-stock-page')
    context = {'item': stock}
    return render(request,'stock/delete_stock.html',context)



