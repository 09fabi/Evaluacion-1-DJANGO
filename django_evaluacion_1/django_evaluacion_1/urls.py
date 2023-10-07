"""
URL configuration for django_evaluacion_1 project.

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
from django.contrib import admin
from django.urls import path
from productos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('mouse/', views.mouse),
    path('teclado/', views.teclado),
    path('auris/', views.auris),
    path('user/', views.user),
    path('mouse/1/', views.mouse1),
    path('mouse/2/', views.mouse2),
    path('mouse/3/', views.mouse3),
    path('teclado/1/', views.teclado1),
    path('teclado/2/', views.teclado2),
    path('teclado/3/', views.teclado3),
    path('auris/1/', views.auris1),
    path('auris/2/', views.auris2),
    path('auris/3/', views.auris3),
]
