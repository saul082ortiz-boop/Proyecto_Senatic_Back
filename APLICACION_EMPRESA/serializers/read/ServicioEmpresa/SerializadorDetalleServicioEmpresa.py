from rest_framework import serializers

from APLICACION_EMPRESA.models import ModeloServicioEmpresa
from APLICACION_EMPRESA.serializers.common import SerializadorServicioResumen, SerializadorEmpresaResumen

class SerializadorDetalleServicioEmpresa(serializers.ModelSerializer):

    Servicio = SerializadorServicioResumen()
    Empresa = SerializadorEmpresaResumen()

    class Meta:

        model = ModeloServicioEmpresa

        fields = (
            "Id",
            "Servicio",
            "Empresa",
            "Estado",
            "FechaCreacion",
            "FechaActualizacion"
        )