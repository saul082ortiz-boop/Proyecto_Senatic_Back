from rest_framework.routers import DefaultRouter
from APLICACION_USUARIOS.views.VistasAuth import VistasAuth

Router = DefaultRouter()

Router.register("Auth", VistasAuth, basename="Auth")

urlpatterns = Router.urls