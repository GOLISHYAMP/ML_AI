from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
# posts = [
#     {
#         'author':"SS. Rajamouli",
#         'title':"Bahubali",
#         'content':"This is the epic movie",
#         'posted_date':"May 31, 2020"
#     },
#     {
#         'author':"RGV",
#         'title':"Rakthacharittra",
#         'content':"This is the bloodshed movie",
#         'posted_date':"August 31, 2010"
#     }

# ]
def home(request):
    # return HttpResponse("<h1>Welcome to Home Page.</h1>")
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

def about(request):
    # return HttpResponse("This is all about us")
    return render(request,'blog/about.html',{'title':"About us"})
