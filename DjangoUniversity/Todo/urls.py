from django import views
from django.urls import URLPattern, path
from .import views

urlpatterns = [
    path("", views.home, name="home"),
    path("agregar/", views.agregar, name="agregar"),
    path("eliminar/<int:tarea_id>/", views.eliminar, name="eliminar"),
    path("editar/<int:tarea_id>/", views.editar, name="editar"),
]