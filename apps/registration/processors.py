from django.db.models import Q
from apps.apuntes.models import Nota
from apps.indicadores.models import AsignacionIndicadores
from apps.tareas.models import Programaciones, Tareas


# Procesador de contexto.
def alarma(request):
    if request.user.is_authenticated: # Validar si hay usuario autenticado para hacer las consultas y evitar generar errores, sino hay entonces que retorne una lista vacía.
        notas_seguimiento = Nota.objects.filter(creado_por=request.user.id, necesita_seguimiento=True).order_by('id').reverse()  # Obtener todas las notas que necesitan seguimiento según el usuario logueado
        mejoras_seguimiento = AsignacionIndicadores.objects.filter(evaluacion__empleado = request.user, debe_mejorar=True).order_by('id').reverse() # Obtener todos los indicadores en los cuáles los empleados deben mejorar, según el empleado logueado
        tareas_porhacer = Tareas.objects.filter(Q(estado = 1) | Q(estado = 2), creado_por = request.user, programacion__cerrado = False)
        ALARMAS = {'Notas':notas_seguimiento, 'Mejoras':mejoras_seguimiento, 'PorHacer':tareas_porhacer} # Generar una lista de cada consulta y devolverlas para ser utilizadas en cualquier template.
    else:
        return {}
    return ALARMAS