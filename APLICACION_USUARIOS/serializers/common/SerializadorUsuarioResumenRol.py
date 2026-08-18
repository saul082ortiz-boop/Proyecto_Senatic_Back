from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field

from APLICACION_USUARIOS.models import ModeloUsuario

class SerializadorUsuarioResumenRol(serializers.ModelSerializer):

    @extend_schema_field(str)
    def get_NombreCompleto(self, obj):
        return f"{obj.Nombre} {obj.Apellido}"

    NombreCompleto = serializers.SerializerMethodField()
    TipoIdentificacion = serializers.CharField(source="TipoIdentificacion.Abreviatura")

    class Meta:

        model = ModeloUsuario

        fields = (
            "Id",
            "NombreCompleto",
            "NumeroIdentificacion",
            "TipoIdentificacion"
        )