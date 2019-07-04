from rest_framework import serializers
from .models import HistoricoTarima, Pasillo, Tarima


class TarimaHistoricoSerializer(serializers.ModelSerializer):
    tarima = serializers.StringRelatedField()
    sector = serializers.StringRelatedField()
    estado = serializers.StringRelatedField()
    editado_por = serializers.StringRelatedField(source='editado_por.get_full_name')
    
    class Meta:
        model = HistoricoTarima
        fields = ('id', 'tarima', 'fecha', 'sector', 'contenido', 'estado', 'editado_por')


class TarimaSerializer(serializers.ModelSerializer):
    sector = serializers.StringRelatedField()
    editado_por = serializers.StringRelatedField(source='editado_por.get_full_name')

    class Meta:
        model = Tarima
        fields = ('id', 'sector', 'contenido', 'editado_por')


class PasilloSerializer(serializers.ModelSerializer):
    #tarimas = serializers.StringRelatedField(many=True)
    tarimas = TarimaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Pasillo
        #fields = '__all__'
        fields = ('id', 'tarimas')


class TarimaRestSerializer(serializers.ModelSerializer):
    sector = serializers.StringRelatedField()
    estado = serializers.StringRelatedField()

    class Meta:
        model = Tarima
        fields = ('id', 'sector', 'contenido', 'estado')