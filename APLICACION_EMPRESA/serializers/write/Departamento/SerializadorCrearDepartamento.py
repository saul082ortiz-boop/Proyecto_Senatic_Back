from rest_framework import serializers

from APLICACION_EMPRESA.models import ModeloDepartamento

class SerializadorCrearDepartamento(serializers.ModelSerializer):

    class Meta:
        model = ModeloDepartamento

        fields = (
            "Nombre",
            "Codigo",
        )