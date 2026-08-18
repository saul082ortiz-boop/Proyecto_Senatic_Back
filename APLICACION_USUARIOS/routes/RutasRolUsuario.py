from rest_framework.routers import DefaultRouter

from APLICACION_USUARIOS.views.VistasRolUsuario import (VistasRolUsuario)

Router = DefaultRouter()

Router.register("RolUsuario", VistasRolUsuario, basename="RolUsuario")

urlpatterns = Router.urls