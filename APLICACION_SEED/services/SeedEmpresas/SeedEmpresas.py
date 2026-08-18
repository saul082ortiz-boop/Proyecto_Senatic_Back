from APLICACION_SEED.services import SeedLogger
from APLICACION_SEED.services.BaseSeed import BaseSeed

from .SeedEmpresa import SeedEmpresa
from .SeedServiciosEmpresa import SeedServiciosEmpresa


class SeedEmpresas:

    @classmethod
    def Ejecutar(cls, Config):
        SeedLogger.Grupo("EMPRESAS")
        SeedEmpresa.Ejecutar(Config)
        SeedServiciosEmpresa.Ejecutar(Config)