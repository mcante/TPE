from django.db import models

from apps.evaluaciones.models import Evaluacion

# Create your models here.

class ControlCreaciones(models.Model):
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        abstract = True

class Area(ControlCreaciones):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return '{}: {}'.format(self.nombre, self.descripcion)

class Indicador(ControlCreaciones):
    nombre = models.CharField(max_length=150)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    class meta:
        verbose_name='Indicador'
        verbose_name_plural='Indicadores'
        ordering = '-id'

    def __str__(self):
        return '{}: {}'.format(self.nombre, self.area.nombre)

class Calificacion(ControlCreaciones):
    rango = models.CharField(max_length=150)
    valor = models.PositiveSmallIntegerField(null=True, blank=True)
    rubrica = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return '{}: {}'.format(self.rango, self.valor)

class AsignacionIndicadores(ControlCreaciones):
    evaluacion = models.ForeignKey(Evaluacion, related_name='evaluaciones', on_delete=models.CASCADE)
    indicador = models.ForeignKey(Indicador, related_name='indicadores', on_delete=models.CASCADE)
    calificacion = models.ForeignKey(Calificacion, related_name='calificaciones', on_delete=models.CASCADE, default=5)
    observaciones_encargado = models.TextField(null=True, blank=True)
    compromiso_del_evaluado = models.TextField(null=True, blank=True)
    debe_mejorar = models.BooleanField(default=False)

    def __str__(self):
        return '{}: {}'.format(self.evaluacion, self.indicador)



        