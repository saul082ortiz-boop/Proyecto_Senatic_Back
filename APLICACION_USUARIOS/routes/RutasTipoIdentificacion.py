from rest_framework.routers import DefaultRouter

from APLICACION_USUARIOS.views.VistasTipoIdentificacion import (VistasTipoIdentificacion)

Router = DefaultRouter()

Router.register("TipoIdentificacion", VistasTipoIdentificacion, basename="TipoIdentificacion")

urlpatterns = Router.urls