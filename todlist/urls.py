from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('dashboard', dashboard, name='todo-dashboard'),


    # path('login/', auth_views.LoginView.as_view(template_name='account/sign-in.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='account/sign-in.html'), name='logout'),
    # path('park/', park, name='parkin')


]