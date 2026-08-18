from rest_framework.routers import DefaultRouter

from APLICACION_EMPRESA.views.VistasEmpresa import VistasEmpresa
from APLICACION_EMPRESA.views.VistasServicioEmpresa import VistasServicioEmpresa
from APLICACION_EMPRESA.views.VistasTipoEmpresa import VistasTipoEmpresa

from .views.VistasServicio import VistasServicio
from .views.VistasDepartamento import VistasDepartamento
from .views.VistasMunicipio import VistasMunicipio

Router = DefaultRouter()

Router.register("Departamento", VistasDepartamento, basename="Departamento")
Router.register("Municipio", VistasMunicipio, basename="Municipio")
Router.register("Servicio", VistasServicio, basename="Servicio")
Router.register("TipoEmpresa", VistasTipoEmpresa, basename="TipoEmpresa")
Router.register("ServicioEmpresa", VistasServicioEmpresa, basename="ServicioEmpresa")
Router.register("Empresa", VistasEmpresa, basename="Empresa")

urlpatterns = Router.urls