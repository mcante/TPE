from django.contrib import admin

from .models import Tarima, HistoricoTarima, Pasillo, Nivel, Sector, EstadoTarima
# Register your models here.

admin.site.register(Tarima)
admin.site.register(HistoricoTarima)
admin.site.register(Pasillo)
admin.site.register(Nivel)
admin.site.register(Sector)
admin.site.register(EstadoTarima)
