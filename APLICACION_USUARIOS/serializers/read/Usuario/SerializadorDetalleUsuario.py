from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field

from APLICACION_EMPRESA.serializers.common import SerializadorEmpresaResumen
from APLICACION_USUARIOS.models import ModeloUsuario
from APLICACION_USUARIOS.serializers.common import SerializadorRolResumenUsuario, SerializadorTipoIdentificacionResumen


class SerializadorDetalleUsuario(serializers.ModelSerializer):

    @extend_schema_field(str)
    def get_NombreCompleto(self, obj):
        return f"{obj.Nombre} {obj.Apellido}"

    @extend_schema_field(SerializadorRolResumenUsuario(many=True))
    def get_Roles(self, obj):
        return [SerializadorRolResumenUsuario(RolUsuario.Rol).data for RolUsuario in obj.RolesUsuario.all()]

    NombreCompleto = (serializers.SerializerMethodField())
    TipoIdentificacion = SerializadorTipoIdentificacionResumen()
    Roles = serializers.SerializerMethodField()
    Empresas = SerializadorEmpresaResumen(many=True, read_only=True)
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
            "Roles",
            "Estado",
            "FechaCreacion",
            "FechaActualizacion",
            "Empresas"
        )