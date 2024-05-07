from django.urls import path
from blog.views import Post_ListView,Post_DetailView
from . import views

urlpatterns = [
    # path('', views.home, name='blog_home'),
    path('', Post_ListView.as_view(), name = 'blog_home'),
    path('post/<int:pk>/', Post_DetailView.as_view(), name = 'Detail_blog'),
    path('about/', views.about, name='blog_about'),

]
