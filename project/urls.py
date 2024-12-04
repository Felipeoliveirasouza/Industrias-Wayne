"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app.views import home, create, store, painel, dologin, dashboard, logouts, changePassword, add_resource, edit_resource, delete_resource

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('store/', store, name='store'),
    path('painel/', painel, name='painel'),
    path('dologin/', dologin, name='dologin'),
    path('dashboard/', dashboard, name='dashboard'), 
    path('logout/', logouts, name='logout'),
    path('password/', changePassword, name='change_password'),
    path('add_resource/', add_resource, name='add_resource'),
    path('edit_resource/<int:id>/', edit_resource, name='edit_resource'),
    path('delete_resource/<int:id>/', delete_resource, name='delete_resource'),
]
