from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from APLICACION_USUARIOS.models import ModeloRol
from APLICACION_USUARIOS.permissions import EsSuperAdministrador
from APLICACION_USUARIOS.serializers.common import SerializadorVacio
from APLICACION_USUARIOS.services.ServicioRol import ServicioRol
from APLICACION_USUARIOS.serializers.read.Rol import SerializadorListaRol, SerializadorDetalleRol
from APLICACION_USUARIOS.serializers.write.Rol import SerializadorCrearRol, SerializadorActualizarRol

class VistasRol(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
    ):

    permission_classes = [EsSuperAdministrador]

    def get_serializer_class(self):
        if self.action == "list":
            return SerializadorListaRol
        if self.action == "retrieve":
            return SerializadorDetalleRol
        if self.action == "create":
            return SerializadorCrearRol
        if self.action == "update":
            return SerializadorActualizarRol
        return SerializadorVacio

    queryset = ModeloRol.objects.all()

    # ===========================================
    # LISTAR (GET /Rol/)
    # ===========================================
    def list(self, request):
        Roles = ServicioRol.ObtenerRoles()
        Serializador = SerializadorListaRol(Roles, many=True)
        return Response(Serializador.data, status=status.HTTP_200_OK)
    
    # ===========================================
    # OBTENER (GET /Rol/{id}/)
    # ===========================================
    def retrieve(self, request, pk=None):
        Rol = ServicioRol.ObtenerRolPorId(pk)
        Serializador = SerializadorDetalleRol(Rol)
        return Response(Serializador.data, status=status.HTTP_200_OK)
    
    # ===========================================
    # CREAR (POST /Rol/)
    # ===========================================
    def create(self, request):
        Serializador = SerializadorCrearRol(data=request.data)
        Serializador.is_valid(raise_exception=True)
        Rol = ServicioRol.CrearRol(Serializador.validated_data)
        SerializadorRespuesta = SerializadorDetalleRol(Rol)
        return Response(SerializadorRespuesta.data, status=status.HTTP_201_CREATED)

    # ===========================================
    # ACTUALIZAR COMPLETO (PUT /Rol/{id}/)
    # ===========================================
    def update(self, request, pk=None):
        Rol = ServicioRol.ObtenerRolPorId(pk)
        Serializador = SerializadorActualizarRol(Rol, data=request.data)
        Serializador.is_valid(raise_exception=True)
        Rol = ServicioRol.ActualizarRol(Rol,Serializador.validated_data)
        return Response(SerializadorDetalleRol(Rol).data, status=status.HTTP_200_OK)

    # ===========================================
    # ACTIVAR (PATCH /Rol/{id}/)
    # ===========================================
    @extend_schema(request=None, responses={200: None})
    @action(detail=True, methods=["patch"])
    def Activar(self, request, pk=None):
        Rol = ServicioRol.ObtenerRolPorId(pk)
        ServicioRol.ActivarRol(Rol)
        return Response({"Mensaje": "Rol Activado"}, status=status.HTTP_200_OK)

    # ===========================================
    # ELIMINAR (DELETE /Rol/{id}/)
    # ===========================================
    @extend_schema(request=None, responses={200: None})
    def destroy(self, request, pk=None):
        Rol = ServicioRol.ObtenerRolPorId(pk)
        ServicioRol.EliminarRol(Rol)
        return Response({"Mensaje": "Rol Eliminado"}, status=status.HTTP_200_OK)
