from django.shortcuts import render,redirect

from rest_framework import viewsets

from .serializers import ProductoSerializers

from .models import Producto

from django.contrib import messages
#viewset api
class ProductosViewset(viewsets.ModelViewSet):
    #variable que lista todos los cursos
    queryset = Producto.objects.all()

    serializer_class = ProductoSerializers


#vista para lectura de base de datos
def home (request):
    producto = Producto.objects.all()
    return render(request, "gestion_carrito.html", {"prod":producto})

#vista para agregar curso
def registroProducto(request):

    nombre=request.POST['txtNombre']
    descripcion=request.POST['txtDescripcion']
    precio=request.POST['numPrecio']
    cantidad=request.POST['numCantidad']
    metodo_envio=request.POST['txtMetodo']

    producto = Producto.objects.create(nombre=nombre, descripcion=descripcion, precio=precio,cantidad=cantidad,metodo_envio=metodo_envio)
    return redirect('/')

#vista para eliminar producto
def eliminarProducto(request, nombre):

    producto = Producto.objects.get(nombre=nombre)
    producto.delete()
  
    return redirect('/')

#vista para eliminar el carrito
def eliminarTodosLosProductos(request):
    productos = Producto.objects.all()
    productos.delete()
    return redirect('/')

#vista para editar producto
def edicionProducto(request, nombre):

    producto = Producto.objects.get(nombre=nombre)
    
    return render(request,"edicionProducto.html" , {"prod":producto})


#vista para guardar el producto actualizado
def editarProducto(request):
    nombre=request.POST['txtNombre']
    descripcion=request.POST['txtDescripcion']
    precio=request.POST['numPrecio']
    cantidad=request.POST['numCantidad']
    metodo_envio=request.POST['txtMetodo']

    producto = Producto.objects.get(nombre=nombre)
    producto.descripcion = descripcion
    producto.precio = precio
    producto.cantidad = cantidad
    producto.metodo_envio = metodo_envio

    producto.save()

    messages.success(request, '¡Producto actualizado!')

    return redirect('/')