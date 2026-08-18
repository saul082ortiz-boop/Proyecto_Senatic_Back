from rest_framework.routers import DefaultRouter

from APLICACION_EMPRESA.views.VistasEmpresa import (VistasEmpresa)

Router = DefaultRouter()

Router.register("Empresas", VistasEmpresa, basename="Empresas")

urlpatterns = Router.urls