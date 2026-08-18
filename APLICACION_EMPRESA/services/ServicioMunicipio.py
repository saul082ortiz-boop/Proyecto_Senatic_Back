from APLICACION_EMPRESA.models import ModeloMunicipio

class ServicioMunicipio:

    @staticmethod
    def ObtenerMunicipios():
        return ModeloMunicipio.objects.all()

    @staticmethod
    def ObtenerMunicipioPorId(MunicipioId):
        return ModeloMunicipio.objects.get(Id=MunicipioId)

    @staticmethod
    def CrearMunicipio(data):
        return ModeloMunicipio.objects.create(**data)

    @staticmethod
    def ActualizarMunicipio(Municipio, data):
        Municipio.Nombre = data.get("Nombre", Municipio.Nombre)
        Municipio.Codigo = data.get("Codigo", Municipio.Codigo)
        Municipio.Departamento = data.get("Departamento", Municipio.Departamento)
        Municipio.save()
        return Municipio
    
    @staticmethod
    def EliminarMunicipio(Municipio):
        Municipio.Estado = False
        Municipio.save()
        return Municipio
    
    @staticmethod
    def ActivarMunicipio(Municipio):
        Municipio.Estado = True
        Municipio.save()
        return Municipio