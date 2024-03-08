from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.views.generic import (ListView,
                                   DetailView,
                                     CreateView)

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

class PostDetailView(DetailView):
    model = Post
   
class PostCreateView(CreateView):
    model = Post
    fields = ['Heading','Description']

    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'post/about.html')