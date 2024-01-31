from django.shortcuts import render
from post import views as post_view
# Create your views here.

def home(request):
    posts = [
    {
        'Author':"Shyam Goli",
        'PostedOn':"Jan 16, 2024",
        'Heading':"Buy 22000 CE Nifty50",
        'Description':"Buying volums are increasing and the graph is just crossing the 30 EMA line."
    },
    {
        'Author':"Vinod Sarwade",
        'PostedOn':"Jan 15, 2024",
        'Heading':"BUY 21900 PE Nifty50",
        'Description':"SMC Strong high level has been touched and graph coming down."
    }
    ]
    context = {
        'posts': posts
    }
    return render(request,'post/home.html',context)

def about(request):
    return render(request, 'post/about.html')