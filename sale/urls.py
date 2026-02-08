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
    path('add-salebill-page/', views.add_salebill, name='add-salebill-page'),
    path('search-salebill-page/', views.searchsalebill, name='search-salebill-page'),
    path('search-salebill-report/', views.searchsalebillreport, name='search-salebill-report'),
    path('search-profit-page/', views.searchprofit, name='search-profit-page'),
    path('search-salebillmade-page/', views.salebillmade, name='search-salebillmade-page'),

    path('update_bill/<str:pk>/', views.updatesalebill, name='update_bill'),
    path('delete_bill/<str:pk>/', views.deletesalebill, name='delete_bill'),
    path('load-vechile', views.load_vechile, name='load-vechile'),

    path('add-tyresalebill-page/', views.add_Tyresalebill, name='add-tyresalebill-page'),
    path('search-tyresalebill-page/', views.searchTyresalebill, name='search-tyresalebill-page'),
    path('search-tyresalebill-report/', views.searchTyresalebillreport, name='search-tyresalebill-report'),
    path('update_Tyre_bill/<str:pk>/', views.updateTyresalebill, name='update_Tyre_bill'),
    path('delete_tyre_bill/<str:pk>/', views.deleteTyresalebill, name='delete_tyre_bill'),
    path('search-tyreprofit-page/', views.searchtyreprofit, name='search-tyreprofit-page'),

    path('Account-chart/', views.Account_chart, name='Account-chart'),
    path('sale-chart/', views.Sale_Chart, name='sale-chart'),

    path('T-Account-chart/', views.T_Account_chart, name='T-Account-chart'),
    path('tyre_sale-chart/', views.Tyre_Sale_Chart, name='tyre_sale-chart'),

    path('sum_vale/', views.Sumvale, name='sum_vale'),

]
