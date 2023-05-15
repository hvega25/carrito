#importa desde la libreria de rest framework
from rest_framework import serializers

#importa desde el model la clase producto
from .models import Producto

#libreria serializers
class ProductoSerializers (serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'