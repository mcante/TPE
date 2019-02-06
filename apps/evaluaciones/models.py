from django.db import models
from django.utils import timezone #Agregada por mi para el manejo de la fecha
import datetime
from django.contrib.auth.models import User

from decimal import Decimal


# Modelo Abstracto para poder ser heredado
class ControlCreaciones(models.Model):
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        abstract = True

# Modelo para la creación de versiones
class Version(ControlCreaciones):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=250)

    def __str__(self):
        return self.nombre
    

# Evaluacion hereda de ControlCreaciones con el fin de utilizar los campos de "creado y actualizado" en su modelo.
class Evaluacion(ControlCreaciones):
    empleado = models.ForeignKey(User, related_name='evaluacion_empleado', on_delete=models.CASCADE)
    version = models.ForeignKey(Version, related_name='versiones', on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.datetime.now, null=True, blank=True)
    evaluador = models.ForeignKey(User, related_name='evaluacion_evaluador', on_delete=models.CASCADE, null=True, blank=True)
    penalizado = models.BooleanField()
    porcentaje_penalizacion = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    aspectos_por_mejorar = models.TextField(verbose_name='Aspectos a Mejorar', null=True, blank=True)
    completado = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.empleado)
    
# Promedio de los indicadores evaluados.
    def get_total(self):
        suma = sum(t.calificacion.valor for t in self.evaluaciones.all()) # Primero sacar la suma de todos los resultados.
        indicadores = self.evaluaciones.all().count() # Luego sacar cuantos indicadores se tomaron en cuenta.
        return "{0:.2f}".format(suma/indicadores) # El promedio

# Calculo del Incentivo a recibir
    def get_incentivo(self):
        incentivo = self.empleado.usuarios.incentivo # Obtener el incentivo del empleado
        promedio = Decimal(self.get_total()) # Obtener el valor promedio de los indicadores evaluados
        total = (incentivo*promedio)/100 # Sacar el total a pagar... sino está penalizado será este el resultado sino se aplicará la penalización sobre este valor.
        if ( self.penalizado ): # Sí está penalizado entrará a la condición
            pena = Decimal(100-self.porcentaje_penalizacion)/100 # Obtener el porcentaje de panalización en decimales...
            print("Penalización: %" + str(pena)) # Mostrar en consola el pocentaje calculado.
            total = total * pena # Aplicar descuento de penalización al incentivo.
        return "{0:.2f}".format(total) # Devolver total del incentivo en formato con dos decimales.

    