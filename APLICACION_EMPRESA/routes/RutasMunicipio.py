from rest_framework.routers import DefaultRouter

from APLICACION_EMPRESA.views.VistasMunicipio import (VistasMunicipio)

Router = DefaultRouter()

Router.register("Municipios", VistasMunicipio, basename="Municipios")

urlpatterns = Router.urls