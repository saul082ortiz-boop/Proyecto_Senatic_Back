from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field

from APLICACION_USUARIOS.models import ModeloUsuario
from APLICACION_USUARIOS.serializers.common import SerializadorRolResumenUsuario, SerializadorTipoIdentificacionResumen


class SerializadorDetalleUsuarioPropio(serializers.ModelSerializer):

    @extend_schema_field(str)
    def get_NombreCompleto(self, obj):
        return f"{obj.Nombre} {obj.Apellido}"

    NombreCompleto = (serializers.SerializerMethodField())
    TipoIdentificacion = SerializadorTipoIdentificacionResumen()

    class Meta:

        model = ModeloUsuario

        fields = (
            "Id",
            "Nombre",
            "Apellido",
            "NombreCompleto",
            "Correo",
            "Telefono",
            "NumeroIdentificacion",
            "TipoIdentificacion",
            "Estado",
            "FechaCreacion",
            "FechaActualizacion"
        )