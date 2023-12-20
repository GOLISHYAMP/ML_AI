from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "posting_home"),
    path('about',views.about, name = "posting_about"),
]
