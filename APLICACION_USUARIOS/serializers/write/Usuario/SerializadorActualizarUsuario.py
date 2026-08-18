from rest_framework import serializers

from APLICACION_USUARIOS.models import ModeloUsuario


class SerializadorActualizarUsuario(serializers.ModelSerializer):

    class Meta:

        model = ModeloUsuario

        fields = (
            "Nombre",
            "Apellido",
            "Telefono",
        )