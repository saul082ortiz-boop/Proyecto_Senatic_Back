from rest_framework import serializers

from APLICACION_EMPRESA.models import ModeloTipoEmpresa

class SerializadorListaTipoEmpresa(serializers.ModelSerializer):

    class Meta:

        model = ModeloTipoEmpresa

        fields = (
            "Id",
            "Nombre",
            "Estado"
        )