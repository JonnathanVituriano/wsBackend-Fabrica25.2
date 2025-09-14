
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'comidas', views.ComidaViewSet)

urlpatterns = [
    path('', views.listar_comidas, name='listar_comidas'),
    path('adicionar/', views.adicionar_comida, name='adicionar_comida'),
    path('editar/<int:pk>/', views.editar_comida, name='editar_comida'),
    path('deletar/<int:pk>/', views.deletar_comida, name='deletar_comida'),
    path('buscar/', views.buscar_comidas_api, name='buscar_comidas_api'),
    path('adicionar-categoria/', views.adicionar_categoria, name='adicionar_categoria'),
    path('api/', include(router.urls)),
]