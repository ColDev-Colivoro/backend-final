from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Empresa, Equipo
from .serializers import EmpresaSerializer, EquipoSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'rut']
    ordering_fields = ['nombre', 'creado_en']

class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.select_related('empresa')
    serializer_class = EquipoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['empresa', 'es_critico']
    search_fields = ['nombre', 'numero_serie']
