from rest_framework.routers import DefaultRouter

from APLICACION_USUARIOS.views.VistasRol import (VistasRol)

Router = DefaultRouter()

Router.register("Rol", VistasRol, basename="Rol")

urlpatterns = Router.urls