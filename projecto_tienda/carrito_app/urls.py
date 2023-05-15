from django.urls import path,include
from . import views

urlpatterns = [
    #ruta para vista de views
    path('', views.home),
    #ruta para listar y agregar
    path('registroProducto/', views.registroProducto),
    #url para eliminar
    path('eliminarProducto/<nombre>', views.eliminarProducto),
    #eliminar completo 
    path('eliminarTodosLosProductos/' , views.eliminarTodosLosProductos),
    #editar curso
    path('edicionProducto/<nombre>', views.edicionProducto),
    path('editarProducto/', views.editarProducto)
]