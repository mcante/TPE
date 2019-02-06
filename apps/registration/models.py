from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone #Agregada por mi para el manejo de la fecha
from decimal import Decimal
from datetime import datetime

from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Area(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):
        return '{}'.format(self.nombre)
        
    class meta:
        verbose_name='área'
        verbose_name_plural='áreas'
        ordering = '-nombre'


class TipoEquipo(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True, unique=True)

    def __str__(self):
        return '{}'.format(self.nombre)
        
    class meta:
        verbose_name='Equipo'
        verbose_name_plural='Tipos de Equipo'
        ordering = '-nombre'


class EquipoCargado(models.Model):
    area = models.OneToOneField(Area, verbose_name="Área", on_delete=models.CASCADE, related_name='rel_EquipoCargado_Area')
    fecha_asignacion = models.DateField(null=True, blank=True, verbose_name="Fecha de Asignación")
    descripcion = models.TextField(null=True, blank=True, verbose_name="Descripción")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):
        return 'Área: {}. {}'.format(self.area, self.fecha_asignacion)
        
    class meta:
        verbose_name='Equipo Cargado'
        verbose_name_plural='Equipos cargados'
        ordering = '-area'

class AsignarEquipo(models.Model):
    asignacion = models.ForeignKey(EquipoCargado, verbose_name="Asignación", on_delete=models.CASCADE, related_name='rel_AsignarEquipo_EquipoCargado')
    tipo_equipo = models.ForeignKey(TipoEquipo, verbose_name="Tipo de Equipo", on_delete=models.CASCADE, related_name='rel_AsignarEquipo_TipoEquipo')
    cantidad = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    identificador = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(null=True, blank=True, verbose_name="Descripción")
    devolucion = models.BooleanField(default=False, verbose_name="Devolución")
    devuelve = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name='rel_AsignarEquipo_User', verbose_name="Quién devuelve")
    observaciones = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{}: {} - {}'.format(self.asignacion, self.tipo_equipo, self.identificador)
        
    class meta:
        verbose_name='Asignación de equipo'
        verbose_name_plural='Asignación de equipos'
        ordering = '-asignacion'
    


def elimina_imagen_cargada(instance, filename):
    old_instance = Perfil.objects.get(pk=instance.pk)
    old_instance.imagen.delete()
    return 'perfiles/' + filename



class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name='usuarios')
    imagen = models.ImageField(upload_to=elimina_imagen_cargada, blank=True, null=True)
    area = models.ForeignKey(Area, related_name='areas', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Área")
    incentivo = models.DecimalField(max_digits=6, decimal_places=2, null = True, blank = True, default=Decimal('0.00'))
    fecha_nacimiento = models.DateField(null=True, blank=True)
    fecha_ingreso = models.DateField(default=timezone.now)
    fecha_salida = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=False)
    sobre_mi = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return '{}'.format(self.user)
        
    class meta:
        verbose_name='perfil'
        verbose_name_plural='perfiles'
        ordering = '-user'

# Obtener el promedio anual del colaborador
    def get_anual(self):
        suma = sum(Decimal(t.get_total()) for t in self.user.evaluacion_empleado.all()) # Primero sacar la suma de todos los resultados.
        if (suma != 0):
            indicadores = self.user.evaluacion_empleado.all().count() # Luego sacar cuantos indicadores se tomaron en cuenta.
        else:
            return 0
        return "{0:.2f}".format(suma/indicadores) # El promedio
    

# Obtener las llamadas de atención del colaborador
    def get_faltas(self):
        faltas = self.user.faltas_empleados.all().count()
        print ("Faltas: " + str(faltas))
        return faltas

# Obtener los debe mejorar de todas las evaluaciones
    def get_mejoras(self):
        mejoras = sum(t.evaluaciones.filter(debe_mejorar=True).count() for t in self.user.evaluacion_empleado.all()) # Recorrer las evaluaciones y sus indicadores sumando todos los debe mejorar
        print("Mejoras: " + str(mejoras))
        return mejoras

    def get_tiempo(self):
        if (self.fecha_salida is True):
            return int((self.fecha_salida - self.fecha_ingreso).days / 365.2425) # Si ya no labora en la empresa se calcula con fecha de salida e ingreso.
        else:
            return int((datetime.now().date() - self.fecha_ingreso).days / 365.2425) # Si no ha salido de la empresa, se calcula con la fecha actual.


class Telefono(models.Model):
    numero = models.IntegerField(blank=True, null=True, verbose_name="Número")
    nota = models.CharField(max_length=150, blank=True, null=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='rel_Telefono_Perfil')

    def __str__(self):
        return '{}'.format(self.numero)
        
    class meta:
        verbose_name='Teléfono'
        verbose_name_plural='Teléfonos'
        ordering = '-numero'


# Signal para crear el perfil luego de crear un nuevo usuario.
@receiver(post_save, sender=User)
def crea_perfil(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Perfil.objects.get_or_create(user=instance)
        print("Se ha creado el perfil del usuario creado")