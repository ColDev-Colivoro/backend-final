from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return f"{self.username} ({self.get_full_name()})"

class Tecnico(models.Model):
    ESPECIALIDAD_CHOICES = [
        ('ELECTRICO', 'Eléctrico'),
        ('MECANICO', 'Mecánico'),
        ('SOFTWARE', 'Software'),
        ('OTRO', 'Otro'),
    ]

    usuario = models.OneToOneField(
        Usuario, 
        on_delete=models.CASCADE, 
        related_name='perfil_tecnico',
        verbose_name="Usuario de Sistema"
    )
    nombre_completo = models.CharField(max_length=255, verbose_name="Nombre Completo")
    especialidad = models.CharField(
        max_length=50, 
        choices=ESPECIALIDAD_CHOICES,
        default='OTRO',
        verbose_name="Especialidad"
    )
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")

    class Meta:
        verbose_name = "Técnico"
        verbose_name_plural = "Técnicos"

    def __str__(self):
        return f"{self.nombre_completo} - {self.get_especialidad_display()}"
