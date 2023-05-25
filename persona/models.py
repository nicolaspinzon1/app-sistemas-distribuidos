from django.db import models
from rol.models import Rol



class Persona(models.Model):
    idPersona = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=32, blank=False, null=False)
    apellido = models.CharField(max_length=32,  blank=True, null=True)
    cedula = models.IntegerField()
    telefono =models.IntegerField()
    Rol_idRol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    
    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return f"{self.nombre}  {self.apellido}"  