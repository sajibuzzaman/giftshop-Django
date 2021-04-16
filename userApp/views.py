from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from .models import UserProfile
from giftshopApp.models import Slider

# Create your views here.
def user_signup(request):
    slider = Slider.objects.get(default=True)

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password_raw = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password_raw)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = 'user_img/default.jpg'
            data.save()

            return redirect('home')
        # else:
        #     messages.warning(request, "Your new and reset password is not matching")
    else:
        form = SignUpForm()
    context = {
        'slider' : slider,
        'form' : form,
    }
    return render(request, 'userApp/user_signup.html',context)

def user_login(request):
    slider = Slider.objects.get(default=True)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

        else:
             messages.warning(request, "Username or Password is Wrong!!")
    


    context = {
        'slider' : slider,
        
    }
    return render(request, 'userApp/user_login.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')

def user_profile(request):
    slider = Slider.objects.get(default=True)
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)

    context = {
        'slider' : slider,
        'profile' : profile,
    }
    return render(request, 'userApp/user_profile.html', context)

@login_required(login_url='/user/login')
def user_update(request):
    slider = Slider.objects.get(default=True)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance= request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance= request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your Account has been Updated!")
            return redirect('user_profile')
        else:
            messages.success(request, "Username already registered!")
            return redirect('user_update')
    else:
        
        user_form = UserUpdateForm(instance = request.user)
        profile_form = ProfileUpdateForm(instance= request.user.userprofile)
        context ={
            'slider' : slider,
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'userApp/userupdate.html', context)