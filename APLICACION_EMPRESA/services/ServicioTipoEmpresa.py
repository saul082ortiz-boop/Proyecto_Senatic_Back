from APLICACION_EMPRESA.models import ModeloTipoEmpresa

class ServicioTipoEmpresa:

    @staticmethod
    def ObtenerTiposEmpresas():
        return ModeloTipoEmpresa.objects.all()

    @staticmethod
    def ObtenerTipoEmpresaPorId(TipoEmpresaId):
        return ModeloTipoEmpresa.objects.get(Id=TipoEmpresaId)

    @staticmethod
    def CrearTipoEmpresa(data):
        return ModeloTipoEmpresa.objects.create(**data)

    @staticmethod
    def ActualizarTipoEmpresa(TipoEmpresa, data):
        TipoEmpresa.Nombre = data.get("Nombre", TipoEmpresa.Nombre)
        TipoEmpresa.save()
        return TipoEmpresa
    
    @staticmethod
    def EliminarTipoEmpresa(TipoEmpresa):
        TipoEmpresa.Estado = False
        TipoEmpresa.save()
        return TipoEmpresa
    
    @staticmethod
    def ActivarTipoEmpresa(TipoEmpresa):
        TipoEmpresa.Estado = True
        TipoEmpresa.save()
        return TipoEmpresa