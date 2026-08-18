from faker import Faker

from APLICACION_SEED.services import SeedUtils
from APLICACION_USUARIOS.models import ModeloTipoIdentificacion

Fake = Faker("es_CO")

class UsuarioFactory:
    PASSWORD = "123456789"

    @classmethod
    def Nombre(cls):
        return Fake.first_name()

    @classmethod
    def Apellido(cls):
        return Fake.last_name()

    @classmethod
    def Telefono(cls):
        return Fake.msisdn()[:10]

    @classmethod
    def NumeroDocumento(cls):
        return Fake.unique.numerify("##########")

    @classmethod
    def Correo(cls, Prefijo="usuario"):
        Numero = Fake.unique.random_int(1, 999999)
        # if Prefijo=="admin":
        #     return f"{Prefijo}@reservas.com"
        # else:
        return f"{Prefijo}{Numero}@reservas.com"

    @classmethod
    def CrearDatos(cls, Prefijo="usuario"):
        TIPO_IDENTIFICACION = SeedUtils.Aleatorio(ModeloTipoIdentificacion.objects.all())
        return {
            "Nombre": cls.Nombre(),
            "Apellido": cls.Apellido(),
            "Telefono": cls.Telefono(),
            "NumeroIdentificacion": cls.NumeroDocumento(),
            "TipoIdentificacion": TIPO_IDENTIFICACION.Id,
            "Correo": cls.Correo(Prefijo),
            "password": cls.PASSWORD,
        }