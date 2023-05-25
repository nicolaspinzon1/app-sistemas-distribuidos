from django.shortcuts import render
from django.contrib.auth.decorators import login_required  
from persona.models import Persona, Rol
from personxcurso.models import Persxcurso
from . import views

@login_required
def mis_cursos(request):
    user = request.user
    persona = Persona.objects.get(cedula = user.get_username())
    cursos = Persxcurso.objects.filter(Persona_idPersona = persona.idPersona)
    search = Search()
    
    if request.method == "POST":
            option = request.POST.get("filtro")
            if option == '1':
                cursos = Persxcurso.objects.filter(Persona_idPersona = persona.idPersona)
            elif option == '2':                
           
                cursos = search.searchCourse(cursos, 'True')
            elif option == '3':
                cursos = search.searchCourse(cursos, 'False')

    context = {'listado_cursos': cursos, 'persona': persona}
    
    return render(request, "cursos.html", context=context)


class CourseFinder:

    def __init__(self) -> None:
        pass
    
    def filterCourses(self, coursesList, state):
        return coursesList.filter(estado = state)



class Search():
    def __init__(self) -> None:
        self.courseFinder = CourseFinder()

    def searchCourse(self, coursesList, state):
        return self.courseFinder.filterCourses(coursesList, state)




# @login_required
# def (request):
#     tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
#     return render(request, 'tasks.html', {"tasks": tasks})

# @login_required
# def curso_copleted(request):
#     tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
#     return render(request, 'tasks.html', {"tasks": tasks})
