import django_filters
from django_filters import rest_framework as filters
from .models import Tarima, HistoricoTarima, Pasillo



class HistoricoFilter(filters.FilterSet):

    fecha_min = django_filters.DateFilter(field_name='fecha_min', method='filter_fecha')
    fecha_max = django_filters.DateFilter(field_name='fecha_max', method='filter_fecha')

    class Meta:
        model = HistoricoTarima
        fields = ['tarima', 'fecha', 'sector', 'contenido', 'estado', 'editado_por']
    
    def filter_fecha(self, queryset, field_name, value):
        if value and field_name == 'fecha_min':
            queryset = queryset.filter(fecha__gte=value)
        if value and field_name == 'fecha_max':
            queryset = queryset.filter(fecha__lte=value)
        return queryset
    

class PasilloFilter(filters.FilterSet):
    class Meta:
        model = Pasillo
        fields = ['id']