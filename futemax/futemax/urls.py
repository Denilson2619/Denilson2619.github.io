"""futemax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.http import HttpResponse  # Adicionado para criar uma view simples

def home(request):
    return HttpResponse("Bem-vindo ao Futemax!")  # Página inicial do site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Adiciona a rota para a URL raiz
    path('minha_app/', include('minha_app.urls')),
]
