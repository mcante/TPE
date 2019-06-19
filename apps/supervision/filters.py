import django_filters
from django_filters import rest_framework as filters
from .models import Movimiento



""" Lo siguiente iría antes de Meta.
    id = django_filters.NumberFilter(field_name="id")
    movimiento = django_filters.NumberFilter(field_name="movimiento")
    tipo = django_filters.CharFilter(field_name='tipo')
""" 

class MovimientoFilter(filters.FilterSet):

    id = django_filters.NumberFilter(field_name="id")
    movimiento = django_filters.NumberFilter(field_name="movimiento")
    tipo = django_filters.CharFilter(field_name='tipo')
    fecha_min = django_filters.DateFilter(field_name='fecha_min', method='filter_fecha')
    fecha_max = django_filters.DateFilter(field_name='fecha_max', method='filter_fecha')

    class Meta:
        model = Movimiento
        fields = ['movimiento', 'tipo', 'fecha']
    
    def filter_fecha(self, queryset, field_name, value):
        if value and field_name == 'fecha_min':
            queryset = queryset.filter(fecha__gte=value)
        if value and field_name == 'fecha_max':
            queryset = queryset.filter(fecha__lte=value)
        return queryset
