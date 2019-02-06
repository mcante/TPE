from django.contrib import admin

from .models import Perfil, Area, TipoEquipo, EquipoCargado, AsignarEquipo, Telefono

# Register your models here.


admin.site.register(Perfil)
admin.site.register(Area)
admin.site.register(EquipoCargado)
admin.site.register(TipoEquipo)
admin.site.register(AsignarEquipo)
admin.site.register(Telefono)