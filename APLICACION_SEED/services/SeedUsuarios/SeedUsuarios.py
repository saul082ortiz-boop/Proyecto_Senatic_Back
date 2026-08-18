from APLICACION_SEED.services import SeedLogger
from APLICACION_SEED.services.BaseSeed import BaseSeed

from .SeedUsuario import SeedUsuario
from .SeedRolUsuario import SeedRolUsuario


class SeedUsuarios:

    @classmethod
    def Ejecutar(cls, Config):
        SeedLogger.Grupo("USUARIOS")
        SeedUsuario.Ejecutar(Config)
        SeedRolUsuario.Ejecutar(Config)