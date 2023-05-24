from django.db import models
from rol.models import Rol
from curso.models import Curso
from persona.models import Persona

# Create your models here.

class Persxcurso(models.Model):
    idPersonaXcurso = models.IntegerField(primary_key=True)
    Persona_idPersona= models.ForeignKey(Persona, on_delete=models.CASCADE)
    Persona_Rol_idRol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    Curso_idCurso= models.ForeignKey(Curso, on_delete=models.CASCADE)


    
    class Meta:
        verbose_name = "Persona por curso"
        verbose_name_plural = "Personas por cursos"

    # def __str__(self):
    #     return f"{self.nombre}  {self.apellido}"  
