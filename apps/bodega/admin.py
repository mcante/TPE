from django.contrib import admin

from .models import Tarima, HistoricoTarima, Pasillo, Nivel, Sector, EstadoTarima, \
    DispositivosTriage, TiposEntrada, InventarioEntrada, ControlTriage, ControlTriageReimpresos, RegistrarTriage, DespachoTriage, \
    Empresa, Maquina, MaquinaPerfil, MaquinaProblema, MaquinaHistorico

# Register your models here.

# CONTROL DE TARIMAS
admin.site.register(Tarima)
admin.site.register(HistoricoTarima)
admin.site.register(Pasillo)
admin.site.register(Nivel)
admin.site.register(Sector)
admin.site.register(EstadoTarima)


# CONTROL DE TRIAGE
admin.site.register(DispositivosTriage)
admin.site.register(TiposEntrada)
admin.site.register(InventarioEntrada)
admin.site.register(ControlTriage)
admin.site.register(ControlTriageReimpresos)
admin.site.register(RegistrarTriage)
admin.site.register(DespachoTriage)


admin.site.register(Empresa)
admin.site.register(Maquina)
admin.site.register(MaquinaPerfil)
admin.site.register(MaquinaProblema)
admin.site.register(MaquinaHistorico)

