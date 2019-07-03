from django.db import models
import datetime
from django.contrib.auth.models import User

from django.db.models import signals
from django.dispatch import receiver


# Modelo Abstracto para poder ser heredado
class ControlCreaciones(models.Model):
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        abstract = True


class Pasillo(models.Model):
    pass

    def __str__(self):
        return str(self.id)

    def tarimas(self):
        return Tarima.objects.filter(sector__nivel__pasillo=self)


class Nivel(models.Model):
    nivel = models.CharField(max_length=1)
    pasillo = models.ForeignKey(Pasillo, on_delete=models.PROTECT, related_name='relNivelPasillo')

    def __str__(self):
        return '{}{}'.format(self.pasillo, self.nivel)

    def tarimas(self):
        return Tarima.objects.filter(sector__nivel=self)


class Sector(models.Model):
    sector = models.IntegerField(null=False)
    nivel = models.ForeignKey(Nivel, related_name='relSectorNivel', on_delete=models.CASCADE)

    def __str__(self):
        return '{nivel}-{sector}'.format(nivel=self.nivel, sector=self.sector)



""" 
Estado de la Tarima:
-En Uso
-Libre = Vacía
-Dañada
"""
class EstadoTarima(models.Model):
    estado = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return '{}'.format(self.estado)


class Tarima(ControlCreaciones):
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT, null=True, blank=True, related_name='relTarimaSector')
    contenido = models.TextField(null=True, blank=True)
    estado = models.ForeignKey(EstadoTarima, on_delete=models.PROTECT, null=True, blank=True, related_name='relTarimaEstado')
    editado_por = models.ForeignKey(User, related_name='relTarimaUsuario', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class HistoricoTarima(ControlCreaciones):
    tarima = models.ForeignKey(Tarima, on_delete=models.PROTECT, null=True, blank=True, related_name='relHistoricoTarimaTarima')
    fecha = models.DateField(default=datetime.datetime.now, null=True, blank=True)
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT, null=True, blank=True, related_name='relHistoricoTarimaSector')
    contenido = models.TextField(null=True, blank=True)
    estado = models.ForeignKey(EstadoTarima, on_delete=models.PROTECT, null=True, blank=True, related_name='relHistoricoTarimaEstado')
    editado_por = models.ForeignKey(User, related_name='relHistoricoTarimaUsuario', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)



""" Agregar cambio al histórico.
*Colocando False se le indica que sólo sí no existe la -created- en el diccionario entre al if o True si ya existe.
"""
@receiver(signals.pre_save, sender=Tarima) 
def enviar_historico(sender, instance, **kwargs):
    
    #if kwargs.get('updated', True):
    if not instance._state.adding:
        print ("______________________________ ACTUALIZAR_____________________________")

        modificado = False

        # id de la tarima que tiene movimiento
        id_tarima = instance.id

        # Validar si no se seleccionó sector
        if (instance.sector):
            sector_tarima = Sector.objects.get(pk=instance.sector.id) # Si seleccionó obtener el valor
            
            if (Tarima.objects.get(pk=id_tarima).sector != None):
                antiguo_sector_tarima = Tarima.objects.get(pk=id_tarima).sector
            else:
                antiguo_sector_tarima = None

        else:
            sector_tarima = None # Sino selecciono marcar como None o nulo
            antiguo_sector_tarima = None
        
        # Validar si no se seleccionó estado
        if (instance.estado):
            estado_tarima = EstadoTarima.objects.get(pk=(instance.estado.id)) # Si seleccionó obtener el valor

            if(Tarima.objects.get(pk=id_tarima).estado != None):
                antiguo_estado_tarima = Tarima.objects.get(pk=id_tarima).estado
            else:
                antiguo_estado_tarima = None

        else:
            estado_tarima = None # Sino selecciono marcar como None o nulo
            antiguo_estado_tarima = None

        contenido_tarima = Tarima.objects.get(pk=id_tarima).contenido # Obtener el valor
        UsuarioTarima = User.objects.get(pk=Tarima.objects.get(pk=id_tarima).editado_por.id) # Obtener el valor

        # Valores antiguos print("\nid: " + str(id_tarima) + " -Sector: " + str(sector_tarima) + " -Contenido:" + str(contenido_tarima) + " -Estado: " + str(estado_tarima))
        # Valores nuevos print("\nid: " + str(instance.id) + " -Sector: " + str(instance.sector) + " -Contenido:" + str(instance.contenido) + " -Estado: " + str(instance.estado) + "\n\n")

        # print(str(antiguo_sector_tarima) + " --- " + str(instance.sector))
        # print(str(antiguo_estado_tarima) + " --- " + str(instance.estado))
        
        # Verificar si algún dato cambió
        if (antiguo_sector_tarima != instance.sector):
            modificado = True

        if (contenido_tarima != instance.contenido):
            modificado = True
        
        if (antiguo_estado_tarima != instance.estado):
            modificado = True
        
        
        # Si la variable es True es porque sí hubieron cambios y se creará el registro en el histórico.
        if (modificado):
            HistoricoTarima.objects.create(tarima=instance, sector=sector_tarima, contenido=instance.contenido, estado=estado_tarima, editado_por=UsuarioTarima)
        


