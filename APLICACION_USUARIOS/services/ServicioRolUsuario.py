from django.db import transaction

from APLICACION_USUARIOS.models import ModeloRolUsuario

class ServicioRolUsuario:

    @staticmethod
    def ObtenerRolesUsuarios():
        return ModeloRolUsuario.objects.all()

    @staticmethod
    def ObtenerRolUsuarioPorId(RolUsuarioId):
        return ModeloRolUsuario.objects.get(Id=RolUsuarioId)

    @staticmethod
    def ObtenerRolesPorUsuario(Usuario):
        return ModeloRolUsuario.objects.filter(Usuario=Usuario)


    @staticmethod
    def ObtenerUsuariosPorRol(Rol):
        return ModeloRolUsuario.objects.filter(Rol=Rol)

    @staticmethod
    @transaction.atomic
    def AsignarRoles(Usuario, Roles):
        ModeloRolUsuario.objects.filter(Usuario=Usuario).delete()
        ModeloRolUsuario.objects.bulk_create([ModeloRolUsuario(Usuario=Usuario, Rol=Rol)for Rol in Roles])
        return Usuario

    @staticmethod
    def RemoverRoles(Usuario, Roles):
        ModeloRolUsuario.objects.filter(Usuario=Usuario, Rol__in=Roles).delete()