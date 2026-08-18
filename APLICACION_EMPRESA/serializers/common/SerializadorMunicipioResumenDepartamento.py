from rest_framework import serializers

from APLICACION_EMPRESA.models import ModeloMunicipio

class SerializadorMunicipioResumenDepartamento(serializers.ModelSerializer):

    class Meta:
    
        model = ModeloMunicipio

        fields = (
            "Id",
            "Nombre",
            "Codigo",
        )