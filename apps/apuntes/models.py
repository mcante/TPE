from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone #Agregada por mi para el manejo de la fecha
import datetime


# Create your models here.

class ControlCreaciones(models.Model):
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        abstract = True

class Categoria(ControlCreaciones):
    nombre = models.CharField(max_length=150)
    fecha = models.DateField(default=datetime.datetime.now, null=True, blank=True)
    descripcion = models.TextField(max_length=250, verbose_name="Descripción", null=True, blank=True)
    creado_por = models.ForeignKey(User, related_name='rel_Categoria_User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorías'
        ordering = '-nombre'

class Nota(ControlCreaciones):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField(null=True, blank=True, verbose_name="Nota")
    categoria = models.ForeignKey(Categoria, verbose_name="Categoría", on_delete=models.CASCADE, related_name='rel_Nota_Categoria')
    link = models.URLField(null=True, blank=True)
    fecha_recordatorio = models.DateField(null=True, blank=True)
    fecha = models.DateField(default=datetime.datetime.now, null=True, blank=True)
    hora = models.TimeField(default=datetime.datetime.now, null=True, blank=True)
    necesita_seguimiento = models.BooleanField(default=False)
    creado_por = models.ForeignKey(User, related_name='rel_Nota_User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{}: {}'.format(self.titulo, self.categoria)

    class meta:
        verbose_name='Nota'
        verbose_name_plural='Notas'
        ordering = '-titulo'

    def get_dias(self):
        if (self.fecha_recordatorio):
            dias = int((self.fecha_recordatorio - datetime.datetime.now().date()).days) # Se calculo la fecha actual contra el recordatorio
            if dias >=1:
                return dias
            else:
                return 0

        return False
    