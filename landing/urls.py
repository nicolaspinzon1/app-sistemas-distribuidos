from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home),
    path("logout/", view=views.signout),
]
