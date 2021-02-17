"""final URL Configuration

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
from django.urls import path
from . import views 
from . import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("login",views.login,name="login"),
    path("loggedin",views.loggedin,name="loggedin"),
    path("Registered",views.registered,name="registered"),
    path("register",views.register,name="register"),
    path("read",views.read,name="read"),
    path("sports",views.sports,name="sports"),
    
    path("business",views.business,name="business"),
    path("movies",views.movies,name="movies"),
    path("politics",views.politics,name="politics"),
    

] 