from django.contrib import admin

from .models import TipoMovimiento, Movimiento

# Register your models here.


admin.site.register(TipoMovimiento)
admin.site.register(Movimiento)