from rest_framework import serializers
from .models import Usuario, Tecnico

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff']

class TecnicoSerializer(serializers.ModelSerializer):
    usuario_detalle = UsuarioSerializer(source='usuario', read_only=True)
    
    class Meta:
        model = Tecnico
        fields = ['id', 'usuario', 'usuario_detalle', 'nombre_completo', 'especialidad', 'telefono']
