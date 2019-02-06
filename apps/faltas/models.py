from django.db import models

from django.utils import timezone #Agregada por mi para el manejo de la fecha
from django.contrib.auth.models import User

# Create your models here.

class LlamadaAtencion(models.Model):
    empleado = models.ForeignKey(User, related_name='faltas_empleados', on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now)
    motivo = models.TextField(null=True, blank=True, max_length=250)
    penalizacion = models.BooleanField()
    levantada_por = models.ManyToManyField(User, related_name='levantada', blank=True)
    tiempo = models.CharField(max_length=150, null=True, blank=True)
    compromiso = models.TextField(max_length=250, null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")


    def __str__(self):
        return '{}'.format(self.empleado)
        
    class meta:
        verbose_name='Llamada de atención'
        verbose_name_plural='Llamadas de atención'
        ordering = '-fecha'
