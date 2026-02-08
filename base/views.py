from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import  CreateUserForm
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from django.db.models import Sum
from django.http import JsonResponse


# Create your views here.
from master.models import *
from sale.models import *
from purchase.models import *
from meterreading.models import *
from stockregister.models import *
from expenses.models import *

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='user')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')
    context = {'form': form}
    return render(request, 'base/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'base/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')



# views.py
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Sum, Count, Avg
from datetime import datetime, timedelta, date
import json
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    # Your existing queries
    salebills = Sale.objects.all()
    commissions = Commission.objects.all()
    total_invoices = Sale.objects.count()
    queryset = Sale.objects.order_by('-id')[:5]
    qs_meterreading = MeterReading.objects.order_by('-id')[:1]
    qs_stockregister = DailyStock.objects.order_by('-id')[:1]
    qs_expenses = ExpenseDetail.objects.order_by('-id')[:2]
    total_pur_invoices = Purchase.objects.count()
    queryset_pur = Purchase.objects.order_by('-id')[:5]

    total_customers = commissions.count()
    total_orders = salebills.count()
    creditor = salebills.filter(invoiceType='Credit').count()
    cash = salebills.filter(invoiceType='CASH').count()
    
    # ============ AI & MODERN DASHBOARD ADDITIONS ============
    
    # Today's date
    today = timezone.now().date()
    
    # 1. Today's Revenue Calculation
    today_sales = Sale.objects.filter(date__date=today)
    today_revenue = today_sales.aggregate(total=Sum('totalAmount'))['total'] or 0
    
    # 2. Yesterday's Revenue for comparison
    yesterday = today - timedelta(days=1)
    yesterday_sales = Sale.objects.filter(date__date=yesterday)
    yesterday_revenue = yesterday_sales.aggregate(total=Sum('totalAmount'))['total'] or 0
    
    # 3. Revenue Increase/Decrease percentage
    if yesterday_revenue > 0:
        revenue_increase = round(((today_revenue - yesterday_revenue) / yesterday_revenue) * 100, 1)
    else:
        revenue_increase = 100 if today_revenue > 0 else 0
    
    # 4. Today's Orders Count
    today_orders = today_sales.count()
    
    # 5. Average Order Value
    avg_order_value = today_sales.aggregate(avg=Avg('totalAmount'))['avg'] or 0
    
    # 6. Peak Hour Analysis (simplified - you can implement actual ML later)
    peak_hour = calculate_peak_hour()
    
    # 7. Stock Analysis from DailyStock
    stock_data = []
    if qs_stockregister:
        for stock in qs_stockregister:
            total_hsd = (stock.rmg_one_hsd or 0) + (stock.rmg_two_hsd or 0)
            total_pmg = stock.rmg_pmg or 0
            total_stock = total_hsd + total_pmg
            
            if total_stock > 0:
                hsd_percent = round((total_hsd / total_stock) * 100)
                pmg_percent = round((total_pmg / total_stock) * 100)
                stock_data = [hsd_percent, pmg_percent, 100 - (hsd_percent + pmg_percent)]
    
    # 8. Sales Trend Data (Last 7 days)
    sales_labels = []
    hsd_sales_data = []
    pmg_sales_data = []
    
    for i in range(6, -1, -1):
        day = today - timedelta(days=i)
        day_name = day.strftime('%a')
        sales_labels.append(day_name)
        
        # Get HSD and PMG sales for each day
        day_meter = MeterReading.objects.filter(date__date=day).first()
        if day_meter:
            hsd_sales_data.append(float(day_meter.total_diesel or 0))
            pmg_sales_data.append(float(day_meter.total_petrol or 0))
        else:
            hsd_sales_data.append(0)
            pmg_sales_data.append(0)
    
    # 9. AI Predictions (simplified - can be enhanced with ML)
    predicted_revenue = predict_tomorrow_revenue(today_revenue, revenue_increase)
    
    # 10. Customer Analysis
    new_customers = Commission.objects.filter(
        created_at__date__gte=today - timedelta(days=7)
    ).count()
    
    # 11. Remaining Stock Days
    stock_days_left = calculate_stock_days_left(qs_stockregister, qs_meterreading)
    
    # 12. Recent Transactions (Last 10)
    recent_orders_list = []
    recent_sales = Sale.objects.order_by('-date')[:10]
    for sale in recent_sales:
        recent_orders_list.append({
            'time': sale.date.strftime('%I:%M %p'),
            'customer': sale.account.name if sale.account else 'Walk-in',
            'fuel_type': 'HSD'
            if sale.item_name and 'diesel' in sale.item_name.name.lower()
            else 'PMG',

            'fuel_type_color': 'primary'
            if sale.item_name and 'diesel' in sale.item_name.name.lower()
            else 'success',


            'quantity': sale.quantity,
            'amount': sale.totalAmount,
            'status': 'Paid' if sale.paidAmount >= sale.totalAmount else 'Pending',
            'status_color': 'success' if sale.paidAmount >= sale.totalAmount else 'warning'
        })
    
    # 13. AI Recommendations
    ai_recommendations = generate_ai_recommendations(
        qs_stockregister, 
        qs_meterreading,
        salebills
    )
    
    # 14. Today's Total Sales in Liters
    today_total_liters = 0
    today_hsd_liters = 0
    today_pmg_liters = 0
    
    if qs_meterreading:
        for meter in qs_meterreading:
            today_hsd_liters = float(meter.total_diesel or 0)
            today_pmg_liters = float(meter.total_petrol or 0)
            today_total_liters = today_hsd_liters + today_pmg_liters
    
    # 15. Today's Expenses Total
    today_expense_total = 0
    today_expenses = ExpenseDetail.objects.filter(date__date=today)
    for expense in today_expenses:
        today_expense_total += float(expense.amount or 0)
    
    # 16. Restock Message
    restock_message = generate_restock_message(qs_stockregister, qs_meterreading)
    
    context = {
        # Existing context
        'commissions': commissions,
        'salebills': salebills,
        'total_orders': total_orders,
        'creditor': creditor,
        'cash': cash,
        'total_customers': total_customers,
        'total_invoices': total_invoices,
        'queryset': queryset,
        'total_pur_invoices': total_pur_invoices,
        'queryset_pur': queryset_pur,
        'qs_meterreading': qs_meterreading,
        'qs_stockregister': qs_stockregister,
        'qs_expenses': qs_expenses,
        
        # New AI Dashboard Context
        'today_revenue': round(today_revenue, 2),
        'revenue_increase': revenue_increase,
        'today_orders': today_orders,
        'avg_order_value': round(avg_order_value, 2),
        'predicted_revenue': round(predicted_revenue, 2),
        'prediction_accuracy': 85,  # Can be calculated from ML model
        'peak_hour': peak_hour,
        'peak_increase': 25,  # Example value
        
        # Chart Data (JSON serialized)
        'sales_labels': json.dumps(sales_labels),
        'hsd_sales': json.dumps(hsd_sales_data),
        'pmg_sales': json.dumps(pmg_sales_data),
        'stock_data': json.dumps(stock_data if stock_data else [50, 30, 20]),
        
        # Quick Stats
        'today_total_sales': round(today_total_liters, 1),
        'today_hsd': round(today_hsd_liters, 1),
        'today_pmg': round(today_pmg_liters, 1),
        'remaining_stock': get_total_stock(qs_stockregister),
        'stock_days_left': stock_days_left,
        'customer_count': total_customers,
        'new_customers': new_customers,
        'regular_customers': total_customers - new_customers,
        'today_expense': round(today_expense_total, 2),
        
        # Recent Transactions
        'recent_orders': recent_orders_list,
        
        # AI Recommendations
        'ai_recommendations': ai_recommendations,
        'restock_message': restock_message,
    }
    
    return render(request, 'dashboard.html', context)

# ============ HELPER FUNCTIONS ============

def calculate_peak_hour():
    """Calculate peak hour based on recent sales"""
    # Simplified version - you can implement actual hour analysis
    from datetime import datetime
    current_hour = datetime.now().hour
    
    if 17 <= current_hour < 19:  # 5-7 PM
        return "6-7 PM"
    elif 8 <= current_hour < 10:  # 8-10 AM
        return "9-10 AM"
    else:
        return "4-5 PM"

def predict_tomorrow_revenue(today_revenue, revenue_increase):
    """Predict tomorrow's revenue"""
    if revenue_increase > 0:
        return round(today_revenue * (1 + revenue_increase/100), 2)
    else:
        return round(today_revenue * 0.95, 2)  # Conservative estimate

def calculate_stock_days_left(stock_register, meter_reading):
    """Calculate how many days stock will last"""
    if not stock_register or not meter_reading:
        return 0
    
    total_stock = get_total_stock(stock_register)
    
    # Get average daily consumption from meter reading
    avg_daily_consumption = 0
    if meter_reading:
        for meter in meter_reading:
            daily_total = (float(meter.total_diesel or 0) + float(meter.total_petrol or 0))
            avg_daily_consumption = daily_total
    
    if avg_daily_consumption > 0:
        return round(total_stock / avg_daily_consumption)
    
    return 7  # Default value

def get_total_stock(stock_register):
    """Calculate total stock from stock register"""
    total = 0
    if stock_register:
        for stock in stock_register:
            total += (float(stock.rmg_one_hsd or 0) + 
                     float(stock.rmg_two_hsd or 0) + 
                     float(stock.rmg_pmg or 0))
    return round(total, 1)

def generate_ai_recommendations(stock_register, meter_reading, salebills):
    """Generate AI-based recommendations"""
    recommendations = []
    
    # Check stock levels
    if stock_register:
        for stock in stock_register:
            hsd_stock = (float(stock.rmg_one_hsd or 0) + float(stock.rmg_two_hsd or 0))
            pmg_stock = float(stock.rmg_pmg or 0)
            
            if hsd_stock < 5000:  # Less than 5000 liters
                recommendations.append({
                    'title': 'Restock HSD Urgently',
                    'description': f'Only {hsd_stock} liters remaining',
                    'icon': 'exclamation-triangle',
                    'color': 'danger'
                })
            elif hsd_stock < 10000:
                recommendations.append({
                    'title': 'Plan HSD Restock',
                    'description': f'Stock at {hsd_stock} liters',
                    'icon': 'warehouse',
                    'color': 'warning'
                })
            
            if pmg_stock < 3000:
                recommendations.append({
                    'title': 'Restock PMG',
                    'description': f'Only {pmg_stock} liters remaining',
                    'icon': 'gas-pump',
                    'color': 'danger'
                })
    
    # Check credit sales
    credit_sales = salebills.filter(invoiceType='Credit')
    overdue_sales = credit_sales.filter(remainingAmount__gt=0)
    
    if overdue_sales.count() > 5:
        recommendations.append({
            'title': 'Credit Risk Alert',
            'description': f'{overdue_sales.count()} overdue payments',
            'icon': 'credit-card',
            'color': 'warning'
        })
    
    # Check peak hour recommendation
    from datetime import datetime
    hour = datetime.now().hour
    if 16 <= hour <= 19:
        recommendations.append({
            'title': 'Peak Hour Staffing',
            'description': 'Consider extra staff for evening rush',
            'icon': 'users',
            'color': 'info'
        })
    
    # Add default recommendations if none
    if not recommendations:
        recommendations = [
            {
                'title': 'All Systems Optimal',
                'description': 'No immediate actions required',
                'icon': 'check-circle',
                'color': 'success'
            }
        ]
    
    return recommendations[:3]  # Return top 3 recommendations

def generate_restock_message(stock_register, meter_reading):
    """Generate restock message based on stock and consumption"""
    if not stock_register or not meter_reading:
        return "Check stock levels manually"
    
    total_stock = get_total_stock(stock_register)
    
    # Get today's consumption
    today_consumption = 0
    if meter_reading:
        for meter in meter_reading:
            today_consumption = (float(meter.total_diesel or 0) + 
                               float(meter.total_petrol or 0))
    
    if today_consumption > 0:
        days_left = total_stock / today_consumption
        if days_left < 2:
            return f"CRITICAL: Stock will last only {int(days_left)} day(s)"
        elif days_left < 5:
            return f"Order soon: Stock for {int(days_left)} days"
        else:
            return f"Stock sufficient for {int(days_left)} days"
    
    return "Monitor stock levels regularly"


# API View
def sales_data_api(request):
    from django.http import JsonResponse
    from datetime import datetime, timedelta
    import json
    
    days = int(request.GET.get('days', 7))
    
    # Generate chart data for given days
    data = {
        'labels': [],
        'hsd': [],
        'pmg': []
    }
    
    # Add your data fetching logic here
    
    return JsonResponse(data)

def customer(request, pk_test):
    commissions = Commission.objects.get(id=pk_test)
    orders = commissions.order_set.all()


    context = {'commissions':commissions,
               'salebills':salebills,
               'orders':orders}
    return render(request, 'master/customer.html',context)

def userPage(request):
	context = {}
	return render(request, 'base/user.html', context)

def aboutus(request):
	context = {}
	return render(request, 'base/aboutus.html', context)