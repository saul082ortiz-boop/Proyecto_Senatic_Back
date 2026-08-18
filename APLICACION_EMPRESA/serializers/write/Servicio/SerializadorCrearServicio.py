from rest_framework import serializers

from APLICACION_EMPRESA.models import ModeloServicio

class SerializadorCrearServicio(serializers.ModelSerializer):

    class Meta:
        model = ModeloServicio

        fields = (
            "Nombre",
        )