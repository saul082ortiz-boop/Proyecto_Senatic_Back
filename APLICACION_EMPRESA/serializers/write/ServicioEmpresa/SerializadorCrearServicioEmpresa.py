from rest_framework import serializers

from APLICACION_EMPRESA.models import ModeloServicioEmpresa


class SerializadorCrearServicioEmpresa(serializers.ModelSerializer):

    class Meta:

        model = ModeloServicioEmpresa

        fields = (
            "Servicio",
            "Empresa"
        )

    def validate(self, attrs):

            Servicio = attrs["Servicio"]
            Empresa = attrs["Empresa"]

            if ModeloServicioEmpresa.objects.filter(Servicio=Servicio, Empresa=Empresa).exists():
                raise serializers.ValidationError("Esa Empresa ya tiene asignado ese Servicio.")

            return attrs