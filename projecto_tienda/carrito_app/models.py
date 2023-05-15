from django.db import models

#crear la tabla en la base de datos
class Producto(models.Model):
    #variables que se insertaran en nuestra tabla en la base de datos
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    cantidad = models.PositiveIntegerField()
    metodo_envio = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        texto = "{0}{{1}}"
        return texto.format(self.nombre , self.descripcion)
