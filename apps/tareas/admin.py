from django.contrib import admin

from .models import Meses, AnotacionesTarea, Tareas, Programaciones, Estados
# Register your models here.

admin.site.register(Programaciones)
admin.site.register(Meses)
admin.site.register(AnotacionesTarea)
admin.site.register(Tareas)
admin.site.register(Estados)