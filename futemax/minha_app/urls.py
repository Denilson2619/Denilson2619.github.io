from django.urls import path
from . import views

urlpatterns = [
    path('jogo/', views.jogo, name='jogo')
]