from rest_framework import serializers

from APLICACION_USUARIOS.models import ModeloRolUsuario


class SerializadorCrearRolUsuario(serializers.ModelSerializer):

    class Meta:

        model = ModeloRolUsuario

        fields = (
            "Usuario",
            "Rol"
        )

    def validate(self, attrs):

            Usuario = attrs["Usuario"]
            Rol = attrs["Rol"]

            if ModeloRolUsuario.objects.filter(Usuario=Usuario, Rol=Rol).exists():
                raise serializers.ValidationError("El Usuario ya tiene asignado ese Rol.")

            return attrs