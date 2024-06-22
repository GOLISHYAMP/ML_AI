# from django.shortcuts import render,redirect
# from . import forms
# from django.contrib import messages

# # Create your views here.
# def home(request):
#     return render(request, 'cartApp/home.html')

# def add_products(request):
#     # form = forms.add_items()
    
#     if request.method == 'POST':
#         form = forms.add_items(request.POST)
#         if form.is_valid():
#             if 'count' in request.COOKIES:
#                 newcount = int(request.COOKIES['count'])+1
#             else:
#                 newcount = 1
#             response = render(request, 'cartApp/add.html', {'form':forms.add_items})
#             response.set_cookie(form.cleaned_data.get('item_name'), form.cleaned_data.get('quantity'))
#             # request.set_cookie('quantity'+str(newcount),form.cleaned_data.get('quantity'))
#             messages.success(request,f'{form.cleaned_data.get("item_name")} is successfully added!')
#             # return redirect('add_products')
#     else:
#         response = render(request, 'cartApp/add.html', {'form':forms.add_items})
#     return response

# def display(request):
#     # my_dic = { 'name' : request.COOKIES['name'],
#     #           'quantity' : request.COOKIES['quantity']}
#     return render(request, 'cartApp/display.html')

from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages

def home(request):
    return render(request, 'cartApp/home.html')

def add_products(request):
    if request.method == 'POST':
        form = forms.add_items(request.POST)
        if form.is_valid():
            # Determine the new count of items
            if 'count' in request.COOKIES:
                newcount = int(request.COOKIES['count']) + 1
            else:
                newcount = 1
            
            item_name = form.cleaned_data.get('item_name')
            quantity = form.cleaned_data.get('quantity')
            
            # Create a response object to set cookies on
            response = redirect('add_products')  # Redirect to the same view after setting cookies
            
            # Setting item name and quantity in cookies with unique keys
            response.set_cookie(f'item_name{newcount}', item_name)
            response.set_cookie(f'quantity{newcount}', quantity)
            
            # Update the count in cookies
            response.set_cookie('count', newcount)
            
            # Add a success message
            messages.success(request, f'{item_name} is successfully added!')
            return response
    else:
        form = forms.add_items()
    
    return render(request, 'cartApp/add.html', {'form': form})

def display(request):
    items = []
    if 'count' in request.COOKIES:
        count = int(request.COOKIES['count'])
        for i in range(1, count + 1):
            item_name = request.COOKIES.get(f'item_name{i}')
            quantity = request.COOKIES.get(f'quantity{i}')
            if item_name and quantity:
                items.append({'item_name': item_name, 'quantity': quantity})

    return render(request, 'cartApp/display.html', {'items': items})
