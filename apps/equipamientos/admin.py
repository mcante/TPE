from django.contrib import admin

from .models import Equipamiento, Aspectos, Aspectos_Evaluados, Cambio_Equipo, Dispositivo, Inconvenientes, Producto_Lista, Productos, Productos_Entregados, Valoraciones
# Register your models here.

admin.site.register(Equipamiento)
admin.site.register(Aspectos)
admin.site.register(Aspectos_Evaluados)
admin.site.register(Cambio_Equipo)
admin.site.register(Dispositivo)
admin.site.register(Inconvenientes)
admin.site.register(Producto_Lista)
admin.site.register(Productos)
admin.site.register(Productos_Entregados)
admin.site.register(Valoraciones)