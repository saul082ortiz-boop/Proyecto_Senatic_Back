from django.db import models

from APLICACION_USUARIOS.models import ModeloBase

class ModeloDepartamento(ModeloBase):

    Id = models.AutoField(db_column='Id', primary_key=True, null=False)
    Nombre = models.CharField(db_column='Nombre', max_length=100, unique=True)
    Codigo = models.CharField(max_length=5, unique=True, default=0)

    class Meta:
        db_table = "Departamento"
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ["Nombre"]

    def __str__(self):
        return self.Nombre