from django.urls import path
from post import views
from .views import (PostListView,
                     PostDetailView,
                       PostCreateView)

urlpatterns = [
    # path('',views.home,name='post_home'),
    path('',PostListView.as_view(),name='post_home'), 
    path('post/<int:pk>/',PostDetailView.as_view(),name='post_detail'),  # here pk is a primary key and it must be type of integer.  
    path('post/new/',PostCreateView.as_view(),name='post_create'),  # here this create view needs the templates to be named as <app>/<model>_form.html
    path('about/',views.about,name='post_about'),
]

