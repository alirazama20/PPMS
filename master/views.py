from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render,redirect

from .models import *
from .forms import *
from .filters import *
from base.decorators import unauthenticated_user, allowed_users, admin_only


def load_vechile(request):
    account_id = request.GET.get('account')
    vechile = Vechile.objects.filter(account_id=account_id).order_by('name')
    context = {
        'vechile': vechile,
    }
    return render(request, 'master/vechile_dropdown_list_options.html', context)

# Create your views here.
@login_required(login_url='login')
def addproduct(request):
    forms = ItemForm()
    if request.method == 'POST':
        forms = ItemForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('addproduct-page')
    items = Item.objects.all()
    context = {'forms': forms, 'items': items}
    return render(request,'master/add_product.html',context)
@login_required(login_url='login')
def deleteproduct(request, pk):
    items = Item.objects.get(id=pk)
    if request.method == 'POST':
        items.delete()
        return redirect('addproduct-page')
    context = {'item': items}
    return render(request,'master/delete_product.html',context)

@login_required(login_url='login')
def addDealer(request):
    forms = DealerForm()
    if request.method == 'POST':
        forms = DealerForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('addDealer-page')
    dealer = Dealer.objects.all()
    context = {'forms': forms, 'dealer': dealer}
    return render(request,'master/add_Dealer.html',context)


@login_required(login_url='login')
def addCommission(request):
    forms = CommissionForm()
    if request.method == 'POST':
        forms = CommissionForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('addCommission-page')
    commissions = Commission.objects.all()
    context = {'forms': forms, 'commissions': commissions}
    return render(request,'master/add_Commission.html',context)
@login_required(login_url='login')
def deleteCommission(request, pk):
    commissions = Commission.objects.get(id=pk)
    if request.method == 'POST':
        commissions.delete()
        return redirect('addCommission-page')
    context = {'item': commissions}
    return render(request,'master/delete_commission.html',context)

@login_required(login_url='login')
def addExpenses(request):
    forms = ExpenseForm()
    if request.method == 'POST':
        forms = ExpenseForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('addExpenses-page')
    expense = Expense.objects.all()
    context = {'forms': forms, 'expense': expense}
    return render(request,'master/add_Expenses.html',context)
@login_required(login_url='login')
def deleteExpenses(request, pk):
    expense = Expense.objects.get(id=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('addExpenses-page')
    context = {'item': expense}
    return render(request,'master/delete_cexpense.html',context)

@login_required(login_url='login')
def addEmployee(request):
    forms = EmployeeForm()
    if request.method == 'POST':
        forms = EmployeeForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('addEmployee-page')
    employee = Employee.objects.all()
    context = {'forms': forms, 'employee': employee}
    return render(request,'master/add_Employee.html',context)
@login_required(login_url='login')
def updateemplyee(request, pk):
    employee = Employee.objects.get(id=pk)
    forms = EmployeeForm(instance=employee)

    if request.method == 'POST':
        forms = EmployeeForm(request.POST, instance=employee)
        if forms.is_valid():
            forms.save()
            return redirect('addEmployee-page')

    context = {'forms': forms}
    return render(request,'master/add_Employee.html',context)


@login_required(login_url='login')
def deleteEmployee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('addEmployee-page')
    context = {'item': employee}
    return render(request,'master/delete_employee.html',context)

@login_required(login_url='login')
def addVechile(request):
    forms = VechileForm()
    if request.method == 'POST':
        forms = VechileForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('addVechile-page')
    transports = Vechile.objects.all()
    context = {'forms': forms, 'transports': transports}
    return render(request,'master/add_Transport.html',context)

@login_required(login_url='login')
def addRate(request):
    forms = RateForm()
    if request.method == 'POST':
        forms = RateForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('addRate-page')
    rate = Rate.objects.all()
    context = {'forms': forms, 'rate': rate}
    return render(request,'master/add_Rate.html',context)


@login_required(login_url='login')
def updateRate(request, pk):
    rate = Rate.objects.get(id=pk)
    forms = RateForm(instance=rate)
    if request.method == 'POST':
        forms = RateForm(request.POST, instance=rate)
        if forms.is_valid():
            forms.save()
            return redirect('addRate-page')
    context = {'forms': forms}
    return render(request,'master/add_Rate.html',context)




@login_required(login_url='login')
def updateTransport(request, pk):
    transports = Vechile.objects.get(id=pk)
    forms = VechileForm(instance=transports)
    if request.method == 'POST':
        forms = VechileForm(request.POST, instance=transports)
        if forms.is_valid():
            forms.save()
            return redirect('addVechile-page')
    context = {'forms': forms}
    return render(request,'master/add_Transport.html',context)
@login_required(login_url='login')
def deleteTransport(request, pk):
    transports = Vechile.objects.get(id=pk)
    if request.method == 'POST':
        transports.delete()
        return redirect('addVechile-page')
    context = {'item': transports}
    return render(request,'master/delete_transports.html',context)

@login_required(login_url='login')
def employee_chart(request):
    labels = []
    data = []

    queryset = Employee.objects.values('emp_name').annotate(salary=Sum('salary')).order_by('-salary')
    for entry in queryset:
        labels.append(entry['emp_name'])
        data.append(entry['salary'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


@login_required(login_url='login')
def Employee_Chart(request):
    employee = Employee.objects.all()
    context={'employee':employee}
    return render(request,'report/employee_chart.html',context)



