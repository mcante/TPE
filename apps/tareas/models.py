from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone #Agregada por mi para el manejo de la fecha
from decimal import Decimal
# from datetime import datetime
import datetime
# from datetime import datetime

import pytz

from django.dispatch import receiver
from django.db.models.signals import post_save


# Modelo Abstracto para poder ser heredado
class ControlCreaciones(models.Model):
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        abstract = True





# PROGRAMACIONES MENSUALES

class Meses(models.Model):
    mes = models.CharField(max_length=25, null=True, blank=True)
    
    def __str__(self):
        return '{}'.format(self.mes)


class Programaciones(ControlCreaciones):
    fecha = models.DateField(default=timezone.now, null=True, blank=True)
    mes = models.ForeignKey(Meses, related_name='rel_ProgramacionesSupervisor_Meses', on_delete=models.CASCADE, null=True, blank=True)
    supervisor = models.ForeignKey(User, related_name='rel_ProgramacionesSupervisor_User', on_delete=models.CASCADE, null=True, blank=True)
    tecnico = models.ForeignKey(User, related_name='rel_ProgramacionesTecnicos_User', on_delete=models.CASCADE, null=True, blank=True)
    cerrado = models.BooleanField(default=False)

    def __str__(self):
        return '{}: {}'.format(self.mes, self.tecnico)

class Estados(models.Model):
    estado = models.CharField(max_length=25, null=True, blank=True)
    ponderacion = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    
    def __str__(self):
        return '{}'.format(self.estado)

class Tareas(ControlCreaciones):
    programacion = models.ForeignKey(Programaciones, related_name='rel_Tareas_Programaciones', on_delete=models.CASCADE, null=True, blank=True)
    tarea = models.TextField(null=True, blank=True)
    fecha_hora_inicio = models.DateTimeField(default=datetime.datetime.now(), null=True, blank=True)
    fecha_hora_planificada = models.DateTimeField(default=datetime.datetime.now(), null=True, blank=True)
    anotaciones = models.TextField(max_length=250, null=True, blank=True)
    estado = models.ForeignKey(Estados, related_name='rel_Tareas_Estados', on_delete=models.CASCADE, null=True, blank=True)
    completado = models.BooleanField(default=False)
    fecha_hora_completado = models.DateTimeField(null=True, blank=True)
    creado_por = models.ForeignKey(User, related_name='rel_Tareas_User', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return '{}'.format(self.tarea)   

    # Calcular el tiempo transcurrido entre lo Ahora y el momento en que fue creado
    def get_tiempotranscurrido(self):
        ahora = datetime.datetime.now() + datetime.timedelta(hours=6) # Sumar 6 hrs a la hora actual para ajustarla a la zona horaria de GT
        creada = self.fecha_hora_inicio.replace(tzinfo=None) # No especificar la zona horaria para el campo guardado
        diferencia = (ahora - creada) # calcular la diferencia.

        print("***********Transcurrido***********")
        dias = diferencia.days # Extraer los días
        horas = diferencia.seconds//3600 # Extraer las horas
        minutos = diferencia.seconds%3600/60 # Extraer los minutos
        
        return ("Días: " + str(dias) + ", Tiempo: " + str(horas) + ":" + str("{0:.0f}".format(minutos))) # Con {0:.0f} formatear para no mostrar decimales
    



    # Calcular el tiempo restante entre lo Planificado y el Final
    def get_tiemporestante(self):
        if (self.fecha_hora_completado):

                
            planificada = self.fecha_hora_planificada.replace(tzinfo=None) # No especificar la zona horaria para el campo guardado
            finalizado = self.fecha_hora_completado.replace(tzinfo=None) # Sumar 6 hrs a la hora actual para ajustarla a la zona horaria de GT
            

            print("***********Restante***********" + str(finalizado))
            print("***********Restante***********" + str(planificada))

            diferencia = finalizado - planificada # calcular la diferencia.

            print(diferencia)
            if (finalizado > planificada):
                print("Atrasado")
                dias = diferencia.days # Extraer los días
                horas = diferencia.seconds//3600 # Extraer las horas
                minutos = diferencia.seconds%3600/60 # Extraer los minutos

                return ("Días: " + str(dias) + ", Tiempo: " + str(horas) + ":" + str("{0:.0f}".format(minutos))) # Con {0:.0f} formatear para no mostrar decimales
            else:
                return "Completado a tiempo"

            
        else:
            return "Aún no ha sido completado"
        
    


    # Retorna la fecha planificada en forma de cadena.
    def get_fechaPlanificada(self):
        
        planificada = self.fecha_hora_planificada.replace(tzinfo=None) # No especificar la zona horaria para el campo guardado
        planificada = planificada - datetime.timedelta(hours=6)
        
        anio = planificada.year
        mes = planificada.month -1 #Quitar un mes porque en javascript los meses van de 0 para enero y 11 para diciembre
        dia = planificada.day
        hora = planificada.hour
        minuto = planificada.minute
        # retorno = "2019, 12, 31, 23, 60"
        retorno = str(anio) + "," + str(mes) + "," + str(dia) + "," + str(hora) + "," + str(minuto) + ",01"
        print("***** Planificada: " + str(retorno))
        return retorno

        # Retorna la fecha actual en forma de cadena.
    def get_fechaActual(self):
        
        ahora = datetime.datetime.now() + datetime.timedelta(hours=6) # Sumar 6 hrs a la hora actual para ajustarla a la zona horaria de GT
        
        anio = ahora.year
        mes = ahora.month
        dia = ahora.day
        hora = ahora.hour
        minuto = ahora.minute
        # retorno = "2019, 12, 31, 23, 60"
        retorno = str(anio) + "," + str(mes) + "," + str(dia) + "," + str(hora) + "," + str(minuto) + ",01"
        print("***** Actual: " + str(retorno))
        return retorno
        

# Signal para crear insertar la fecha si se marca como completado.
@receiver(post_save, sender=Tareas)
def insertar_fecha(sender, instance, **kwargs):
    if kwargs.get('updated', True):
        if (instance.estado.id == 3 or instance.estado.id == 4):
            Tareas.objects.filter(pk=instance.id).update(fecha_hora_completado=datetime.datetime.now())
        else:
            Tareas.objects.filter(pk=instance.id).update(fecha_hora_completado=None)


            

class AnotacionesTarea(ControlCreaciones):
    tarea = models.ForeignKey(Tareas, related_name='rel_AnotacionesTarea_Tareas', on_delete=models.CASCADE, null=True, blank=True)
    apunte = models.TextField(max_length=250, null=True, blank=True)
    fecha_hora_anotacion = models.DateTimeField(default=datetime.datetime.now(), null=True, blank=True)
    

    