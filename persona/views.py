from django.shortcuts import render
from persona.models import Persona

def perfil(request):
    user = request.user
    persona = Persona.objects.get(cedula = user.get_username())
    context = {'persona': persona}
    
    return render(request, "perlfil.html", context=context)