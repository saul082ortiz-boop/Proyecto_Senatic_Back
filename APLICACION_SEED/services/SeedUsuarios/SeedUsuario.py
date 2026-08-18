from APLICACION_SEED.services.BaseSeed import BaseSeed

from APLICACION_SEED.services.factories import UsuarioFactory
from APLICACION_USUARIOS.models import ModeloUsuario, ModeloTipoIdentificacion

class SeedUsuario(BaseSeed):

    Nombre = "USUARIO"

    @classmethod
    def Crear(cls, Config):
        for _ in range(Config.CantidadUsuarios):
            Datos = UsuarioFactory.CrearDatos()
            ModeloUsuario.objects.create_user(**Datos)

        for _ in range(Config.CantidadAdministradoresEmpresa):
            Datos = UsuarioFactory.CrearDatos(Prefijo="adminempresa")
            ModeloUsuario.objects.create_user(**Datos)

        for _ in range(Config.CantidadSuperAdmin):
            Datos = UsuarioFactory.CrearDatos(Prefijo="admin")
            ModeloUsuario.objects.create_user(**Datos)