from django.contrib import admin
from .models import PlanMantencion, OrdenTrabajo

@admin.register(PlanMantencion)
class PlanMantencionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'equipo', 'frecuencia_dias', 'activo']
    list_filter = ['activo']
    search_fields = ['nombre', 'equipo__nombre']

@admin.register(OrdenTrabajo)
class OrdenTrabajoAdmin(admin.ModelAdmin):
    list_display = ['id', 'plan', 'equipo', 'tecnico', 'estado', 'fecha_programada', 'completado_en']
    list_filter = ['estado', 'fecha_programada']
    search_fields = ['plan__nombre', 'equipo__nombre', 'tecnico__nombre_completo']
    date_hierarchy = 'fecha_programada'
    readonly_fields = ['completado_en']
