from APLICACION_EMPRESA.models import ModeloTipoEmpresa
from APLICACION_SEED.services.BaseSeed import BaseSeed


class SeedTiposEmpresa(BaseSeed):

    Nombre = "TIPOS_EMPRESA"

    DATOS = [
        "RESTAURANTE",
        "BARBERÍA",
        "HOSPITAL",
        "COLEGIO",
        "TALLER",
    ]

    @classmethod
    def Crear(cls, Config):
        for Nombre in cls.DATOS:
            cls.CrearSiNoExiste(ModeloTipoEmpresa, Nombre=Nombre)