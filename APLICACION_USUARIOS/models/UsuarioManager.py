from django.contrib.auth.base_user import BaseUserManager

from APLICACION_USUARIOS.models import ModeloTipoIdentificacion

class UsuarioManager(BaseUserManager):

    def create_user(self, Correo, password=None, **ExtraFields):
        if not Correo:
            raise ValueError("El Correo es obligatorio")
        TipoIdentificacionId = ExtraFields.get("TipoIdentificacion")
        TipoIdentificacion = ModeloTipoIdentificacion.objects.get(pk=TipoIdentificacionId)
        ExtraFields["TipoIdentificacion"] = TipoIdentificacion
        Correo = self.normalize_email(Correo)
        Usuario = self.model(Correo=Correo, **ExtraFields)
        Usuario.set_password(password)
        Usuario.save(using=self._db)
        return Usuario

    def create_superuser(self, Correo, password, **ExtraFields):
        ExtraFields.setdefault("is_staff", True)
        ExtraFields.setdefault("is_superuser", True)
        return self.create_user(Correo, password, **ExtraFields)
