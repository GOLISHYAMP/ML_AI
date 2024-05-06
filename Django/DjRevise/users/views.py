from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .form import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        Form = UserRegisterForm(request.POST)
        if Form.is_valid():
            Form.save()
            username = Form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} successfully!')
            return redirect('user_login')
    else:
        Form = UserRegisterForm()
    return render(request,'users/register.html',{'form':Form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('user_profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form':u_form,
            'p_form':p_form
        }
        return render(request,'users/profile.html',context)