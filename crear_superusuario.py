"""
Script de inicialización para crear el superusuario del sistema.
Ejecutar: python crear_superusuario.py
"""
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_mantencion.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Credenciales predefinidas
USERNAME = 'admin'
EMAIL = 'admin@mantencion.local'
PASSWORD = 'admin123'

def crear_superusuario():
    """Crea el superusuario si no existe."""
    if User.objects.filter(username=USERNAME).exists():
        print(f"✅ El superusuario '{USERNAME}' ya existe.")
        print(f"   Credenciales: {USERNAME} / {PASSWORD}")
    else:
        User.objects.create_superuser(
            username=USERNAME,
            email=EMAIL,
            password=PASSWORD
        )
        print(f"✅ Superusuario creado exitosamente!")
        print(f"   Usuario: {USERNAME}")
        print(f"   Contraseña: {PASSWORD}")
        print(f"   Email: {EMAIL}")

if __name__ == '__main__':
    crear_superusuario()
