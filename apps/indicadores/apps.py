from django.apps import AppConfig


class IndicadoresConfig(AppConfig):
    name = 'apps.indicadores'
    verbose_name = 'Indicadores'

    def ready(self):
        from . import signals
