from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from usuarios.views import UsuarioViewSet, TecnicoViewSet
from activos.views import EmpresaViewSet, EquipoViewSet
from operaciones.views import PlanMantencionViewSet, OrdenTrabajoViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'tecnicos', TecnicoViewSet)
router.register(r'empresas', EmpresaViewSet)
router.register(r'equipos', EquipoViewSet)
router.register(r'planes-mantencion', PlanMantencionViewSet)
router.register(r'ordenes-trabajo', OrdenTrabajoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    
    # Auth
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
