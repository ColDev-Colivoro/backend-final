from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import PlanMantencion, OrdenTrabajo
from .serializers import PlanMantencionSerializer, OrdenTrabajoSerializer

class PlanMantencionViewSet(viewsets.ModelViewSet):
    queryset = PlanMantencion.objects.select_related('equipo')
    serializer_class = PlanMantencionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['equipo', 'activo']

class OrdenTrabajoViewSet(viewsets.ModelViewSet):
    queryset = OrdenTrabajo.objects.select_related('plan', 'equipo', 'tecnico')
    serializer_class = OrdenTrabajoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['estado', 'tecnico', 'equipo']
    ordering_fields = ['fecha_programada', 'estado']

    def perform_create(self, serializer):
        serializer.save()
