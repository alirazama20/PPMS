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




    path('add-stock-page/', views.add_stock_page, name='add-stock-page'),
    path('search-stock-page/', views.searchstock, name='search-stock-page'),
    path('update_stock_bill/<str:pk>/', views.updatestock, name='update_stock_bill'),
    path('delete_stock_bill/<str:pk>/', views.deletestock, name='delete_stock_bill'),



]
