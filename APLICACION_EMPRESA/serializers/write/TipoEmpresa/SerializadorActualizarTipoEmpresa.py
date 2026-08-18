from rest_framework import serializers

from APLICACION_EMPRESA.models import ModeloTipoEmpresa

class SerializadorActualizarTipoEmpresa(serializers.ModelSerializer):

    class Meta:
        model = ModeloTipoEmpresa

        fields = (
            "Nombre",
        )