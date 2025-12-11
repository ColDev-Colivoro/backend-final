from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    """
    Punto de entrada principal de la API con navegación a todos los endpoints.
    """
    return Response({
        '🔐 Autenticación': {
            'login_session': reverse('api-auth-login', request=request, format=format),
            'login_jwt': reverse('token_obtain_pair', request=request, format=format),
            'refresh_jwt': reverse('token_refresh', request=request, format=format),
        },
        '🏢 Gestión de Activos': {
            'empresas': reverse('empresa-list', request=request, format=format),
            'equipos': reverse('equipo-list', request=request, format=format),
        },
        '👥 Gestión de Personal': {
            'usuarios': reverse('usuario-list', request=request, format=format),
            'tecnicos': reverse('tecnico-list', request=request, format=format),
        },
        '⚙️ Operaciones': {
            'planes_mantencion': reverse('planmantencion-list', request=request, format=format),
            'ordenes_trabajo': reverse('ordentrabajo-list', request=request, format=format),
        },
        '📚 Documentación': {
            'swagger': request.build_absolute_uri('/api/schema/swagger-ui/'),
            'redoc': request.build_absolute_uri('/api/schema/redoc/'),
        }
    })
