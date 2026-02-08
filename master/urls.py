"""KFS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('addproduct-page/', views.addproduct, name='addproduct-page'),
    path('addDealer-page/', views.addDealer, name='addDealer-page'),
    path('addCommission-page/', views.addCommission, name='addCommission-page'),
    path('addExpenses-page/', views.addExpenses, name='addExpenses-page'),
    path('addEmployee-page/', views.addEmployee, name='addEmployee-page'),
    path('addVechile-page/', views.addVechile, name='addVechile-page'),
    path('addRate-page/', views.addRate, name='addRate-page'),


    path('delete_product/<str:pk>/', views.deleteproduct, name='delete_product'),
    path('delete_Commission/<str:pk>/', views.deleteCommission, name='delete_Commission'),
    path('delete_expense/<str:pk>/', views.deleteExpenses, name='delete_expense'),
    path('delete_employee/<str:pk>/', views.deleteEmployee, name='delete_employee'),
    path('delete_transport/<str:pk>/', views.deleteTransport, name='delete_transport'),

    path('update_rate/<str:pk>/', views.updateRate, name='update_rate'),
    path('update_employee/<str:pk>/', views.updateemplyee, name='update_employee'),
    path('update_transport/<str:pk>/', views.updateTransport, name='update_transport'),

    path('employee-chart/', views.employee_chart, name='employee-chart'),
    path('load-vechile', views.load_vechile, name='load-vechile'),

    path('employees-chart/', views.Employee_Chart, name='employees-chart'),


]
