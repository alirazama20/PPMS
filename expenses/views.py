from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from .filters import ExpenseDetailFilter
from django.core.paginator import Paginator
from base.decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def addexpensedetails(request):
    forms = ExpenseDetailForm()
    if request.method == 'POST':
        forms = ExpenseDetailForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Successfully Saved')
            return redirect('searchexpensedetails-page')
    expensedetails = ExpenseDetail.objects.all()
    context = {'forms': forms, 'expensedetails': expensedetails}
    return render(request,'expense/add_addexpensedetails.html',context)

@login_required(login_url='login')
def searchexpensedetails(request):
    expensedetails = ExpenseDetail.objects.all()
    myFilter = ExpenseDetailFilter(request.GET, queryset=expensedetails)
    expensedetails = myFilter.qs

    paginator = Paginator(expensedetails, 100)
    page = request.GET.get('page')
    expensedetails = paginator.get_page(page)

    context = {'expensedetails': expensedetails,
               'myFilter': myFilter
               }
    return render(request,'expense/search_ssearchexpensedetails.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','user'])
def updateexpensesbill(request, pk):
    expensedetail = ExpenseDetail.objects.get(id=pk)
    forms = ExpenseDetailForm(instance=expensedetail)

    if request.method == 'POST':
        forms = ExpenseDetailForm(request.POST, instance=expensedetail)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Successfully Update')
            return redirect('searchexpensedetails-page')

    context = {'forms': forms}
    return render(request,'expense/add_addexpensedetails.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','user'])
def deleteexpensebill(request, pk):
    expensedetail = ExpenseDetail.objects.get(id=pk)
    if request.method == 'POST':
        expensedetail.delete()
        messages.success(request, 'Successfully Delete')
        return redirect('searchexpensedetails-page')
    context = {'item': expensedetail}
    return render(request,'expense/delete_expenses.html',context)

@login_required(login_url='login')
def population_chart(request):
    labels = []
    data = []

    queryset = ExpenseDetail.objects.values('exp_name').annotate(amount=Sum('amount')).order_by('-amount')
    for entry in queryset:
        labels.append(entry['exp_name'])
        data.append(entry['amount'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

@login_required(login_url='login')
def Expense_Chart(request):
    expensedetails = ExpenseDetail.objects.all()
    context={'expensedetails':expensedetails}
    return render(request,'report/expense_chart.html',context)

