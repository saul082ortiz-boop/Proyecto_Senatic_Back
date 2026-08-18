from rest_framework.routers import DefaultRouter

from APLICACION_USUARIOS.views.VistasUsuario import (VistasUsuario)

Router = DefaultRouter()

Router.register("Usuarios", VistasUsuario, basename="Usuarios")

urlpatterns = Router.urls