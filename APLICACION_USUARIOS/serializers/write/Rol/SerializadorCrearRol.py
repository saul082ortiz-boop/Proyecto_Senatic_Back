from rest_framework import serializers

from APLICACION_USUARIOS.models import ModeloRol

class SerializadorCrearRol(serializers.ModelSerializer):

    class Meta:
        model = ModeloRol

        fields = (
            "Nombre",
        )