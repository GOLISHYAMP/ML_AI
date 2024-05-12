from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'cartApp/home.html')

def add_products(request):
    form = forms.add_items()
    response = render(request, 'cartApp/add.html', {'form':forms.add_items})
    if request.method == 'POST':
        form = forms.add_items(request.POST)
        if form.is_valid():
            if 'count' in request.COOKIES:
                newcount = int(request.COOKIES['count'])+1
            else:
                newcount = 1
            
            response.set_cookie(form.cleaned_data.get('item_name'), form.cleaned_data.get('quantity'))
            # request.set_cookie('quantity'+str(newcount),form.cleaned_data.get('quantity'))
            messages.success(request,f'{form.cleaned_data.get("item_name")} is successfully added!')
            # return redirect('add_products')

    return response

def display(request):
    # my_dic = { 'name' : request.COOKIES['name'],
    #           'quantity' : request.COOKIES['quantity']}
    return render(request, 'cartApp/display.html')