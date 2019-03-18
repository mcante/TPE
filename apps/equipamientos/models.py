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


    



# EQUIPAMIENTOS
class Equipamiento(ControlCreaciones):
    entrega = models.CharField(max_length=10, null=True, blank=True)
    udi = models.CharField(max_length=15, null=True, blank=True)
    destino = models.CharField(max_length=250, null=True, blank=True)
    latitud = models.CharField(max_length=25, null=True, blank=True)
    longitud = models.CharField(max_length=25, null=True, blank=True)
    creado_por = models.ForeignKey(User, related_name='rel_Equipamiento_User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.entrega)
    
class Dispositivo(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Cambio_Equipo(ControlCreaciones):
    entrega = models.ForeignKey(Equipamiento, related_name='rel_CambioEquipo_Equipamiento', on_delete=models.CASCADE)
    link_scan = models.URLField(null=True, blank=True)
    dispositivo = models.ForeignKey(Dispositivo, related_name='rel_CambioEquipo_Dispositivo', on_delete=models.CASCADE)
    triage_malo = models.CharField(max_length=10, null=True, blank=True)
    falla = models.TextField(max_length=150, null=True, blank=True)
    triage_bueno = models.CharField(max_length=10, null=True, blank=True)
    hecho_por = models.ForeignKey(User, related_name='rel_CambioEquipo_User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'Entrega: {}, triage malo: {}, triage bueno{}'.format(self.entrega, self.triage_malo, self.triage_bueno)






# VALORACIÓN DE ENTREGA DE PRODUCTOS DURANTE EQUIPAMIENTO
class Valoraciones(models.Model):
    valoracion = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return self.valoracion
    
class Productos_Entregados(ControlCreaciones):
    entrega = models.ForeignKey(Equipamiento, related_name='rel_ProductosEntregados_Equipamiento', on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.datetime.now, null=True, blank=True)
    link_scan = models.URLField(null=True, blank=True)
    entregado_por = models.ForeignKey(User, related_name='rel_ProductosEntregados_User', on_delete=models.CASCADE, null=True, blank=True)
    encargado_recibe = models.CharField(max_length=100, null=True, blank=True)
    anotaciones = models.TextField(max_length=250, null=True, blank=True)
    estrellas = models.ForeignKey(Valoraciones, related_name='rel_ProductosEntregados_Valoracion', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'Entrega: {}, fecha: {}'.format(self.entrega, self.fecha)

class Productos(ControlCreaciones):
    producto = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.producto)

class Producto_Lista(models.Model):
    formulario = models.ForeignKey(Productos_Entregados, related_name='rel_ProductoLista_ProductosEntregados', on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, related_name='rel_ProductoLista_Productos', on_delete=models.CASCADE, null=True, blank=True)
    entregado = models.BooleanField(default=False)
    anotaciones = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return 'Producto: {}, Entregado: {}'.format(self.producto, self.entregado)




# HOJA DE INCONVENIENTES DURANTE EL EQUIPAMEINTO
class Inconvenientes(ControlCreaciones):
    entrega = models.ForeignKey(Equipamiento, related_name='rel_Inconvenientes_Equipamiento', on_delete=models.CASCADE)
    fecha_reporte = models.DateField(default=datetime.datetime.now, null=True, blank=True)
    encargado_que_recibe = models.CharField(max_length=100, null=True, blank=True)
    link_fotos = models.URLField(null=True, blank=True)
    condiciones = models.TextField(max_length=250, null=True, blank=True)
    recomendaciones = models.TextField(max_length=250, null=True, blank=True)
    resuelto = models.BooleanField(default=False)
    fecha_resuelto = models.DateField(default=datetime.datetime.now, null=True, blank=True)
    link_scan = models.URLField(null=True, blank=True)
    creado_por = models.ForeignKey(User, related_name='rel_Inconvenientes_User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'Entrega: {}, Resuelto: {}'.format(self.entrega, self.resuelto)

class Aspectos(ControlCreaciones):
    aspecto = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.aspecto)

class Aspectos_Evaluados(models.Model):
    inconveniente = models.ForeignKey(Inconvenientes, related_name='rel_AspectosEvaluados_Inconvenientes', on_delete=models.CASCADE)
    aspecto = models.ForeignKey(Aspectos, related_name='rel_AspectosEvaluados_Aspectos', on_delete=models.CASCADE, null=True, blank=True)
    cumple = models.BooleanField(default=False)
    anotaciones = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return 'Inconveniente: {}, Aspecto: {}'.format(self.inconveniente, self.aspecto)
