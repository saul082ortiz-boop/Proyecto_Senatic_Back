from rest_framework import serializers

from APLICACION_USUARIOS.models import ModeloRolUsuario
from APLICACION_USUARIOS.serializers.common import SerializadorSimpleRol, SerializadorSimpleUsuario

class SerializadorDetalleRolUsuario(serializers.ModelSerializer):

    Rol = SerializadorSimpleRol()
    Usuario = SerializadorSimpleUsuario()

    class Meta:

        model = ModeloRolUsuario

        fields = (
            "Id",
            "Rol",
            "Usuario",
            "Estado",
            "FechaCreacion",
            "FechaActualizacion"
        )