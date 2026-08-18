from django.db import transaction

from APLICACION_EMPRESA.models import ModeloServicioEmpresa

class ServicioServicioEmpresa:

    @staticmethod
    def ObtenerServiciosEmpresas():
        return ModeloServicioEmpresa.objects.all()

    @staticmethod
    def ObtenerServicioEmpresaPorId(ServicioEmpresaId):
        return ModeloServicioEmpresa.objects.get(Id=ServicioEmpresaId)

    @staticmethod
    def ObtenerServiciosPorEmpresa(Empresa):
        return ModeloServicioEmpresa.objects.filter(Empresa=Empresa)


    @staticmethod
    def ObtenerEmpresasPorServicio(Servicio):
        return ModeloServicioEmpresa.objects.filter(Servicio=Servicio)

    @staticmethod
    @transaction.atomic
    def AsignarEmpresas(Servicio, Empresas):
        ModeloServicioEmpresa.objects.filter(Servicio=Servicio).delete()
        ModeloServicioEmpresa.objects.bulk_create([ModeloServicioEmpresa(Servicio=Servicio, Empresa=Empresa)for Empresa in Empresas])
        return Servicio

    @staticmethod
    def RemoverEmpresas(Servicio, Empresas):
        ModeloServicioEmpresa.objects.filter(Servicio=Servicio, Empresa__in=Empresas).delete()