from django.shortcuts import render

from persona.models import Persona, Rol
from personxcurso.models import Persxcurso

def mis_cursos(request):
    user = request.user
    persona = Persona.objects.get(cedula = user.get_username())
    cursos = Persxcurso.objects.filter(Persona_idPersona = persona.idPersona)
    context = {'listado_cursos': cursos, 'persona': persona}
    return render(request, "cursos.html", context=context)
