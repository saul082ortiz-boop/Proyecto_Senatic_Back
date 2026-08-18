from APLICACION_SEED.services import SeedLogger
from APLICACION_SEED.services.BaseSeed import BaseSeed

from .SeedRoles import SeedRoles
from .SeedTiposIdentificacion import SeedTiposIdentificacion
from .SeedTiposEmpresa import SeedTiposEmpresa
from .SeedServicios import SeedServicios



class SeedCatalogos:

    @classmethod
    def Ejecutar(cls, Config):
        SeedLogger.Grupo("CATÁLOGOS")
        SeedRoles.Ejecutar(Config)
        SeedTiposIdentificacion.Ejecutar(Config)
        SeedTiposEmpresa.Ejecutar(Config)
        SeedServicios.Ejecutar(Config)