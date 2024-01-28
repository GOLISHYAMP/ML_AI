from django.shortcuts import render

# Create your views here.
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

def home(request):
    context = {
        "posts" : posts
    }
    return render(request, 'posting/home.html',context)

def about(request):
    return render(request, 'posting/about.html')