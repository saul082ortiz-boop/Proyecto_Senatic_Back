from rest_framework import serializers


class SerializadorRestablecerContrasena(serializers.Serializer):

    Token = serializers.CharField()
    ContrasenaNueva = serializers.CharField(write_only=True)
    ContrasenaConfirmacion = serializers.CharField(write_only=True)

    def validate(self, attrs):

        if attrs["ContrasenaNueva"] != attrs["ContrasenaConfirmacion"]:
            raise serializers.ValidationError("Las contraseñas no coinciden.")

        return attrs