from django.urls import path
from post import views
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView)

urlpatterns = [
    # path('',views.home,name='post_home'),
    path('', PostListView.as_view(), name='post_home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user_posts'),
    # here pk is a primary key and it must be type of integer.
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    # this is also going to use the same post_form.html template.
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    # this delete view use the template <app>_confirm_delete.html           
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    # here this create view needs the templates to be named as <app>/<model>_form.html
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('about/', views.about, name='post_about'),
]
