from django.contrib import admin

from .models import TipoMovimiento, Movimiento, Entrada, DetalleDepuracion

# Register your models here.


admin.site.register(TipoMovimiento)
admin.site.register(Movimiento)
admin.site.register(Entrada)
admin.site.register(DetalleDepuracion)