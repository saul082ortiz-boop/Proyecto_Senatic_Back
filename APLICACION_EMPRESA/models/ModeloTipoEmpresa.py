from django.db import models

from APLICACION_USUARIOS.models import ModeloBase

class ModeloTipoEmpresa(ModeloBase):

    Id = models.AutoField(db_column='Id', primary_key=True, null=False)
    Nombre = models.CharField(db_column='Nombre', max_length=100, unique=True)

    class Meta:
        db_table = "TipoEmpresa"
        verbose_name = "Tipo Empresa"
        verbose_name_plural = "Tipos de Empresa"
        ordering = ["Nombre"]

    def __str__(self):
        return self.Nombre