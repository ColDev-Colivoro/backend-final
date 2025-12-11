from rest_framework import serializers
from .models import Empresa, Equipo

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class EquipoSerializer(serializers.ModelSerializer):
    empresa_nombre = serializers.ReadOnlyField(source='empresa.nombre')

    class Meta:
        model = Equipo
        fields = ['id', 'empresa', 'empresa_nombre', 'nombre', 'numero_serie', 'es_critico', 'fecha_instalacion']
