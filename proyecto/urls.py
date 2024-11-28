from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('proyectos/', views.proyecto_list, name='proyecto_list'),
    path('proyectos/new/', views.proyecto_create, name='proyecto_create'),
    path('proyectos/<int:pk>/edit/', views.proyecto_update, name='proyecto_update'),
    path('proyectos/<int:pk>/delete/', views.proyecto_delete, name='proyecto_delete'),
]
