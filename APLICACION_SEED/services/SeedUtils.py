import random

from APLICACION_EMPRESA.models import ModeloServicio

SERVICIOS = {
    "BARBERÍA": 
    [
        "CORTE DE CABELLO",
        "BARBA",
        "LAVADO",
        "TINTURA",
        "PERFILADO"
    ],
        
    "RESTAURANTE":
    [
        "DESAYUNO",
        "ALMUERZO",
        "CENA",
        "DOMICILIO"
    ],
        
    "TALLER":
    [
        "CAMBIO DE ACEITE",
        "ALINEACIÓN",
        "BALANCEO",
        "REVISIÓN GENERAL",
        "CAMBIO DE LLANTAS"
    ],
        
    "HOSPITAL":
    [
        "CONSULTA GENERAL",
        "CONSULTA ESPECIALIZADA",
        "VACUNACIÓN",
        "RADIOGRAFÍA",
        "LABORATORIO"
    ],
        
    "COLEGIO":
    [
        "MATRICULAS",
        "RETIROS",
        "ATENCIÓN A PADRES",
        "ATENCION A ESTUDIANTES"
    ]
}

class SeedUtils:

    @classmethod
    def Aleatorio(cls, queryset):
        Cantidad = queryset.count()
        Indice = random.randint(0, Cantidad - 1)
        return queryset[Indice]

    @classmethod
    def ServiciosPorTipoEmpresa(cls, Tipo_empresa):
        Nombres = SERVICIOS.get(Tipo_empresa.Nombre, [])
        Servicios = list(ModeloServicio.objects.filter(Nombre__in=Nombres))
        if not Servicios:
            return []
        Cantidad = random.randint(1, len(Servicios))
        return random.sample(Servicios, Cantidad)