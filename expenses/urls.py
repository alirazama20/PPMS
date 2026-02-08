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

    path('addexpensedetails-page/', views.addexpensedetails, name='addexpensedetails-page'),
    path('searchexpensedetails-page/', views.searchexpensedetails, name='searchexpensedetails-page'),

    path('update_exp_bill/<str:pk>/', views.updateexpensesbill, name='update_exp_bill'),
    path('delete_exp_bill/<str:pk>/', views.deleteexpensebill, name='delete_exp_bill'),

    path('population-chart/', views.population_chart, name='population-chart'),
    path('expenses-chart/', views.Expense_Chart, name='expenses-chart'),

]
