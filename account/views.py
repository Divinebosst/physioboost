from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from account.forms import RegistrationForm, EditProfileForm
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib import messages
from django.core import serializers
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:dash')
        
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard:dash')
    else:
        form = RegistrationForm()
    return render(request, 'account/signup.html', {'form':form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:dash')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('dashboard:dash')
        else:
            messages.warning(request, 'Please enter the correct details')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form':form})
    
def logout_view(request):
    logout(request)
    return redirect('account:login')

@login_required(login_url="/account/login/")
def view_profile(request):
    args = {'user' : request.user}
    return render(request, 'account/profile.html', args)

@login_required(login_url="/account/login/")
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile changed successfully!!!')
            return redirect('account:edit_profile')
        else:
            messages.warning(request, 'Please correct the error below.') 
    else:
        form = EditProfileForm(instance = request.user)
    return render(request, 'account/edit_profile.html', {'form':form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password changed successfully!!!')
        else:
            messages.warning(request, 'Please correct the error below.') 
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request, 'account/change_password.html', {'form':form})