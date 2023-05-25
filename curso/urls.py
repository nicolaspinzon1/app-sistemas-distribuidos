from django.urls import path
from . import views

urlpatterns = [
    path("mis-cursos/", views.mis_cursos),
]
