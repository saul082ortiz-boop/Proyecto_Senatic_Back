import random

from APLICACION_SEED.services.BaseSeed import BaseSeed

from APLICACION_EMPRESA.models import ModeloEmpresa, ModeloServicioEmpresa

from ..SeedUtils import SeedUtils

class SeedServiciosEmpresa(BaseSeed):

    Nombre = "SERVICIOS EMPRESA"

    @classmethod
    def Crear(cls, Config):

        Empresas = ModeloEmpresa.objects.all()

        for Empresa in Empresas:
            Servicios = SeedUtils.ServiciosPorTipoEmpresa(Empresa.TipoEmpresa)
            for Servicio in Servicios:
                cls.CrearSiNoExiste(ModeloServicioEmpresa, Empresa=Empresa, Servicio=Servicio)