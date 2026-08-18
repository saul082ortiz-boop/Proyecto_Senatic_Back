from django.db import transaction
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404

from APLICACION_USUARIOS.models import ModeloUsuario, ModeloRolUsuario, ModeloRol


class ServicioUsuario:

    @staticmethod
    @transaction.atomic
    def CrearUsuario(data, Roles):
        """
        Crea usuario + asigna roles
        """
        Usuario = ModeloUsuario.objects.create(
            Nombre=data["Nombre"],
            Apellido=data["Apellido"],
            Correo=data["Correo"],
            Telefono=data["Telefono"],
            NumeroIdentificacion=data["NumeroIdentificacion"],
            TipoIdentificacion=data["TipoIdentificacion"],
            password=make_password(data["Password"])
        )
        ModeloRolUsuario.objects.bulk_create([ModeloRolUsuario(Usuario = Usuario, Rol = Rol)for Rol in Roles])
        return Usuario


    @staticmethod
    def ObtenerUsuarios():
        return ModeloUsuario.objects.all()
    
    @staticmethod
    def ObtenerUsuarioPorId(UsuarioId):
        return get_object_or_404(ModeloUsuario, Id=UsuarioId)
    
    @staticmethod
    @transaction.atomic
    def ActualizarUsuario(Usuario, data):
        Usuario.Nombre = data.get("Nombre", Usuario.Nombre)
        Usuario.Apellido = data.get("Apellido", Usuario.Apellido)
        Usuario.Telefono = data.get("Telefono", Usuario.Telefono)
        Usuario.save()
        return Usuario

    @staticmethod
    def EliminarUsuario(Usuario):
        Usuario.Estado = False
        Usuario.save()
        return Usuario

    @staticmethod
    def ActivarUsuario(Usuario):
        Usuario.Estado = True
        Usuario.save()
        return Usuario