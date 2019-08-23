from django.db import models
import datetime
from decimal import Decimal
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
        



# ******** CONTROL DE TRIAGE ********

""" Dispositivo
CPU, MONITOR, TECLADO, MOUSE, LAPTOP, TABLET, DISCO DURO
"""
class DispositivosTriage(models.Model):
    dispositivo = models.CharField(max_length=100, null=False, blank=False)
    identificador = models.CharField(max_length=15, null=True, blank=True)
    
    def __str__(self):
        return str(self.dispositivo)

""" Tipo de Entrada
Donación, Compra, Renovación, Reingreso, Etc.
"""
class TiposEntrada(models.Model):
    tipo = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return str(self.tipo)

""" Estado de la Entrada
Útil o Repuesto
"""
class InventarioEntrada(models.Model):
    tipo = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return str(self.tipo)

class ControlTriage(ControlCreaciones):
    no_entrada = models.PositiveSmallIntegerField(null=False, unique=True)
    fecha_entrada = models.DateField(default=datetime.datetime.now, null=True, blank=True)
    ingresa_como = models.ForeignKey(TiposEntrada, on_delete=models.PROTECT, null=True, blank=True, related_name='relControlTriageTiposEntrada')
    
    completado = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.no_entrada)
    
class RegistrarTriage(models.Model):
    no_entrada = models.ForeignKey(ControlTriage, on_delete=models.PROTECT, null=True, blank=True, related_name='relRegistrarTriageControlTriage')
    dispositivo = models.ForeignKey(DispositivosTriage, on_delete=models.PROTECT, null=True, blank=True, related_name='relRegistrarTriageDispositivosTriage')
    cantidad = models.PositiveSmallIntegerField(null=False)
    a_inventario_de = models.ForeignKey(InventarioEntrada, on_delete=models.PROTECT, null=True, blank=True, related_name='relRegistrarTriageInventarioEntrada')

    creado_por = models.ForeignKey(User, related_name='relRegistrarTriageCreadoPor', on_delete=models.CASCADE, null=True, blank=True)
    fecha_creacion = models.DateField(default=datetime.datetime.now, null=True, blank=True)

    rando_inicia = models.PositiveSmallIntegerField(null=False)
    rando_termina = models.PositiveSmallIntegerField(null=False)

    def __str__(self):
        return '{} - {}: {}'.format(self.no_entrada, self.dispositivo, self.cantidad)
    


class DespachoTriage(models.Model):
    no_entrada = models.ForeignKey(ControlTriage, on_delete=models.PROTECT, null=True, blank=True, related_name='relDespachoTriageControlTriage')
    dispositivo = models.ForeignKey(DispositivosTriage, on_delete=models.PROTECT, null=True, blank=True, related_name='relDespachoTriageDispositivosTriage')
    cantidad = models.PositiveSmallIntegerField(null=False)
    a_inventario_de = models.ForeignKey(InventarioEntrada, on_delete=models.PROTECT, null=True, blank=True, related_name='relDespachoTriageInventarioEntrada')

    rando_inicia = models.PositiveSmallIntegerField(null=False)
    rando_termina = models.PositiveSmallIntegerField(null=False)

    fecha_entrega = models.DateField(default=datetime.datetime.now, null=True, blank=True)
    entrega = models.ForeignKey(User, related_name='relDespachoTriageReimpresosEntrega', on_delete=models.CASCADE, null=True, blank=True)
    recibe = models.ForeignKey(User, related_name='relDespachoTriageReimpresosRecibe', on_delete=models.CASCADE)
    firma_digital = models.BooleanField(default=False, verbose_name='Confirmar de recibido')

    def __str__(self):
        return '{}'.format(self.no_entrada)



class ControlTriageReimpresos(ControlCreaciones):
    dispositivo = models.ForeignKey(DispositivosTriage, on_delete=models.PROTECT, null=True, blank=True, related_name='relControlTriageReimpresosDispositivosTriage')
    autorizado_por = models.ForeignKey(User, related_name='relControlTriageReimpresosAutorizadoPor', on_delete=models.CASCADE)
    motivo_reimpresion = models.TextField(verbose_name='Motivo de la Reimpresión', null=True, blank=True)
    
    fecha_reimpresion = models.DateField(default=datetime.datetime.now, null=True, blank=True)
    triage = models.PositiveSmallIntegerField(null=False)    
    
    fecha_entrega = models.DateField(default=datetime.datetime.now, null=True, blank=True)
    entrega = models.ForeignKey(User, related_name='relControlTriageReimpresosEntrega', on_delete=models.CASCADE, null=True, blank=True)
    recibe = models.ForeignKey(User, related_name='relControlTriageReimpresosRecibe', on_delete=models.CASCADE)
    firma_digital = models.BooleanField(default=False, verbose_name='Confirmar de recibido')

    def __str__(self):
        return '{}: {}'.format(self.dispositivo, str(self.dispositivo.identificador) + str(self.triage))




# CONTROL DE MAQUINARIA

class Empresa(models.Model):
    empresa = models.CharField(max_length=150, null=True, blank=True)
    contacto = models.CharField(max_length=150, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    celular = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return '{}: {}'.format(self.empresa, self.contacto)

class Maquina(models.Model):
    tipo = models.CharField(max_length=150, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.tipo)

class MaquinaPerfil(ControlCreaciones):
    maquina = models.ForeignKey(Maquina, related_name='relMaquinaPerfilMaquina', on_delete=models.CASCADE)
    servicio_programado = models.DateField(default=datetime.datetime.now, null=True, blank=True, verbose_name='Servicio Programado')
    encargado = models.ForeignKey(User, related_name='relMaquinaPerfilEncargado', on_delete=models.CASCADE, null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return '{}'.format(self.maquina)

class MaquinaProblema(models.Model):
    problema = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.problema)

class MaquinaHistorico(ControlCreaciones):
    maquina = models.ForeignKey(MaquinaPerfil, related_name='relMaquinaHistoricoMaquinaPerfil', on_delete=models.CASCADE, null=True, blank=True)
    empresa = models.ForeignKey(Empresa, related_name='relMaquinaHistoricoEmpresa', on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.datetime.now, null=True, blank=True)
    trabajo_realizado = models.ForeignKey(MaquinaProblema, related_name='relMaquinaHistoricoEmpresa', on_delete=models.CASCADE)
    costo = models.DecimalField(max_digits=6, decimal_places=2, null = True, blank = True, default=Decimal('0.00'))
    descripcion = models.TextField(null=True, blank=True)
    recomendaciones = models.TextField(null=True, blank=True)
    tecnico_supervisor = models.ForeignKey(User, related_name='relMaquinaHistoricoTecnicoSupervisor', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{}: {}'.format(self.empresa, self.trabajo_realizado)