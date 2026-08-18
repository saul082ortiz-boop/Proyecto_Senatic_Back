from rest_framework.routers import DefaultRouter

from APLICACION_EMPRESA.views.VistasDepartamento import (VistasDepartamento)

Router = DefaultRouter()

Router.register("Departamentos", VistasDepartamento, basename="Departamentos")

urlpatterns = Router.urls