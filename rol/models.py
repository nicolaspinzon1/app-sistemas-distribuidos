from django.db import models

class Rol(models.Model):
    idRol = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=16, blank=False, null=False)
    descripcion = models.CharField(max_length=64,  blank=True, null=True)
    
    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

    def __str__(self):
        return f"{self.nombre}  "  