from rest_framework import serializers

from APLICACION_USUARIOS.models import ModeloUsuario, ModeloRol


class SerializadorCrearUsuario(serializers.ModelSerializer):

    Password = serializers.CharField(write_only=True)

    Roles = serializers.PrimaryKeyRelatedField(
        queryset=ModeloRol.objects.filter(Estado=True),
        many=True,
        write_only=True
    )

    class Meta:

        model = ModeloUsuario

        fields = (
            "Nombre",
            "Apellido",
            "Telefono",
            "Correo",
            "NumeroIdentificacion",
            "TipoIdentificacion",
            "Password",
            "Roles"
        )