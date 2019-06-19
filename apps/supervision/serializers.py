from rest_framework import serializers
from .models import Movimiento, TipoMovimiento, User




class TipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoMovimiento
        fields = ['tipo']

class UsuariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']



class MovimientoSerializer(serializers.ModelSerializer):
    tipo = serializers.StringRelatedField()
    entrega = serializers.StringRelatedField(source='entrega.get_full_name')
    recibe = serializers.StringRelatedField(source='recibe.get_full_name')
    supervisado_por = serializers.StringRelatedField(source='supervisado_por.get_full_name')
    supervision_completada = serializers.SerializerMethodField()

    class Meta:
        model = Movimiento
        fields = ('movimiento', 'tipo', 'dispositivo', 'cantidad', 'fecha', 'entrega', 'recibe', 'kardex', 'supervisado_por', 'supervision_completada')

    def get_supervision_completada(sel, object):
        if object.supervision_completada:
            return "Si"
        else:
            return "No"





class MovimientoInformeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movimiento
        fields = ['movimiento', 'tipo', 'dispositivo', 'cantidad', 'fecha', 'entrega', 'recibe', 'kardex', 'supervisado_por', 'supervision_completada']