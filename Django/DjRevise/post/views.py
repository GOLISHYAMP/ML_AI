from typing import Optional
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import (ListView,
                                   DetailView,
                                     CreateView,
                                       UpdateView,
                                          DeleteView)


# this below class help to stop the unauthorized access of the user without login for the class views, just like loginrequied decarotors for the function views.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

# Create your views here.

# def home(request):
#     # posts = [
#     # {
#     #     'Author':"Shyam Goli",
#     #     'PostedOn':"Jan 16, 2024",
#     #     'Heading':"Buy 22000 CE Nifty50",
#     #     'Description':"Buying volums are increasing and the graph is just crossing the 30 EMA line."
#     # },
#     # {
#     #     'Author':"Vinod Sarwade",
#     #     'PostedOn':"Jan 15, 2024",
#     #     'Heading':"BUY 21900 PE Nifty50",
#     #     'Description':"SMC Strong high level has been touched and graph coming down."
#     # }
#     # ]
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request,'post/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'post/home.html' # here the template required name must be in the format <app>/<model_name>_<view_type>.html  eg: post/Post_list.html
    context_object_name = 'posts'  # Here in class view I don't now in template on which variable I should iterate. so this variable needs to be set.
    ordering = ['-PostOn']  # to put the latest post on the top.
    paginate_by = 3   #  from django.core.paginator import paginator  here we do not need to import, because it is a class based view.

class UserPostListView(ListView):
    model = Post
    template_name = 'post/user_posts.html' # here the template required name must be in the format <app>/<model_name>_<view_type>.html  eg: post/Post_list.html
    context_object_name = 'posts'  # Here in class view I don't now in template on which variable I should iterate. so this variable needs to be set.
    # ordering = ['-PostOn']  # to put the latest post on the top.
    paginate_by = 3   #  from django.core.paginator import paginator  here we do not need to import, because it is a class based view.

    # this below query works when the url is hitted and search for keywords in the url
    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(Author = user).order_by('-PostOn')


class PostDetailView(DetailView):
    model = Post
   
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['Heading','Description']

    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)
    
#here in the below view the class which are inherited LoginRequiredMixin, UserPassesTestMixin most be first as written.

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['Heading','Description']

    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)
    
    # this function ensure that the post you want to update is the correct user or not.
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.Author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'  # here I am saying the django to return to home after successful deletion of post.
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.Author:
            return True
        return False

def about(request):
    return render(request, 'post/about.html')