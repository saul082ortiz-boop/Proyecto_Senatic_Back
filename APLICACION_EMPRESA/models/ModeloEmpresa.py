from django.db import models

from APLICACION_USUARIOS.models import ModeloBase
from APLICACION_USUARIOS.models import ModeloUsuario

from APLICACION_EMPRESA.models.RutasGuardado import RutaLogoEmpresa


from .ModeloMunicipio import ModeloMunicipio
from .ModeloTipoEmpresa import ModeloTipoEmpresa
import os
import uuid

class ModeloEmpresa(ModeloBase):

    Id = models.AutoField(db_column='Id', primary_key=True, null=False)
    Nit = models.CharField(db_column='Nit', max_length=20, unique=True)
    RazonSocial = models.CharField(db_column='RazonSocial', max_length=200)
    Logo = models.ImageField(db_column='Logo', upload_to=RutaLogoEmpresa, null=True, blank=True)
    Direccion = models.CharField(db_column='Direccion', max_length=250)
    Municipio = models.ForeignKey(ModeloMunicipio, on_delete=models.PROTECT, db_column='Municipio', related_name="Empresas")
    Barrio = models.CharField(db_column='Barrio', max_length=100)
    Telefono = models.CharField(db_column='Telefono', max_length=20)
    Correo = models.EmailField(db_column='Correo', )
    CuposHora = models.PositiveSmallIntegerField(db_column='CuposHora', default=1)
    TipoEmpresa = models.ForeignKey(ModeloTipoEmpresa, on_delete=models.PROTECT, db_column='TipoEmpresa', related_name="Empresas")
    Administrador = models.ForeignKey(ModeloUsuario, on_delete=models.PROTECT, db_column='Administrador', related_name="Empresas")

    class Meta:
        db_table = "Empresa"
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        ordering = ["RazonSocial"]

    def __str__(self):
        return self.RazonSocial