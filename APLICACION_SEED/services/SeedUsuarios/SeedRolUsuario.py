from APLICACION_SEED.services.BaseSeed import BaseSeed

from APLICACION_USUARIOS.models import ModeloRol, ModeloRolUsuario, ModeloUsuario


class SeedRolUsuario(BaseSeed):

    Nombre = "ROLES USUARIO"

    @classmethod
    def Crear(cls, Config):
    
        RolSuperAdmin = ModeloRol.objects.get(Nombre="SUPER ADMIN")
        RolAdministradorEmpresa = ModeloRol.objects.get(Nombre="ADMINISTRADOR EMPRESA")
        RolUsuario = ModeloRol.objects.get(Nombre="USUARIO")

        # SUPER ADMIN
        SuperAdmins = ModeloUsuario.objects.filter(Correo__startswith="admin")
        for SuperAdmin in SuperAdmins:
            cls.CrearSiNoExiste(ModeloRolUsuario, Usuario=SuperAdmin, Rol=RolSuperAdmin)
            cls.CrearSiNoExiste(ModeloRolUsuario, Usuario=SuperAdmin, Rol=RolAdministradorEmpresa)

        # ADMINISTRADORES
        Administradores = ModeloUsuario.objects.filter(Correo__startswith="adminempresa")
        for Administrador in Administradores:
            cls.CrearSiNoExiste(ModeloRolUsuario, Usuario=Administrador, Rol=RolAdministradorEmpresa)

        # USUARIOS
        Usuarios = ModeloUsuario.objects.all()
        for Usuario in Usuarios:
            cls.CrearSiNoExiste(ModeloRolUsuario, Usuario=Usuario, Rol=RolUsuario)