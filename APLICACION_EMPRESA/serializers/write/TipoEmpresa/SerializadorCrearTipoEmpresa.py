from rest_framework import serializers

from APLICACION_EMPRESA.models import ModeloTipoEmpresa

class SerializadorCrearTipoEmpresa(serializers.ModelSerializer):

    class Meta:
        model = ModeloTipoEmpresa

        fields = (
            "Nombre",
        )