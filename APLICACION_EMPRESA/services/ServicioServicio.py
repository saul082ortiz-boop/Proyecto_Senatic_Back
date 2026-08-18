from APLICACION_EMPRESA.models import ModeloServicio

class ServicioServicio:

    @staticmethod
    def ObtenerServicios():
        return ModeloServicio.objects.all()

    @staticmethod
    def ObtenerServicioPorId(ServicioId):
        return ModeloServicio.objects.get(Id=ServicioId)

    @staticmethod
    def CrearServicio(data):
        return ModeloServicio.objects.create(**data)

    @staticmethod
    def ActualizarServicio(Servicio, data):
        Servicio.Nombre = data.get("Nombre", Servicio.Nombre)
        Servicio.save()
        return Servicio
    
    @staticmethod
    def EliminarServicio(Servicio):
        Servicio.Estado = False
        Servicio.save()
        return Servicio
    
    @staticmethod
    def ActivarServicio(Servicio):
        Servicio.Estado = True
        Servicio.save()
        return Servicio