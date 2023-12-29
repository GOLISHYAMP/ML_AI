from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='chatbot_home'),
    path('about', views.about, name="chatbot_about")
]