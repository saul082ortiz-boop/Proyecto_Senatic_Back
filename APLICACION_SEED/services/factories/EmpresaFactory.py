from faker import Faker

from APLICACION_EMPRESA.models import ModeloMunicipio, ModeloTipoEmpresa
from APLICACION_SEED.services import SeedUtils
from APLICACION_USUARIOS.models import ModeloUsuario

Fake = Faker("es_CO")

class EmpresaFactory:
    @classmethod
    def Nit(cls):
        return Fake.unique.numerify("#########")

    @classmethod
    def RazonSocial(cls):
        return Fake.company()

    @classmethod
    def Direccion(cls):
        return Fake.street_address()

    @classmethod
    def Barrio(cls):
        return Fake.city_suffix()

    @classmethod
    def Telefono(cls):
        return Fake.msisdn()[:10]

    @classmethod
    def Correo(cls):
        Numero = Fake.unique.random_int(1, 999999)
        return f"empresa{Numero}@reservas.com"

    @classmethod
    def CuposHora(cls):
        return Fake.random_int(3, 20)

    @classmethod
    def CrearDatos(cls):
        MUNICIPIO = SeedUtils.Aleatorio(ModeloMunicipio.objects.all())
        TIPO_EMPRESA = SeedUtils.Aleatorio(ModeloTipoEmpresa.objects.all())
        ADMINISTRADOR = SeedUtils.Aleatorio(ModeloUsuario.objects.filter(RolesUsuario__Rol__Nombre="ADMINISTRADOR EMPRESA").distinct())
        return {
            "Nit": cls.Nit(),
            "RazonSocial": cls.RazonSocial(),
            "Direccion": cls.Direccion(),
            "Municipio": MUNICIPIO,
            "Barrio": cls.Barrio(),
            "Telefono": cls.Telefono(),
            "Correo": cls.Correo(),
            "CuposHora": cls.CuposHora(),
            "TipoEmpresa": TIPO_EMPRESA,
            "Administrador": ADMINISTRADOR
        }