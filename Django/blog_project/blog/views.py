from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
      DetailView,
        CreateView,
            UpdateView,
                DeleteView)

# posts = [
#     {
#         'post_id': 1,
#         'post_title': 'Fisrt Post',
#         'post_content': "First Post content",
#     },
#     {
#         'post_id': 2,
#         'post_title': 'Second Post',
#         'post_content': "Second Post content",
#     },
#     {
#         'post_id': 3,
#         'post_title': 'Third Post',
#         'post_content': "Third Post content",
#     }
# ]

# Create your views here.
# def home(request):
#     context1 = {
#         'posts': Post.objects.all()
#     }
#     context2 = {
#        'title':'home'
#        }
#     combined_context = {**context1, **context2}
#     # print(combined_context)
#     return render(request, 'blog/home.html',context = combined_context)

class Post_ListView(ListView):
    model = Post 
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-posted_on']

class Post_DetailView(DetailView):
    model = Post

class Post_CreateView(LoginRequiredMixin,CreateView):
    model = Post 
    fields = ['title', 'content']
    # success_url = '/'       This can be uncomment if we want to visit the home page after post created
    # template_name = 'blog/home.html'
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class Post_UpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False
   
   
class Post_DeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title':"About"},)