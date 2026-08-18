from rest_framework import serializers

from APLICACION_EMPRESA.models import ModeloMunicipio
from APLICACION_EMPRESA.serializers.common import SerializadorDepartamentoResumen

class SerializadorMunicipioResumen(serializers.ModelSerializer):

    Departamento = SerializadorDepartamentoResumen()

    class Meta:
    
        model = ModeloMunicipio

        fields = (
            "Id",
            "Nombre",
            "Codigo",
            "Departamento"
        )