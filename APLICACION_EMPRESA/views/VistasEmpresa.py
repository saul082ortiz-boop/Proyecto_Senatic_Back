from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import FormParser
from rest_framework.decorators import action

from APLICACION_EMPRESA.models import ModeloEmpresa
from APLICACION_EMPRESA.serializers.read.Empresa import SerializadorDetalleEmpresa, SerializadorListaEmpresa
from APLICACION_EMPRESA.serializers.write.Empresa import SerializadorActualizarEmpresa, SerializadorCrearEmpresa, SerializadorLogoEmpresa
from APLICACION_EMPRESA.services import ServicioEmpresa
from APLICACION_USUARIOS.serializers.common import SerializadorVacio

class VistasEmpresa(
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
            return SerializadorListaEmpresa
        if self.action == "retrieve":
            return SerializadorDetalleEmpresa
        if self.action == "create":
            return SerializadorCrearEmpresa
        if self.action == "update":
            return SerializadorActualizarEmpresa
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

    queryset = ModeloEmpresa.objects.all()

    # ===========================================
    # LISTAR (GET /Empresa/)
    # ===========================================
    def list(self, request):
        Empresas = ServicioEmpresa.ObtenerEmpresas()
        Serializador = SerializadorListaEmpresa(Empresas, many=True)
        return Response(Serializador.data, status=status.HTTP_200_OK)

    # ===========================================
    # OBTENER (GET /Empresa/{id}/)
    # ===========================================
    def retrieve(self, request, pk=None):
        Empresa = ServicioEmpresa.ObtenerEmpresaPorId(pk)
        Serializador = SerializadorDetalleEmpresa(Empresa)
        return Response(Serializador.data, status=status.HTTP_200_OK)

    # ===========================================
    # CREAR (POST /Empresa/)
    # ===========================================
    from drf_spectacular.utils import extend_schema, OpenApiRequest

    def create(self, request):
        Serializador = SerializadorCrearEmpresa(data=request.data)
        Serializador.is_valid(raise_exception=True)
        Empresa = ServicioEmpresa.CrearEmpresa(Serializador.validated_data)
        SerializadorRespuesta = SerializadorDetalleEmpresa(Empresa)
        return Response(SerializadorRespuesta.data, status=status.HTTP_201_CREATED)

    # ===========================================
    # ACTUALIZAR COMPLETO (PUT /Empresa/{id}/)
    # ===========================================
    def update(self, request, pk=None):
        Empresa = ServicioEmpresa.ObtenerEmpresaPorId(pk)
        Serializador = SerializadorActualizarEmpresa(Empresa, data=request.data)
        Serializador.is_valid(raise_exception=True)
        Empresa = ServicioEmpresa.ActualizarEmpresa(Empresa,Serializador.validated_data)
        return Response(SerializadorDetalleEmpresa(Empresa).data, status=status.HTTP_200_OK)

    # ===========================================
    # ACTIVAR (PATCH /Empresa/{id}/)
    # ===========================================
    @extend_schema(request=None, responses={200: None})
    #@action(detail=True, methods=["patch"], permission_classes = [EsSuperAdministrador])
    def Activar(self, request, pk=None):
        Empresa = ServicioEmpresa.ObtenerEmpresaPorId(pk)
        ServicioEmpresa.ActivarEmpresa(Empresa)
        return Response({"Mensaje": "Empresa"}, status=status.HTTP_200_OK)

    # ===========================================
    # ELIMINAR (DELETE /Empresa/{id}/)
    # ===========================================
    @extend_schema(request=None, responses={200: None})
    def destroy(self, request, pk=None):
        Empresa = ServicioEmpresa.ObtenerEmpresaPorId(pk)
        ServicioEmpresa.EliminarEmpresa(Empresa)
        return Response({"Mensaje": "Empresa Eliminado"}, status=status.HTTP_200_OK)


    @extend_schema(request=SerializadorLogoEmpresa, responses={200: SerializadorDetalleEmpresa})
    @action(detail=True, methods=["post"], parser_classes=[MultiPartParser])
    def SubirLogo(self, request, Id=None):
        Empresa = ServicioEmpresa.ObtenerEmpresaPorId(Id)
        Serializador = SerializadorLogoEmpresa(data=request.data)
        Serializador.is_valid(raise_exception=True)
        Empresa = ServicioEmpresa.ActualizarLogo(Empresa, Serializador.validated_data["Logo"])
        return Response(SerializadorDetalleEmpresa(Empresa).data, status=status.HTTP_200_OK)