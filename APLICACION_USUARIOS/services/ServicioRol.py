from APLICACION_USUARIOS.models import ModeloRol

class ServicioRol:

    @staticmethod
    def ObtenerRoles():
        return ModeloRol.objects.all()

    @staticmethod
    def ObtenerRolPorId(RolId):
        return ModeloRol.objects.get(Id=RolId)

    @staticmethod
    def CrearRol(data):
        return ModeloRol.objects.create(**data)

    @staticmethod
    def ActualizarRol(Rol, data):
        Rol.Nombre = data.get("Nombre", Rol.Nombre)
        Rol.save()
        return Rol
    
    @staticmethod
    def EliminarRol(Rol):
        Rol.Estado = False
        Rol.save()
        return Rol
    
    @staticmethod
    def ActivarRol(Rol):
        Rol.Estado = True
        Rol.save()
        return Rol