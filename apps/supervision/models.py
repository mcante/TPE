from django.db import models
import datetime
from django.contrib.auth.models import User


# Modelo Abstracto para poder ser heredado
class ControlCreaciones(models.Model):
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        abstract = True

# Tipos de movimientos Solicitud y Devolución
class TipoMovimiento(models.Model):
    tipo = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return '{}'.format(self.tipo)


# Supervisión de Movimientos con herencia al control de Creaciones
class Movimiento(ControlCreaciones):

    movimiento = models.IntegerField(null=False, blank=False, unique=True)
    tipo = models.ForeignKey(TipoMovimiento, related_name='relMovimientoTipo', on_delete=models.CASCADE)
    desecho = models.BooleanField(default=False)
    dispositivo = models.CharField(max_length=100, null=False, blank=False)
    cantidad = models.PositiveSmallIntegerField(null=False, blank=False, default=0)
    fecha = models.DateField(default=datetime.datetime.now, null=False, blank=False)
    entrega = models.ForeignKey(User, related_name='relMovimientoUsuarioEntrega', on_delete=models.CASCADE)
    recibe = models.ForeignKey(User, related_name='relMovimientoUsuarioRecibe', on_delete=models.CASCADE)
    creado_en_suni = models.BooleanField(default=False)
    hoja_impresa = models.BooleanField(default=False)
    genera_kardex = models.BooleanField(default=False)
    kardex = models.IntegerField(verbose_name='No. Kardex', null=True, blank=True)
    registro_en_correo = models.BooleanField(default=False)
    observaciones = models.TextField(verbose_name='Observaciones', null=True, blank=True)
    supervisado_por = models.ForeignKey(User, related_name='relMovimientoUsuarioSupervisa', on_delete=models.CASCADE)
    supervision_completada = models.BooleanField(default=False)
        
    def __str__(self):
        return '{}'.format(self.movimiento)





# Supervisión de SUNI-Entradas-Depuración a Kardex.
class Entrada(ControlCreaciones):

    entrada = models.PositiveSmallIntegerField(null=False, blank=False)
    fecha = models.DateField(default=datetime.datetime.now, null=False, blank=False)
    entrega = models.ForeignKey(User, related_name='relEntradaUsuarioEntrega', on_delete=models.CASCADE)
    recibe = models.ForeignKey(User, related_name='relEntradaUsuarioRecibe', on_delete=models.CASCADE)
    creado_en_suni = models.BooleanField(default=False)
    hoja_impresa = models.BooleanField(default=False)
    kardex = models.IntegerField(verbose_name='No. Kardex', null=True, blank=True)
    registro_en_correo = models.BooleanField(default=False)
    observaciones = models.TextField(verbose_name='Observaciones', null=True, blank=True)
    supervisado_por = models.ForeignKey(User, related_name='relEntradaUsuarioSupervisa', on_delete=models.CASCADE)
    cerrar = models.BooleanField(default=False)
        
    def __str__(self):
        return '{}'.format(self.entrada)



# Detalle de la depuración
class DetalleDepuracion(models.Model):

    entrada = models.ForeignKey(Entrada, related_name='relDepuracionEntrada', on_delete=models.CASCADE)
    dispositivo = models.CharField(max_length=100)
    cantidad = models.PositiveSmallIntegerField(null=False, blank=False, default=0)
    observaciones = models.TextField(verbose_name='Observaciones', null=True, blank=True)
        
    def __str__(self):
        return '{} - {}'.format(self.cantidad, self.dispositivo)