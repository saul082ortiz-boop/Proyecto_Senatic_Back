from rest_framework import serializers

from APLICACION_EMPRESA.models import ModeloDepartamento

class SerializadorDepartamentoResumen(serializers.ModelSerializer):

    class Meta:
    
        model = ModeloDepartamento

        fields = (
            "Id",
            "Nombre",
            "Codigo",
        )