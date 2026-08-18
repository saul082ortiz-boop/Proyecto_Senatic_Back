from APLICACION_USUARIOS.models import ModeloTipoIdentificacion

class ServicioTipoIdentificacion:

    @staticmethod
    def ObtenerTiposIdentificaciones():
        return ModeloTipoIdentificacion.objects.all()

    @staticmethod
    def ObtenerTipoIdentificacionPorId(TipoIdentificacionId):
        return ModeloTipoIdentificacion.objects.get(Id=TipoIdentificacionId)

    @staticmethod
    def CrearTipoIdentificacion(data):
        return ModeloTipoIdentificacion.objects.create(**data)

    @staticmethod
    def ActualizarTipoIdentificacion(TipoIdentificacion, data):
        TipoIdentificacion.Nombre = data.get("Nombre", TipoIdentificacion.Nombre)
        TipoIdentificacion.Abreviatura = data.get("Abreviatura", TipoIdentificacion.Abreviatura)
        TipoIdentificacion.save()
        return TipoIdentificacion
    
    @staticmethod
    def EliminarTipoIdentificacion(TipoIdentificacion):
        TipoIdentificacion.Estado = False
        TipoIdentificacion.save()
        return TipoIdentificacion
    
    @staticmethod
    def ActivarTipoIdentificacion(TipoIdentificacion):
        TipoIdentificacion.Estado = True
        TipoIdentificacion.save()
        return TipoIdentificacion