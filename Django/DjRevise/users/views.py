from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from . import form
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        Form = form.UserRegisterForm(request.POST)
        if Form.is_valid():
            Form.save(commit=True)
            username = Form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} successfully!')
            return redirect('user_login')
    else:
        Form = form.UserRegisterForm()
    return render(request,'users/register.html',{'form':Form})

@login_required
def profile(request):
    return render(request,'users/profile.html')