from django.contrib import admin

from .models import Area, Indicador, Calificacion, AsignacionIndicadores, VersionIndicador

# Register your models here.


admin.site.register(Area)
admin.site.register(Indicador)
admin.site.register(Calificacion)
admin.site.register(AsignacionIndicadores)
admin.site.register(VersionIndicador)