from APLICACION_SEED.services.BaseSeed import BaseSeed
from APLICACION_USUARIOS.models import ModeloRol


class SeedRoles(BaseSeed):

    Nombre = "ROLES"

    DATOS = [
        "SUPER ADMIN", 
        "ADMINISTRADOR EMPRESA", 
        "USUARIO"
    ]

    @classmethod
    def Crear(cls, Config):
        for Nombre in cls.DATOS:
            cls.CrearSiNoExiste(ModeloRol, Nombre=Nombre)
