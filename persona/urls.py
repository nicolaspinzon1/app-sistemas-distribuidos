from django.urls import path
from . import views

urlpatterns = [
    path("MiPerfil/", views.perfil),
]
