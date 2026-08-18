from rest_framework import serializers

class SerializadorCerrarSesion(serializers.Serializer):
    refresh = serializers.CharField()