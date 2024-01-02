from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account created has been created and now You are able to login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user_login/register.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'user_login/profile.html')
