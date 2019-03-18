from django.contrib import admin

from .models import Companias_telefonia, Estados, Eventos, Marcas, \
    Modelos, Pilotos, Rentadora, Ruta_Entregas, Rutas, Telefonos_Piloto, Telefonos_Rentadora, Vehiculos
# Register your models here.

admin.site.register(Companias_telefonia)
admin.site.register(Estados)
admin.site.register(Eventos)
admin.site.register(Marcas)
admin.site.register(Modelos)
admin.site.register(Pilotos)
admin.site.register(Rentadora)
admin.site.register(Ruta_Entregas)
admin.site.register(Rutas)
admin.site.register(Telefonos_Piloto)
admin.site.register(Telefonos_Rentadora)
admin.site.register(Vehiculos)
