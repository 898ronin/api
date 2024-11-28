from django.urls import path
from . import views
from .api import ProyectoViewSet

urlpatterns = [
    # Rutas HTML
    path('', views.index, name='index'),
    path('proyectos/', views.proyecto_list, name='proyecto_list'),
    path('proyectos/new/', views.proyecto_create, name='proyecto_create'),
    path('proyectos/<int:pk>/edit/', views.proyecto_update, name='proyecto_update'),
    path('proyectos/<int:pk>/delete/', views.proyecto_delete, name='proyecto_delete'),

    # Rutas de API
    path('api/proyectos/', ProyectoViewSet.as_view({'get': 'list'}), name='proyecto_api_list'),
    path('api/proyectos/<int:pk>/', ProyectoViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name='proyecto_api_detail'),
]

