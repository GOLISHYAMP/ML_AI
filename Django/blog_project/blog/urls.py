from django.urls import path
from blog.views import (
    Post_ListView,
        Post_DetailView,
            Post_CreateView,
                Post_UpdateView,
                    Post_DeleteView,
                        UserPost_ListView)
from . import views

urlpatterns = [
    # path('', views.home, name='blog_home'),
    path('', Post_ListView.as_view(), name = 'blog_home'),
    path('post/<int:pk>/', Post_DetailView.as_view(), name = 'detail_blog'),
    path('post/new/', Post_CreateView.as_view(), name = 'create_blog'),
    path('post/<int:pk>/update/', Post_UpdateView.as_view(), name = 'update_blog'),
    path('post/<int:pk>/delete/', Post_DeleteView.as_view(), name = 'delete_blog'),
    path('post/<str:username>/posts',UserPost_ListView.as_view(), name = 'user_posts'),
    path('about/', views.about, name='blog_about'),

]
