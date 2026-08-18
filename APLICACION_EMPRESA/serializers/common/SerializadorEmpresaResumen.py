from rest_framework import serializers

from APLICACION_EMPRESA.models import ModeloEmpresa
from APLICACION_EMPRESA.serializers.common import SerializadorMunicipioResumen

class SerializadorEmpresaResumen(serializers.ModelSerializer):

    class Meta:
    
        Municipio = SerializadorMunicipioResumen()

        model = ModeloEmpresa

        fields = (
            "Id",
            "Nit",
            "RazonSocial",
            "Logo",
            "Municipio"
        )