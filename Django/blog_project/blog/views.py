from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

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

def about(request):
    return render(request, 'blog/about.html', {'title':"About"},)