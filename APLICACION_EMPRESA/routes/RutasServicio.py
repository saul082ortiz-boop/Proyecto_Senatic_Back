from rest_framework.routers import DefaultRouter

from APLICACION_EMPRESA.views.VistasServicio import (VistasServicio)

Router = DefaultRouter()

Router.register("Servicios", VistasServicio, basename="Servicios")

urlpatterns = Router.urls