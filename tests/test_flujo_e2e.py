from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from activos.models import Empresa, Equipo
from operaciones.models import PlanMantencion, OrdenTrabajo

User = get_user_model()

class FlujoCompletoTests(APITestCase):
    def setUp(self):
        # 1. Crear Usuario Admin para autenticarse
        self.user = User.objects.create_superuser(
            username='testadmin', 
            email='admin@test.com', 
            password='testpassword123'
        )
        # 2. Obtener Token JWT
        url_login = reverse('token_obtain_pair')
        data = {'username': 'testadmin', 'password': 'testpassword123'}
        response = self.client.post(url_login, data, format='json')
        self.item_access_token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.item_access_token}')

    def test_flujo_de_vida_mantenimiento(self):
        """
        Simula el ciclo completo:
        1. Crear Empresa
        2. Registrar Equipo
        3. Crear Plan de Mantención
        4. Verificar que todo se guardó
        """
        print("\n>>> INICIANDO TEST DE FLUJO COMPLETO (E2E) <<<")

        # PASO 1: Crear Empresa
        url_empresa = '/api/empresas/'  # Usamos rutas explicitas para verificar configuración
        data_empresa = {
            'nombre': 'Industrias Biobío S.A.',
            'direccion': 'Parque Industrial 2020',
            'rut': '76.888.999-K'
        }
        res_empresa = self.client.post(url_empresa, data_empresa, format='json')
        self.assertEqual(res_empresa.status_code, status.HTTP_201_CREATED)
        empresa_id = res_empresa.data['id']
        print(f"✅ Empresa creada: ID {empresa_id}")

        # PASO 2: Crear Equipo
        url_equipo = '/api/equipos/'
        data_equipo = {
            'empresa': empresa_id,
            'nombre': 'Generador Eléctrico 5000W',
            'numero_serie': 'GEN-5000-X1',
            'es_critico': True,
            'fecha_instalacion': '2023-01-15'
        }
        res_equipo = self.client.post(url_equipo, data_equipo, format='json')
        self.assertEqual(res_equipo.status_code, status.HTTP_201_CREATED)
        equipo_id = res_equipo.data['id']
        print(f"✅ Equipo registrado: ID {equipo_id}")

        # PASO 3: Crear Plan de Mantención
        url_plan = '/api/planes-mantencion/'
        data_plan = {
            'equipo': equipo_id,
            'nombre': 'Mantención Mensual Preventiva',
            'frecuencia_dias': 30
        }
        res_plan = self.client.post(url_plan, data_plan, format='json')
        self.assertEqual(res_plan.status_code, status.HTTP_201_CREATED)
        print(f"✅ Plan de mantención configurado: {res_plan.data['nombre']}")

        # VERIFICACIÓN FINAL
        self.assertEqual(Empresa.objects.count(), 1)
        self.assertEqual(Equipo.objects.count(), 1)
        self.assertEqual(PlanMantencion.objects.count(), 1)
        print(">>> TEST COMPLETADO CON ÉXITO: Todos los datos han sido ingresados correctamente. <<<")
