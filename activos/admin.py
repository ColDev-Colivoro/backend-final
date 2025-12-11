from django.contrib import admin
from .models import Empresa, Equipo

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'rut', 'direccion', 'creado_en']
    search_fields = ['nombre', 'rut']
    list_filter = ['creado_en']
    date_hierarchy = 'creado_en'

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'numero_serie', 'empresa', 'es_critico', 'fecha_instalacion']
    list_filter = ['es_critico', 'empresa']
    search_fields = ['nombre', 'numero_serie']
    date_hierarchy = 'fecha_instalacion'
