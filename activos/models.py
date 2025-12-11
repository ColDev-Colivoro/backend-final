from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=255, db_index=True, verbose_name="Nombre Empresa")
    direccion = models.TextField(verbose_name="Dirección")
    rut = models.CharField(max_length=20, verbose_name="RUT")
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        ordering = ['-creado_en']

    def __str__(self):
        return f"{self.nombre} ({self.rut})"

class Equipo(models.Model):
    empresa = models.ForeignKey(
        Empresa, 
        on_delete=models.CASCADE, 
        related_name='equipos',
        verbose_name="Empresa Propietaria"
    )
    nombre = models.CharField(max_length=255, verbose_name="Nombre del Equipo")
    numero_serie = models.CharField(
        max_length=100, 
        unique=True, 
        verbose_name="Número de Serie"
    )
    es_critico = models.BooleanField(default=False, verbose_name="¿Es Crítico?")
    fecha_instalacion = models.DateField(verbose_name="Fecha de Instalación")

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        indexes = [
            models.Index(fields=['empresa', 'nombre']),
        ]

    def __str__(self):
        return f"{self.nombre} (S/N: {self.numero_serie})"
