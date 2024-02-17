"""isntrack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user import views as user_view
from django.contrib.auth import views as auth_view
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def index_view(request):
   if request.user.is_authenticated:
        return redirect('dashboard-index')  #  Assuming that's your dashboard URL name
   else:
        return redirect('user-login')  # Redirect to login if not authenticated

urlpatterns = [
    path('', index_view, name='root-index'), # Root-level  view and URL configuration 
    path('admin/', admin.site.urls),
    path('login/', auth_view.LoginView.as_view(template_name='user/login.html'), name='user-login'),
    path('dashboard/', include('dashboard.urls')),
    path('register/', user_view.register, name='user-register'),
    path('logout/', auth_view.LogoutView.as_view(template_name='user/logout.html'), name='user-logout'),
    path('profile/', user_view.profile, name='user-profile'),
]
