from APLICACION_EMPRESA.models import ModeloDepartamento

class ServicioDepartamento:

    @staticmethod
    def ObtenerDepartamentos():
        return ModeloDepartamento.objects.all()

    @staticmethod
    def ObtenerDepartamentoPorId(DepartamentoId):
        return ModeloDepartamento.objects.get(Id=DepartamentoId)

    @staticmethod
    def CrearDepartamento(data):
        return ModeloDepartamento.objects.create(**data)

    @staticmethod
    def ActualizarDepartamento(Departamento, data):
        Departamento.Nombre = data.get("Nombre", Departamento.Nombre)
        Departamento.Codigo = data.get("Codigo", Departamento.Codigo)
        Departamento.save()
        return Departamento
    
    @staticmethod
    def EliminarDepartamento(Departamento):
        Departamento.Estado = False
        Departamento.save()
        return Departamento
    
    @staticmethod
    def ActivarDepartamento(Departamento):
        Departamento.Estado = True
        Departamento.save()
        return Departamento