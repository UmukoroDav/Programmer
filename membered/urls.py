"""
URL configuration for FIRSTAPP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import appindex, appregistration, appquery, appinfo, appcontact, appsignup, APIind, appprivate, RestApiVeiw
from django.urls import path
from .views import appStudentcrateveiw
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', appindex, name='appindex'),
    path('registration/', appregistration, name='appregistration'),
    path('query', appquery,name='appquery'),
    path('info', appinfo, name='appinfo'),
    path('contact/<int:pr>/', appcontact, name='appcontact'),
    path('signup/', appsignup, name='appsignup'),
    path('display/', appStudentcrateveiw.as_view(), name='rest'),
    path('APIind/<int:pk>/', APIind.as_view(), name='restapips'),
    path('private/', appprivate, name='private'),
    path('rest/', RestApiVeiw, name='restapi'),
]