from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated

from APLICACION_EMPRESA.models import ModeloTipoEmpresa
from APLICACION_EMPRESA.serializers.read.TipoEmpresa import SerializadorDetalleTipoEmpresa, SerializadorListaTipoEmpresa
from APLICACION_EMPRESA.serializers.write.TipoEmpresa import SerializadorActualizarTipoEmpresa, SerializadorCrearTipoEmpresa
from APLICACION_EMPRESA.services import ServicioTipoEmpresa
from APLICACION_USUARIOS.serializers.common import SerializadorVacio

class VistasTipoEmpresa(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
    ):

    #permission_classes=[IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "list":
            return SerializadorListaTipoEmpresa
        if self.action == "retrieve":
            return SerializadorDetalleTipoEmpresa
        if self.action == "create":
            return SerializadorCrearTipoEmpresa
        if self.action == "update":
            return SerializadorActualizarTipoEmpresa
        return SerializadorVacio

    # def get_permissions(self):
    #     if self.action in ["list", "retrieve", "create", "update", "destroy"]:
    #         permission_classes = [EsSuperAdministrador]
    #     elif self.action == "Activar":
    #         permission_classes = [EsSuperAdministrador]
    #     elif self.action == "Obtener":
    #         permission_classes = [IsAuthenticated, PermisosPersonalizados]
    #     else:
    #         permission_classes = [IsAuthenticated]
    #     return [permission() for permission in permission_classes]

    queryset = ModeloTipoEmpresa.objects.all()

    # ===========================================
    # LISTAR (GET /TipoEmpresa/)
    # ===========================================
    def list(self, request):
        TipoEmpresas = ServicioTipoEmpresa.ObtenerTiposEmpresas()
        Serializador = SerializadorListaTipoEmpresa(TipoEmpresas, many=True)
        return Response(Serializador.data, status=status.HTTP_200_OK)

    # ===========================================
    # OBTENER (GET /TipoEmpresa/{id}/)
    # ===========================================
    def retrieve(self, request, pk=None):
        TipoEmpresa = ServicioTipoEmpresa.ObtenerTipoEmpresaPorId(pk)
        Serializador = SerializadorDetalleTipoEmpresa(TipoEmpresa)
        return Response(Serializador.data, status=status.HTTP_200_OK)

    # ===========================================
    # CREAR (POST /TipoEmpresa/)
    # ===========================================
    def create(self, request):
        Serializador = SerializadorCrearTipoEmpresa(data=request.data)
        Serializador.is_valid(raise_exception=True)
        TipoEmpresa = ServicioTipoEmpresa.CrearTipoEmpresa(Serializador.validated_data)
        SerializadorRespuesta = SerializadorDetalleTipoEmpresa(TipoEmpresa)
        return Response(SerializadorRespuesta.data, status=status.HTTP_201_CREATED)

    # ===========================================
    # ACTUALIZAR COMPLETO (PUT /TipoEmpresa/{id}/)
    # ===========================================
    def update(self, request, pk=None):
        TipoEmpresa = ServicioTipoEmpresa.ObtenerTipoEmpresaPorId(pk)
        Serializador = SerializadorActualizarTipoEmpresa(TipoEmpresa, data=request.data)
        Serializador.is_valid(raise_exception=True)
        TipoEmpresa = ServicioTipoEmpresa.ActualizarTipoEmpresa(TipoEmpresa,Serializador.validated_data)
        return Response(SerializadorDetalleTipoEmpresa(TipoEmpresa).data, status=status.HTTP_200_OK)

    # ===========================================
    # ACTIVAR (PATCH /TipoEmpresa/{id}/)
    # ===========================================
    @extend_schema(request=None, responses={200: None})
    #@action(detail=True, methods=["patch"], permission_classes = [EsSuperAdministrador])
    def Activar(self, request, pk=None):
        TipoEmpresa = ServicioTipoEmpresa.ObtenerTipoEmpresaPorId(pk)
        ServicioTipoEmpresa.ActivarTipoEmpresa(TipoEmpresa)
        return Response({"Mensaje": "TipoEmpresa"}, status=status.HTTP_200_OK)

    # ===========================================
    # ELIMINAR (DELETE /TipoEmpresa/{id}/)
    # ===========================================
    @extend_schema(request=None, responses={200: None})
    def destroy(self, request, pk=None):
        TipoEmpresa = ServicioTipoEmpresa.ObtenerTipoEmpresaPorId(pk)
        ServicioTipoEmpresa.EliminarTipoEmpresa(TipoEmpresa)
        return Response({"Mensaje": "TipoEmpresa Eliminado"}, status=status.HTTP_200_OK)