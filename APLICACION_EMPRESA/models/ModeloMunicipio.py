from django.db import models

from APLICACION_USUARIOS.models import ModeloBase

from .ModeloDepartamento import ModeloDepartamento

class ModeloMunicipio(ModeloBase):

    Id = models.AutoField(db_column='Id', primary_key=True, null=False)
    Nombre = models.CharField(db_column='Nombre', max_length=120)
    Codigo = models.CharField(max_length=5, unique=True, default=0)
    Departamento = models.ForeignKey(ModeloDepartamento, on_delete=models.PROTECT, db_column='Departamento', related_name="Municipios")

    class Meta:
        db_table = "Municipio"
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"
        ordering = ["Nombre"]
        unique_together = ("Nombre", "Departamento")

    def __str__(self):
        return f"{self.Nombre}, {self.Departamento.Nombre}"