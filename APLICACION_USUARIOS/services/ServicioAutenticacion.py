from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password, make_password
from APLICACION_USUARIOS.models import ModeloUsuario

class ServicioAutenticacion:

    @staticmethod
    def IniciarSesion(Correo, Contrasena):
        Usuario = ModeloUsuario.objects.filter(Correo=Correo).first()
        if not Usuario:
            return None
        if not Usuario.check_password(Contrasena):
            return None
        return Usuario
    
    @staticmethod
    def CambiarContrasena(Usuario, ContrasenaActual, ContrasenaNueva):
        if not Usuario.check_password(ContrasenaActual):
            raise Exception("La Contraseña actual es incorrecta")
        Usuario.password = make_password(ContrasenaNueva)
        Usuario.save()
        return Usuario
    
    @staticmethod
    def RestablecerContrasena(Usuario, ContrasenaNueva):
        Usuario.password = make_password(ContrasenaNueva)
        Usuario.save()
        return Usuario