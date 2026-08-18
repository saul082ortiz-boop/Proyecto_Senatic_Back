from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class SerializadorTokenPersonalizado(TokenObtainPairSerializer):

    username_field = "Correo"

    @classmethod
    def get_token(cls, Usuario):
        Token = super().get_token(Usuario)
        Token["Usuario_Id"] = Usuario.Id
        Token["Nombre"] = Usuario.Nombre
        Token["Nombre_Completo"] = f"{Usuario.Nombre} {Usuario.Apellido}"
        Token["Correo"] = Usuario.Correo
        Token["Roles"] = [
            RolUsuario.Rol.Nombre
            for RolUsuario in Usuario.RolesUsuario.all()
        ]
        return Token
    
    def validate(self, attrs):
        Datos = super().validate(attrs)
        Datos["Usuario"] = {
            "Id": self.user.Id,
            "Nombre": self.user.Nombre,
            "NombreCompleto": f"{self.user.Nombre} {self.user.Apellido}",
            "Correo": self.user.Correo,
            "Roles": [{"Id": RolUsuario.Rol.Id,"Nombre": RolUsuario.Rol.Nombre}for RolUsuario in self.user.RolesUsuario.all()]
        }
        return Datos