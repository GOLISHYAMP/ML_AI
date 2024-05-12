from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='app_home'),
    path('add_form/', views.add_products, name='add_products'),
    path('display_items/',views.display, name = 'display_products')
]