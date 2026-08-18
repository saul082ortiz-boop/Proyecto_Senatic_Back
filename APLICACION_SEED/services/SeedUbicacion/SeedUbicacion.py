from APLICACION_SEED.services import SeedLogger
from APLICACION_SEED.services.BaseSeed import BaseSeed

from .SeedDepartamentos import SeedDepartamentos
from .SeedMunicipios import SeedMunicipios


class SeedUbicacion:

    @classmethod
    def Ejecutar(cls, Config):
        SeedLogger.Grupo("UBICACIÓN")
        SeedDepartamentos.Ejecutar(Config)
        SeedMunicipios.Ejecutar(Config)