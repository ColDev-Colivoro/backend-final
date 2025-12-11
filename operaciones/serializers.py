from rest_framework import serializers
from .models import PlanMantencion, OrdenTrabajo
from activos.serializers import EquipoSerializer
from usuarios.serializers import TecnicoSerializer

class PlanMantencionSerializer(serializers.ModelSerializer):
    equipo_nombre = serializers.ReadOnlyField(source='equipo.nombre')

    class Meta:
        model = PlanMantencion
        fields = ['id', 'equipo', 'equipo_nombre', 'nombre', 'frecuencia_dias', 'activo']

class OrdenTrabajoSerializer(serializers.ModelSerializer):
    equipo_detalle = EquipoSerializer(source='equipo', read_only=True)
    tecnico_detalle = TecnicoSerializer(source='tecnico', read_only=True)
    plan_nombre = serializers.ReadOnlyField(source='plan.nombre')
    esta_atrasada = serializers.SerializerMethodField()

    class Meta:
        model = OrdenTrabajo
        fields = [
            'id', 'plan', 'plan_nombre', 'equipo', 'equipo_detalle',
            'tecnico', 'tecnico_detalle', 'estado', 'fecha_programada',
            'completado_en', 'notas', 'esta_atrasada'
        ]

    def get_esta_atrasada(self, obj):
        from django.utils import timezone
        if obj.estado not in ['COMPLETADA', 'CANCELADA'] and obj.fecha_programada < timezone.now():
            return True
        return False
