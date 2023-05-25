from django.db import models
from rol.models import Rol
from curso.models import Curso
from persona.models import Persona

# Create your models here.

class Persxcurso(models.Model):
    idPersonaXcurso = models.AutoField(primary_key=True, auto_created=True)
    Persona_idPersona= models.ForeignKey(Persona, on_delete=models.CASCADE)
    Persona_Rol_idRol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    Curso_idCurso= models.ForeignKey(Curso, on_delete=models.CASCADE)
    estado = models.BooleanField(default=False,blank=False, null=False)
    archivo = models.FileField(blank=True, null=True, upload_to='uploads/')

    class Meta:
        verbose_name = "Persona por curso"
        verbose_name_plural = "Personas por cursos"

    def __str__(self):
        return f"{self.Persona_idPersona}. Curso: {self.Curso_idCurso}"  
