from rest_framework import serializers

from APLICACION_EMPRESA.models import ModeloTipoEmpresa

class SerializadorTipoEmpresaResumen(serializers.ModelSerializer):

    class Meta:
    
        model = ModeloTipoEmpresa

        fields = (
            "Id",
            "Nombre"
        )