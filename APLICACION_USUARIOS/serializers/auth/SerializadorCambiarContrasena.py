from rest_framework import serializers


class SerializadorCambiarContrasena(serializers.Serializer):

    ContrasenaActual = serializers.CharField(write_only=True)
    ContrasenaNueva = serializers.CharField(write_only=True)
    ContrasenaConfirmacion = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs["ContrasenaNueva"] != attrs["ContrasenaConfirmacion"]:
            raise serializers.ValidationError("Las contraseñas no coinciden.")

        return attrs