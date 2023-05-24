from django.db import models

class Curso(models.Model):
    idCurso = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=64, blank=False, null=False)
    descripcion = models.CharField(max_length=20,  blank=True, null=True)
    duracion = models.DurationField()
    fechaInicio = models.DateTimeField(auto_now_add=True)
    fechaFinal = models.DateTimeField(null= True, blank=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return f"{self.nombre}  "  
