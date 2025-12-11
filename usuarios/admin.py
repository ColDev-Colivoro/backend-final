from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Tecnico

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    """Admin personalizado para modelo Usuario"""
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    search_fields = ['username', 'email', 'first_name', 'last_name']

@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ['nombre_completo', 'especialidad', 'telefono', 'usuario']
    list_filter = ['especialidad']
    search_fields = ['nombre_completo', 'telefono']
