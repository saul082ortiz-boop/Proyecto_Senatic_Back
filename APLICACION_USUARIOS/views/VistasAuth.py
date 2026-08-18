from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework_simplejwt.tokens import RefreshToken

from APLICACION_USUARIOS.serializers.auth.SerializadorTokenPersonalizado import SerializadorTokenPersonalizado
from APLICACION_USUARIOS.serializers.auth.SerializadorIniciarSesion import SerializadorIniciarSesion
from APLICACION_USUARIOS.serializers.auth.SerializadorCerrarSesion import SerializadorCerrarSesion

@extend_schema_view(
    login=extend_schema(tags=["Autenticación"], description="Iniciar sesión"),
    refresh=extend_schema(tags=["Autenticación"], description="Renovar Access Token"),
    logout=extend_schema(tags=["Autenticación"], description="Cerrar sesión"),
)
class VistasAuth(ViewSet):

    @extend_schema(request=SerializadorIniciarSesion, responses=SerializadorTokenPersonalizado)
    @action(detail=False, methods=["post"])
    def login(self, request):
        Serializador = SerializadorTokenPersonalizado(data=request.data)
        Serializador.is_valid(raise_exception=True)
        return Response(Serializador.validated_data, status=status.HTTP_200_OK)

    @extend_schema(request=TokenRefreshSerializer, responses=TokenRefreshSerializer)
    @action(detail=False, methods=["post"])
    def refresh(self, request):
        Serializador = TokenRefreshSerializer(data=request.data)
        Serializador.is_valid(raise_exception=True)
        return Response(Serializador.validated_data)
    
    @extend_schema(request=SerializadorCerrarSesion, responses={200: dict})
    @action(detail=False, methods=["post"])
    def logout(self, request):
        refresh_token = request.data["refresh"]
        if not refresh_token:
            return Response({"error": "El refresh token es requerido"}, status=status.HTTP_400_BAD_REQUEST)
        Token = RefreshToken(refresh_token)
        Token.blacklist()
        return Response({"mensaje": "Sesión cerrada correctamente"})