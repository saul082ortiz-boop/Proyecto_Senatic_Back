from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field

from APLICACION_USUARIOS.models import ModeloRolUsuario

class SerializadorListaRolUsuario(serializers.ModelSerializer):

    @extend_schema_field(str)
    def get_Usuario(self,obj):
            return (f"{obj.Usuario.Nombre} {obj.Usuario.Apellido}")

    Rol = serializers.CharField(source="Rol.Nombre")
    Usuario = serializers.SerializerMethodField()

    class Meta:

        model = ModeloRolUsuario

        fields = (
            "Id",
            "Rol",
            "Usuario"
        )