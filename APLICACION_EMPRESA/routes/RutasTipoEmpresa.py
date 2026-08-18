from rest_framework.routers import DefaultRouter

from APLICACION_EMPRESA.views.VistasTipoEmpresa import (VistasTipoEmpresa)

Router = DefaultRouter()

Router.register("TiposEmpresas", VistasTipoEmpresa, basename="TiposEmpresas")

urlpatterns = Router.urls