from django.db import models
from django.utils import timezone #Agregada por mi para el manejo de la fecha
import datetime
from django.contrib.auth.models import User

from decimal import Decimal

from apps.equipamientos.models import Equipamiento


# Modelo Abstracto para poder ser heredado
class ControlCreaciones(models.Model):
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        abstract = True

class Companias_telefonia(models.Model):
    empresa = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.empresa)




# EMPRESA RENTADORA DE VEHÍCULOS
class Rentadora(ControlCreaciones):
    nombre = models.CharField(max_length=150, null=True, blank=True)
    contacto = models.CharField(max_length=150, null=True, blank=True)
    agregado_por = models.ForeignKey(User, related_name='rel_Rentadora_User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.nombre)


class Telefonos_Rentadora(ControlCreaciones):
    rentadora = models.ForeignKey(Rentadora, related_name='rel_Telefonos_Rentadora', on_delete=models.CASCADE, null=True, blank=True)
    numero = models.CharField(max_length=15, null=True, blank=True)
    pertenece_a = models.CharField(max_length=50, null=True, blank=True)
    compania = models.ForeignKey(User, related_name='rel_Telefonos_User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'Rentadora: {} - Número{}'.format(self.rentadora, self.numero)




# PILOTOS
class Pilotos(ControlCreaciones):
    nombre_completo = models.CharField(max_length=200, null=True, blank=True)
    numero_lincencia = models.CharField(max_length=25, null=True, blank=True)
    tipo = models.CharField(max_length=2, null=True, blank=True)
    link_scan = models.URLField(null=True, blank=True)
    dpi = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.nombre)


class Telefonos_Piloto(ControlCreaciones):
    piloto = models.ForeignKey(Pilotos, related_name='rel_Telefonos_Piloto', on_delete=models.CASCADE, null=True, blank=True)
    numero = models.CharField(max_length=15, null=True, blank=True)
    pertenece_a = models.CharField(max_length=50, null=True, blank=True)
    compania = models.ForeignKey(User, related_name='rel_TelefonosPiloto_User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'Piloto: {} - Número{}'.format(self.piloto, self.numero)





# VEHÍCULOS
class Marcas(models.Model):
    marca = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return '{}'.format(self.marca)


class Modelos(models.Model):
    modelo = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return '{}'.format(self.modelo)

class Vehiculos(ControlCreaciones):
    rentadora = models.ForeignKey(Rentadora, related_name='rel_Vehiculo_Rentadora', on_delete=models.CASCADE, null=True, blank=True)
    marca = models.ForeignKey(Marcas, related_name='rel_Vehiculo_Marca', on_delete=models.CASCADE, null=True, blank=True)
    modelo = models.ForeignKey(Modelos, related_name='rel_Vehiculo_Modelo', on_delete=models.CASCADE, null=True, blank=True)
    placa = models.CharField(max_length=25, null=True, blank=True)
    combustible = models.CharField(max_length=25, null=True, blank=True)
    fotos = models.URLField(null=True, blank=True)
    fecha_solicitud = models.DateField(default=datetime.datetime.now, null=True, blank=True)
    
    fecha_recepcion = models.DateField(default=datetime.datetime.now, null=True, blank=True)
    hora_recepcion = models.TimeField(default=datetime.datetime.now, null=True, blank=True)
    quien_recibe = models.ForeignKey(User, related_name='rel_VehiculosRecibe_User', on_delete=models.CASCADE, null=True, blank=True)
    kilometraje_recibido = models.CharField(max_length=50, null=True, blank=True)
    
    quien_devuelve = models.ForeignKey(User, related_name='rel_VehiculosDevuelve_User', on_delete=models.CASCADE, null=True, blank=True)
    fecha_devolucion = models.DateField(default=datetime.datetime.now, null=True, blank=True)
    hora_hora = models.TimeField(default=datetime.datetime.now, null=True, blank=True)
    kilometraje_devuelto = models.CharField(max_length=50, null=True, blank=True)
    anotaciones = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return '{}, {}: {}'.format(self.marca, self.modelo, self.placa)






# RUTA DE ENTREGA

class Rutas(ControlCreaciones):
    fecha_salida = models.DateField(default=datetime.datetime.now, null=True, blank=True)
    fecha_entrada = models.DateField(default=datetime.datetime.now, null=True, blank=True)
    piloto = models.ForeignKey(Pilotos, related_name='rel_Rutas_Pilotos', on_delete=models.CASCADE, null=True, blank=True)
    vehiculo = models.ForeignKey(Vehiculos, related_name='rel_Rutas_Vehiculo', on_delete=models.CASCADE, null=True, blank=True)
    anotaciones = models.TextField(max_length=250, null=True, blank=True)
    completado = models.BooleanField(default=False)
    creado_por = models.ForeignKey(User, related_name='rel_Rutas_User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.fecha_salida)


class Ruta_Entregas(ControlCreaciones):
    entrega = models.ForeignKey(Equipamiento, related_name='rel_Rutas_Entrega', on_delete=models.CASCADE, null=True, blank=True)
    ruta = models.ForeignKey(Rutas, related_name='rel_Ruta_Rutas', on_delete=models.CASCADE, null=True, blank=True)    
    completado = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.entrega, self.ruta)






# REGISTRO DE EVENTOS DURANTE LA RUTA PROGRAMADA

class Estados(models.Model):
    estado = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return '{}'.format(self.estado)

class Eventos(ControlCreaciones):
    ruta_entrega = models.ForeignKey(Ruta_Entregas, related_name='rel_Eventos_RutaEntregas', on_delete=models.CASCADE, null=True, blank=True)
    evento = models.ForeignKey(Estados, related_name='rel_Eventos_Estados', on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateField(default=datetime.datetime.now, null=True, blank=True)
    anotaciones = models.TextField(max_length=250, null=True, blank=True)
    link_fotos = models.URLField(null=True, blank=True)
    latitud = models.CharField(max_length=25, null=True, blank=True)
    longitud = models.CharField(max_length=25, null=True, blank=True)
    creado_por = models.ForeignKey(User, related_name='rel_Eventos_User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{}: {}'.format(self.ruta_entrega, self.evento)