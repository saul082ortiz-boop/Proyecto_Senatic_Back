from APLICACION_EMPRESA.models import ModeloEmpresa

class ServicioEmpresa:

    @staticmethod
    def ObtenerEmpresas():
        return ModeloEmpresa.objects.all()

    @staticmethod
    def ObtenerEmpresaPorId(EmpresaId):
        return ModeloEmpresa.objects.get(Id=EmpresaId)

    @staticmethod
    def CrearEmpresa(data):
        return ModeloEmpresa.objects.create(**data)

    @staticmethod
    def ActualizarEmpresa(Empresa, data):
        Empresa.Nit = data.get("Nit", Empresa.Nit)
        Empresa.RazonSocial = data.get("RazonSocial", Empresa.RazonSocial)
        Empresa.Direccion = data.get("Direccion", Empresa.Direccion)
        Empresa.Municipio = data.get("Municipio", Empresa.Municipio)
        Empresa.Barrio = data.get("Barrio", Empresa.Barrio)
        Empresa.Telefono = data.get("Telefono", Empresa.Telefono)
        Empresa.Correo = data.get("Correo", Empresa.Correo)
        Empresa.CuposHora = data.get("CuposHora", Empresa.CuposHora)
        Empresa.TipoEmpresa = data.get("TipoEmpresa", Empresa.TipoEmpresa)
        Empresa.Administrador = data.get("Administrador", Empresa.Administrador)
        Empresa.save()
        return Empresa
    
    @staticmethod
    def EliminarEmpresa(Empresa):
        Empresa.Estado = False
        Empresa.save()
        return Empresa
    
    @staticmethod
    def ActivarEmpresa(Empresa):
        Empresa.Estado = True
        Empresa.save()
        return Empresa

    @staticmethod
    def ActualizarLogo(Empresa, Logo):
        Empresa.Logo = Logo
        Empresa.save(update_fields=["Logo", "FechaActualizacion",])
        return Empresa