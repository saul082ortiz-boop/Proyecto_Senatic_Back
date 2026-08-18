from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from APLICACION_EMPRESA.models import ModeloServicioEmpresa
from APLICACION_EMPRESA.serializers.read.ServicioEmpresa import SerializadorDetalleServicioEmpresa, SerializadorListaServicioEmpresa
from APLICACION_EMPRESA.services import ServicioServicioEmpresa

class VistasServicioEmpresa(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
    ):

    #permission_classes = [EsSuperAdministrador]

    def get_serializer_class(self):
        if self.action == "list":
            return SerializadorListaServicioEmpresa
        if self.action == "retrieve":
            return SerializadorDetalleServicioEmpresa

    queryset = ModeloServicioEmpresa.objects.all()

    #===========================================
    #LISTAR (GET /ServicioEmpresa/)
    #===========================================
    def list(self, request):
        ServiciosEmpresas = ServicioServicioEmpresa.ObtenerServiciosEmpresas()
        Serializador = SerializadorListaServicioEmpresa(ServiciosEmpresas, many=True)
        return Response(Serializador.data, status=status.HTTP_200_OK)

    #===========================================
    #OBTENER (GET /ServicioEmpresa/{id}/)
    #===========================================
    def retrieve(self, request, pk=None):
        ServicioEmpresa = ServicioServicioEmpresa.ObtenerServicioEmpresaPorId(pk)
        Serializador = SerializadorDetalleServicioEmpresa(ServicioEmpresa)
        return Response(Serializador.data, status=status.HTTP_200_OK)