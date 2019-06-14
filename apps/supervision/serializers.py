from rest_framework import serializers
from .models import Movimiento


class MovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento
        fields = ['movimiento', 'tipo', 'dispositivo', 'cantidad', 'fecha', 'entrega', 'recibe', 'kardex', 'supervisado_por', 'supervision_completada']