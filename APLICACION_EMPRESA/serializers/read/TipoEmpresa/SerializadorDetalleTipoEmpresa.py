from rest_framework import serializers

from APLICACION_EMPRESA.models import ModeloTipoEmpresa
from APLICACION_EMPRESA.serializers.common import SerializadorEmpresaResumenServicio

class SerializadorDetalleTipoEmpresa(serializers.ModelSerializer):

    Empresas = SerializadorEmpresaResumenServicio(many=True, read_only=True)

    class Meta:

        model = ModeloTipoEmpresa

        fields = (
            "Id",
            "Nombre",
            "Empresas",
            "Estado",
            "FechaCreacion",
            "FechaActualizacion"
        )