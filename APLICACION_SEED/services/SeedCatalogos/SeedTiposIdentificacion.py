from APLICACION_SEED.services.BaseSeed import BaseSeed
from APLICACION_USUARIOS.models import ModeloTipoIdentificacion


class SeedTiposIdentificacion(BaseSeed):

    Nombre = "TIPOS_IDENTIFICACION"

    DATOS = [
        ("Cédula de Ciudadanía", "CC"),
        ("Tarjeta de Identidad", "TI"),
        ("Cédula de Extranjería", "CE"),
        ("Pasaporte", "PAS")
    ]

    @classmethod
    def Crear(cls, Config):
        for Nombre, Abreviatura in cls.DATOS:
            cls.CrearSiNoExiste(ModeloTipoIdentificacion, Nombre=Nombre, Abreviatura=Abreviatura)