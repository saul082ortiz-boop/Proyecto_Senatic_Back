from APLICACION_SEED.services.BaseSeed import BaseSeed

from APLICACION_EMPRESA.models import ModeloEmpresa
from APLICACION_SEED.services.factories import EmpresaFactory 

class SeedEmpresa(BaseSeed):

    Nombre = "EMPRESA"

    @classmethod
    def Crear(cls, Config):
        for _ in range(Config.CantidadEmpresas):
            Datos = EmpresaFactory.CrearDatos()
            ModeloEmpresa.objects.create(**Datos)