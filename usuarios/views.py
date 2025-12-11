from rest_framework import viewsets, permissions
from .models import Usuario, Tecnico
from .serializers import UsuarioSerializer, TecnicoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAdminUser]

class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]
