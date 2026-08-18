from django.db import models

from .ModeloBase import ModeloBase


class ModeloTipoIdentificacion(ModeloBase):

    Id = models.AutoField(db_column='Id', primary_key=True, null=False)
    Nombre = models.CharField(db_column='Nombre', max_length=100, unique=True)
    Abreviatura = models.CharField(db_column='Abreviatura', max_length=10, unique=True)

    class Meta:
        managed = True
        db_table = "Tipo_Identificacion"
        verbose_name = "Tipo de Identificación"
        verbose_name_plural = "Tipos de Identificación"

    def __str__(self):
        return self.Abreviatura