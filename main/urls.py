from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("autenticacion.urls")),
    path("cursos/",include("curso.urls")),
    path("", include("landing.urls"))
]

    