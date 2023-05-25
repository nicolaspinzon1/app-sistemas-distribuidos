from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate # crear la cookie 
from django.contrib.auth.decorators import login_required  
from django.db import IntegrityError
from django.contrib.auth.models import User
from persona.models import Persona, Rol
from personxcurso.models import Persxcurso


def sign_up(request):
    if request.method == 'GET':
        return render(requestº, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # register user
                user = User.objects.create_user(
                    username=request.POST['cedula'], password=request.POST
                    ['password1'])
                
                nombre = request.POST['nombre']
                apellido = request.POST['apellido']
                cedula = request.POST['cedula']
                telefono = request.POST['telefono']

                rol = Rol.objects.get(idRol = 1) 
                persona = Persona.objects.create(nombre = nombre, apellido = apellido, cedula = cedula, telefono = telefono, Rol_idRol = rol)

                persona.save()
                user.save() 

                login(request, user)
                return redirect('/cursos/mis-cursos/')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'User already exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Password do not match'
        })

def sign_in(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['cedula'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html',{
                'form': AuthenticationForm,
                'error': 'cedula o contraseña es incorrecta'
            })
        else:
            login(request, user)
            return redirect('/cursos/mis-cursos/')
@login_required
def signout(request):
    logout(request)
    return redirect(request, 'home.html')