import os

from PIL import Image
from rest_framework import serializers
from drf_spectacular.utils import OpenApiTypes, extend_schema_field

from APLICACION_EMPRESA.models import ModeloEmpresa

class SerializadorLogoEmpresa(serializers.Serializer):

    Logo = serializers.ImageField(required=True)

    def validate_Logo(self, Imagen):
        Extension = os.path.splitext(Imagen.name)[1].lower()
        Img = Image.open(Imagen)
        Ancho, Alto = Img.size

        Permitidas = [
            ".jpg",
            ".jpeg",
            ".png",
            ".webp"
        ]

        if Extension not in Permitidas:
            raise serializers.ValidationError("Solo se permiten imágenes JPG, PNG o WEBP.")

        if Imagen.size > 2 * 1024 * 1024:
            raise serializers.ValidationError("El logo no puede superar los 2 MB.")

        if Ancho < 300 or Alto < 300:
            raise serializers.ValidationError("La imagen debe ser mínimo de 300x300 píxeles.")

        return Imagen
