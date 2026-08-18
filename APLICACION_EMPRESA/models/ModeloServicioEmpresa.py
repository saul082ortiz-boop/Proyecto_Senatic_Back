from django.db import models

from APLICACION_USUARIOS.models import ModeloBase

from .ModeloEmpresa import ModeloEmpresa
from .ModeloServicio import ModeloServicio

class ModeloServicioEmpresa(ModeloBase):

    Id = models.AutoField(db_column='Id', primary_key=True, null=False)
    Empresa = models.ForeignKey(ModeloEmpresa, on_delete=models.CASCADE, db_column='Empresa', related_name="Servicios")
    Servicio = models.ForeignKey(ModeloServicio, on_delete=models.PROTECT, db_column='Servicio', related_name="Empresas")

    class Meta:
        db_table = "ServiciosEmpresa"
        verbose_name = "Servicio Empresa"
        verbose_name_plural = "Servicios Empresa"
        unique_together = ("Empresa", "Servicio")

    def __str__(self):
        return f"{self.Empresa.RazonSocial} - {self.Servicio.Nombre}"