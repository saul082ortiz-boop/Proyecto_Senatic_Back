from rest_framework.routers import DefaultRouter

from APLICACION_EMPRESA.views.VistasServicioEmpresa import (VistasServicioEmpresa)

Router = DefaultRouter()

Router.register("ServicioEmpresa", VistasServicioEmpresa, basename="ServicioEmpresa")

urlpatterns = Router.urls