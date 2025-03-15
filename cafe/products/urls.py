from django.urls import path
from . import views


urlpatterns = [

    path('', views.product_list_and_increment, name='product_list'), 
    path('manage-products/', views.manage_products, name='manage_products'),
    path('sales-calendar/', views.sales_calendar, name='sales_calendar'),
    path('sales-details/<str:date>/', views.sales_details, name='sales_details'),

]
