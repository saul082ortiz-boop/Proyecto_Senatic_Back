from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from APLICACION_USUARIOS.models import ModeloUsuario
from APLICACION_USUARIOS.permissions import EsAdministradorEmpresa, EsSuperAdministrador, EsUsuario, PermisosPersonalizados
from APLICACION_USUARIOS.serializers.common import SerializadorVacio
from APLICACION_USUARIOS.services.ServicioUsuario import ServicioUsuario
from APLICACION_USUARIOS.serializers.read.Usuario import SerializadorDetalleUsuarioPropio, SerializadorListaUsuario, SerializadorDetalleUsuario
from APLICACION_USUARIOS.serializers.write.Usuario import SerializadorCrearUsuario, SerializadorActualizarUsuario

class VistasUsuario(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
    ):

    permission_classes=[IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "list":
            return SerializadorListaUsuario
        if self.action == "retrieve":
            return SerializadorDetalleUsuario
        if self.action == "create":
            return SerializadorCrearUsuario
        if self.action == "update":
            return SerializadorActualizarUsuario
        return SerializadorVacio

    def get_permissions(self):
        if self.action in ["list", "retrieve", "create", "update", "destroy"]:
            permission_classes = [EsSuperAdministrador]
        elif self.action == "Activar":
            permission_classes = [EsSuperAdministrador]
        elif self.action == "Obtener":
            permission_classes = [IsAuthenticated, PermisosPersonalizados]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    queryset = ModeloUsuario.objects.all()

    # ===========================================
    # LISTAR (GET /usuario/)
    # ===========================================
    def list(self, request):
        Usuarios = ServicioUsuario.ObtenerUsuarios()
        Serializador = SerializadorListaUsuario(Usuarios, many=True)
        return Response(Serializador.data, status=status.HTTP_200_OK)

    # ===========================================
    # OBTENER (GET /usuario/{id}/)
    # ===========================================
    def retrieve(self, request, pk=None):
        Usuario = ServicioUsuario.ObtenerUsuarioPorId(pk)
        Serializador = SerializadorDetalleUsuario(Usuario)
        return Response(Serializador.data, status=status.HTTP_200_OK)

    # ===========================================
    # CREAR (POST /usuario/)
    # ===========================================
    def create(self, request):
        Serializador = SerializadorCrearUsuario(data=request.data)
        Serializador.is_valid(raise_exception=True)
        Roles = Serializador.validated_data.pop("Roles")
        Usuario = ServicioUsuario.CrearUsuario(Serializador.validated_data, Roles)
        SerializadorRespuesta = SerializadorDetalleUsuario(Usuario)
        return Response(SerializadorRespuesta.data, status=status.HTTP_201_CREATED)

    # ===========================================
    # ACTUALIZAR COMPLETO (PUT /usuario/{id}/)
    # ===========================================
    def update(self, request, pk=None):
        Usuario = ServicioUsuario.ObtenerUsuarioPorId(pk)
        Serializador = SerializadorActualizarUsuario(Usuario, data=request.data)
        Serializador.is_valid(raise_exception=True)
        Usuario = ServicioUsuario.ActualizarUsuario(Usuario,Serializador.validated_data)
        return Response(SerializadorDetalleUsuario(Usuario).data, status=status.HTTP_200_OK)

    # ===========================================
    # ACTIVAR (PATCH /usuario/{id}/)
    # ===========================================
    @extend_schema(request=None, responses={200: None})
    @action(detail=True, methods=["patch"], permission_classes = [EsSuperAdministrador])
    def Activar(self, request, pk=None):
        Usuario = ServicioUsuario.ObtenerUsuarioPorId(pk)
        ServicioUsuario.ActivarUsuario(Usuario)
        return Response({"Mensaje": "Usuario"}, status=status.HTTP_200_OK)

    # ===========================================
    # ELIMINAR (DELETE /usuario/{id}/)
    # ===========================================
    @extend_schema(request=None, responses={200: None})
    def destroy(self, request, pk=None):
        Usuario = ServicioUsuario.ObtenerUsuarioPorId(pk)
        ServicioUsuario.EliminarUsuario(Usuario)
        return Response({"Mensaje": "Usuario Eliminado"}, status=status.HTTP_200_OK)
    
    # ===========================================
    # OBTENER (GET /usuario/{id}/)
    # ===========================================
    @action(detail=True, methods=["get"], serializer_class=SerializadorDetalleUsuarioPropio)
    def Obtener(self, request, pk=None):
        Usuario = ServicioUsuario.ObtenerUsuarioPorId(pk)
        self.check_object_permissions(request, Usuario)
        Serializador = SerializadorDetalleUsuarioPropio(Usuario)
        return Response(Serializador.data, status=status.HTTP_200_OK)
    