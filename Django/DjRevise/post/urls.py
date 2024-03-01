from django.urls import path
from post import views

urlpatterns = [
    path('',views.home,name='post_home'),
    path('about/',views.about,name='post_about'),
]

