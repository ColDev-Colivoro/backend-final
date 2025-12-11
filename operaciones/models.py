from django.db import models
from django.utils import timezone
from activos.models import Equipo
from usuarios.models import Tecnico

class PlanMantencion(models.Model):
    equipo = models.ForeignKey(
        Equipo, 
        on_delete=models.CASCADE, 
        related_name='planes_mantencion',
        verbose_name="Equipo"
    )
    nombre = models.CharField(max_length=255, verbose_name="Nombre del Plan")
    frecuencia_dias = models.PositiveIntegerField(
        verbose_name="Frecuencia (Días)",
        help_text="Cada cuántos días se debe ejecutar este plan."
    )
    activo = models.BooleanField(default=True, verbose_name="¿Activo?")

    class Meta:
        verbose_name = "Plan de Mantención"
        verbose_name_plural = "Planes de Mantención"

    def __str__(self):
        return f"{self.nombre} - {self.equipo.nombre}"

class OrdenTrabajo(models.Model):
    ESTADO_CHOICES = [
        ('PROGRAMADA', 'Programada'),
        ('EN_PROGRESO', 'En Progreso'),
        ('COMPLETADA', 'Completada'),
        ('CANCELADA', 'Cancelada'),
    ]

    plan = models.ForeignKey(
        PlanMantencion, 
        on_delete=models.CASCADE, 
        related_name='ordenes',
        verbose_name="Plan Base"
    )
    equipo = models.ForeignKey(
        Equipo, 
        on_delete=models.CASCADE, 
        verbose_name="Equipo Objetivo"
    )
    tecnico = models.ForeignKey(
        Tecnico, 
        on_delete=models.PROTECT, 
        related_name='ordenes_asignadas',
        verbose_name="Técnico Asignado"
    )
    estado = models.CharField(
        max_length=20, 
        choices=ESTADO_CHOICES, 
        default='PROGRAMADA',
        verbose_name="Estado"
    )
    fecha_programada = models.DateTimeField(verbose_name="Fecha Programada")
    completado_en = models.DateTimeField(
        null=True, 
        blank=True, 
        verbose_name="Fecha Completado"
    )
    notas = models.TextField(blank=True, verbose_name="Notas/Observaciones")

    class Meta:
        verbose_name = "Orden de Trabajo"
        verbose_name_plural = "Órdenes de Trabajo"
        ordering = ['-fecha_programada']

    def __str__(self):
        return f"OT-{self.id} {self.plan.nombre} ({self.get_estado_display()})"

    def save(self, *args, **kwargs):
        if self.estado == 'COMPLETADA' and not self.completado_en:
            self.completado_en = timezone.now()
        super().save(*args, **kwargs)
