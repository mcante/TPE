from django.db.models import signals
from django.dispatch import receiver

from apps.evaluaciones.models import Evaluacion
from .models import AsignacionIndicadores, Indicador, VersionIndicador





""" Señal que escucha cada vez que se crea una evaluación:
    Dependiendo de la versión elegida, así mismo se crea un grupo de
    instancias correspondientes a indicadores.
"""
@receiver(signals.post_save, sender=Evaluacion) 
def generar_version(sender, instance, **kwargs):

    if kwargs.get('created', False):
        print ("Se ha creado una evaluación.")
        versionId = Evaluacion.objects.get(pk=instance.pk).version.pk
        print ("Version de valuacion: " +  str(versionId))

        detalle = VersionIndicador.objects.filter(version=versionId)
        
        for x in detalle:
                AsignacionIndicadores.objects.create(evaluacion=instance, indicador=Indicador.objects.get(pk=x.indicador.id))
