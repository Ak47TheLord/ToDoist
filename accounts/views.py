from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from . import forms as account_forms

# Create your views here.
from .models import UserProfile


@csrf_exempt
def sign_in(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])
        if user is not None:
            login(request, user)
            message = f'Hello {user.username}! You have been logged in'
            messages.success(request, message)
            return redirect('todo-dashboard')
        else:
            message = 'Login Failed'
            messages.error(request, message)
            return redirect('accounts-signin')
    return render(request, 'account/sign-in.html')


@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'That email is being used')
            return redirect('accounts-signup')
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'That email is being used')
                return redirect('accounts-signup')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                UserProfile.objects.create(user=user)
                messages.success(request, 'You are now registered and can log in')
                return redirect('accounts-signin')

    return render(request, 'account/sign-up.html')


@login_required(login_url='accounts-sigin')  # redirect when user is not logged in
def sign_out(request):
    logout(request)
    messages.success(request, "Logout Successfully!")
    return redirect('accounts-signin')


@login_required(login_url='accounts-sigin')
def profile(request):
    user = request.user
    userprofile_form = account_forms.UserProfileForm(request.POST or None, instance=request.user.userprofile)
    context = {
        'user': user,
        'userprofile_form': userprofile_form,
        'read_only': True,
        'active_cls': 'active',
    }
    return render(request, 'account/profile.html', context)


@login_required(login_url='accounts-sigin')
def edit_profile(request):
    userprofile_form = account_forms.UserProfileForm(request.POST or None, instance=request.user.userprofile)
    if request.method == "POST":
        if userprofile_form.is_valid():
            userprofile_form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('accounts-userprofile-profile')
        else:
            messages.error(request, "Please resolve the errors below!")
    context = {
        "title": "Edit profile",
        "userprofile_form": userprofile_form,
        'edit': True,
        'active_cls': 'active',
        # "nav": {
        #     "active": "profile",
        #     "collapse": {
        #         "target_class": "info",
        #         "child": "profile"
        #     }
        # }

    }
    return render(request, "account/profile.html", context)


@login_required(login_url='accounts-sigin')
def edit_profile_picture(request):
    form = account_forms.UserProfileImageForm(request.POST, request.FILES, instance=request.user.userprofile)
    if request.method == "POST":
        if form.is_valid():
            profile = form.save()
            request.session["image"] = profile.image.url
            messages.success(request, " Profile image updated successfully!")
        else:
            messages.error(request, " Please provide valid image!")

    return redirect(reverse("accounts-userprofile-profile"))


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts-userprofile-profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "title": "Update Password",
        "form": form,
        # "nav": {
        #     "active": "password",
        #     "collapse": {
        #         "target_class": "info",
        #         "child": "password"
        #     }
        # }
    }
    return render(request, 'account/password.html', context)
