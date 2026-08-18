from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field

from APLICACION_EMPRESA.models import ModeloServicioEmpresa

class SerializadorListaServicioEmpresa(serializers.ModelSerializer):

    @extend_schema_field(str)
    def get_Empresa(self,obj):
            return (f"{obj.Empresa.Nit} {obj.Empresa.RazonSocial}")

    Servicio = serializers.CharField(source="Servicio.Nombre")
    Empresa = serializers.SerializerMethodField()

    class Meta:

        model = ModeloServicioEmpresa

        fields = (
            "Id",
            "Servicio",
            "Empresa"
        )