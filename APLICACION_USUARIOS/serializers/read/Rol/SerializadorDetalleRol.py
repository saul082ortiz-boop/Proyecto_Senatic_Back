from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field

from APLICACION_USUARIOS.models import ModeloRol
from APLICACION_USUARIOS.serializers.common import SerializadorUsuarioResumenRol

class SerializadorDetalleRol(serializers.ModelSerializer):

    @extend_schema_field(SerializadorUsuarioResumenRol(many=True))
    def get_Usuarios(self, obj):
        return [SerializadorUsuarioResumenRol(UsuarioRol.Usuario).data for UsuarioRol in obj.UsuariosRol.all()]

    Usuarios = serializers.SerializerMethodField()
    class Meta:

        model = ModeloRol

        fields = (
            "Id",
            "Nombre",
            "Usuarios",
            "Estado",
            "FechaCreacion",
            "FechaActualizacion"
        )