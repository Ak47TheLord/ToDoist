from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('accounts/signin', sign_in, name='accounts-signin'),
    path('accounts/signup', sign_up, name='accounts-signup'),
    path('accounts/signout', sign_out, name='accounts-signout'),
    path('accounts/userprofile', profile, name='accounts-userprofile-profile'),
    path("accounts/userprofile/editprofile", edit_profile, name="accounts-userprofile-edit-profile"),
    path("accounts/userprofile/password", change_password, name="accounts-userprofile-password"),
    path("accounts/userprofile/image", edit_profile_picture, name="accounts-userprofile-image"),

]


def account_signin():
    return reverse("accounts-signin")


def account_signup():
    return reverse("accounts-signup")


def account_userprofile_profile():
    return reverse("accounts-userprofile-profile")


def account_userprofile_edit_profile():
    return reverse("accounts-userprofile-edit-profile")


def account_userprofile_password():
    return reverse("accounts-userprofile-edit-profile")


def account_userprofile_image():
    return reverse("<accounts-userprofile-image")
