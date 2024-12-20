from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Rota principal para a página index
    path('modelo/', views.modelo_view, name='modelo'),  # Página de modelo
    path('cadastro/', views.cadastro_view, name='cadastro'),  # Página de cadastro
    path('classificacao/', views.classificacao_view, name='classificacao'),  # Página de classificação
    path('iniciar/', views.iniciar_view, name='iniciar'),  # Página de iniciar
    path('redefinir-senha/', views.redefinir_senha_view, name='redefinir-senha'),  # Página de redefinir senha
    path('processar-redefinicao/', views.processar_redefinicao_view, name='processar-redefinicao'),  # Página de processar redefinição
    path('resultados/', views.resultados_view, name='resultados'),  # Página de resultados
    path('configuracao/', views.configuracao_view, name='configuracao'),  # Página de configuração
    
]
