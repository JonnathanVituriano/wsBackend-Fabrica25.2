from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_comidas, name='listar_comidas'),
    path('adicionar/', views.adicionar_comida, name='adicionar_comida'),
    path('editar/<int:pk>/', views.editar_comida, name='editar_comida'),
    path('deletar/<int:pk>/', views.deletar_comida, name='deletar_comida'),
    path('buscar/', views.buscar_comidas_api, name='buscar_comidas_api'),
]