from django.db import models
from YBLEGACY.FLUtil import FLUtil
from YBLEGACY.clasesBase import BaseModel


def _miextend(self, **kwargs):
    self._legacy_mtd = kwargs
    return self


models.Field._miextend = _miextend


class mtd_auth_group(models.Model, BaseModel):
    id = models.AutoField(db_column="id", verbose_name=FLUtil.translate(u"Identificador", u"MetaData"), primary_key=True)._miextend(visiblegrid=False, OLDTIPO="SERIAL")
    name = models.CharField(unique=True, max_length=80)._miextend(OLDTIPO="STRING")

    class Meta:
        managed = False
        verbose_name = "Grupos"
        db_table = 'auth_group'


class mtd_auth_user(models.Model, BaseModel):
    id = models.AutoField(db_column="id", verbose_name=FLUtil.translate(u"Identificador", u"MetaData"), primary_key=True)._miextend(visiblegrid=False, OLDTIPO="SERIAL")
    password = models.CharField(max_length=128)._miextend(OLDTIPO="STRING")
    last_login = models.DateTimeField(blank=True, null=True)._miextend(OLDTIPO="DATE")
    is_superuser = models.BooleanField()._miextend(OLDTIPO="BOOL")
    username = models.CharField(unique=True, max_length=30)._miextend(OLDTIPO="STRING")
    first_name = models.CharField(max_length=30)._miextend(OLDTIPO="STRING")
    last_name = models.CharField(max_length=30)._miextend(OLDTIPO="STRING")
    email = models.CharField(max_length=254)._miextend(OLDTIPO="STRING")
    is_staff = models.BooleanField()._miextend(OLDTIPO="BOOL")
    is_active = models.BooleanField()._miextend(OLDTIPO="BOOL")
    date_joined = models.DateTimeField()._miextend(OLDTIPO="DATE")

    class Meta:
        managed = False
        verbose_name = "Usuarios"
        db_table = 'auth_user'


class mtd_auth_user_groups(models.Model, BaseModel):
    user = models.ForeignKey(mtd_auth_user)._miextend()
    group = models.ForeignKey(mtd_auth_group)._miextend()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class mtd_sis_acl(models.Model, BaseModel):
    id = models.AutoField(db_column="id", verbose_name=FLUtil.translate(u"Identificador", u"MetaData"), primary_key=True)._miextend(visiblegrid=False, OLDTIPO="SERIAL")
    usuario = models.CharField(blank=True, null=True, max_length=20)._miextend(OLDTIPO="STRING")
    grupo = models.TextField(blank=True, null=True)._miextend(OLDTIPO="STRING")
    tipo = models.CharField(db_column="tipo", verbose_name=FLUtil.translate(u"Tipo", u"MetaData"), default=u"tabla", max_length=10)._miextend(optionslist=u"tabla,accion,app", OLDTIPO="STRING")
    valor = models.CharField(blank=True, null=True, max_length=50)._miextend(OLDTIPO="STRING")
    # app = models.CharField(db_column="app", verbose_name="app", blank=True, null=True, max_length=50)._miextend(OLDTIPO="STRING")
    permiso = models.CharField(blank=True, null=True, max_length=2)._miextend(OLDTIPO="STRING")

    class Meta:
        managed = True
        verbose_name = FLUtil.translate(u"Control de acceso", u"MetaData")
        db_table = 'sis_acl'


class mtd_aqn_user(models.Model, BaseModel):
    id = models.AutoField(db_column="id", verbose_name=FLUtil.translate(u"Identificador", u"MetaData"), primary_key=True)._miextend(visiblegrid=False, OLDTIPO="SERIAL")
    password = models.CharField(max_length=128)._miextend(OLDTIPO="STRING")
    last_login = models.DateTimeField(blank=True, null=True)._miextend(OLDTIPO="DATE")
    usuario = models.CharField(max_length=30)._miextend(OLDTIPO="STRING")
    nombre = models.CharField(max_length=30)._miextend(OLDTIPO="STRING")
    apellidos = models.CharField(max_length=30)._miextend(OLDTIPO="STRING")
    email = models.CharField(unique=True, max_length=254)._miextend(OLDTIPO="STRING")
    idcompania = models.ForeignKey("mtd_aqn_companias", db_column="idcompania", verbose_name=FLUtil.translate(u"Compañia", u"MetaData"), blank=True, null=True, to_field="idcompania", on_delete=FLUtil.deleteCascade, related_name="aqn_user_idcompania__fk__aqn_companias_idcompania")._miextend(visiblegrid=False, OLDTIPO="UINT")

    class Meta:
        managed = True
        verbose_name = "Usuarios"
        db_table = 'aqn_user'


class mtd_aqn_companias(models.Model, BaseModel):
    idcompania = models.AutoField(db_column="idcompania", verbose_name=FLUtil.translate(u"Código", u"MetaData"), primary_key=True, blank=False)._miextend(REQUIRED=True, visiblegrid=False, OLDTIPO="SERIAL")
    nombre = models.CharField(db_column="nombre", verbose_name=FLUtil.translate(u"Nombre proyecto", u"MetaData"), blank=False, null=True, max_length=50)._miextend(REQUIRED=True, OLDTIPO="STRING")
    descripcion = models.CharField(db_column="descripcion", verbose_name=FLUtil.translate(u"Descripción", u"MetaData"), blank=True, null=True, max_length=200)._miextend(OLDTIPO="STRING")

    class Meta:
        managed = True
        verbose_name = FLUtil.translate(u"Compañias", u"MetaData")
        db_table = u"aqn_companias"
