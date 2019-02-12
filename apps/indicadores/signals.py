from django.db.models import signals
from django.dispatch import receiver

from apps.evaluaciones.models import Evaluacion
from .models import AsignacionIndicadores, Indicador





""" Señal que escucha cada vez que se crea una evaluación:
    Dependiendo de la versión elegida, así mismo se crea un grupo de
    instancias correspondientes a indicadores.
"""
@receiver(signals.post_save, sender=Evaluacion) 
def generar_version(sender, instance, **kwargs):

    if kwargs.get('created', False):
        print ("Se ha creado una evaluación.")
        version = Evaluacion.objects.get(pk=instance.pk).version.pk
        print ("Version de valuacion: " +  str(version))

        if(version is 1):
                print("Evaluacion Tecnica Mensual")
                AsignacionIndicadores.objects.create(evaluacion=instance, indicador=Indicador.objects.get(pk=1))
                AsignacionIndicadores.objects.create(evaluacion=instance, indicador=Indicador.objects.get(pk=2))
                AsignacionIndicadores.objects.create(evaluacion=instance, indicador=Indicador.objects.get(pk=3))
                AsignacionIndicadores.objects.create(evaluacion=instance, indicador=Indicador.objects.get(pk=4))
                AsignacionIndicadores.objects.create(evaluacion=instance, indicador=Indicador.objects.get(pk=5))
                AsignacionIndicadores.objects.create(evaluacion=instance, indicador=Indicador.objects.get(pk=6))
                AsignacionIndicadores.objects.create(evaluacion=instance, indicador=Indicador.objects.get(pk=7))
                AsignacionIndicadores.objects.create(evaluacion=instance, indicador=Indicador.objects.get(pk=9))
                AsignacionIndicadores.objects.create(evaluacion=instance, indicador=Indicador.objects.get(pk=11))
                AsignacionIndicadores.objects.create(evaluacion=instance, indicador=Indicador.objects.get(pk=17))
                AsignacionIndicadores.objects.create(evaluacion=instance, indicador=Indicador.objects.get(pk=12))
                AsignacionIndicadores.objects.create(evaluacion=instance, indicador=Indicador.objects.get(pk=18))
                AsignacionIndicadores.objects.create(evaluacion=instance, indicador=Indicador.objects.get(pk=19))
                AsignacionIndicadores.objects.create(evaluacion=instance, indicador=Indicador.objects.get(pk=23))
                AsignacionIndicadores.objects.create(evaluacion=instance, indicador=Indicador.objects.get(pk=26))
                print("Se han creado los indicadores correctamente.")