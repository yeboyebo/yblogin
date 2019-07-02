# @class_declaration interna_aqn_user #
import importlib

from YBUTILS.viewREST import helpers

from models.fllogin import models as modelos


class interna_aqn_user(modelos.mtd_aqn_user, helpers.MixinConAcciones):
    pass

    @helpers.decoradores.accion(aqparam=["oParam"])
    def getUsuariosProyecto(self, oParam):
        return form.iface.getUsuariosProyecto(oParam)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def getParticipantesProyecto(self, oParam):
        return form.iface.getParticipantesProyecto(oParam)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def getParticProyectosUsu(self, oParam):
        return form.iface.getParticProyectosUsu(oParam)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def getParticCompaniaUsu(self, oParam):
        return form.iface.getParticCompaniaUsu(oParam)

    @helpers.decoradores.accion(aqparam=["oParam", "cursor"])
    def desactivar_usuario(self, oParam, cursor):
        return form.iface.desactivar_usuario(self, oParam, cursor)

    def checkCambiaPassword(cursor):
        return form.iface.checkCambiaPassword(cursor)

    def checkDrawUser(cursor):
        return form.iface.checkDrawUser(cursor)

    class Meta:
        proxy = True


# @class_declaration yblogin_aqn_user #
class yblogin_aqn_user(interna_aqn_user, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration aqn_user #
class aqn_user(yblogin_aqn_user, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.fllogin.aqn_user_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
# # @class_declaration interna_aqn_user #
# import importlib

# from YBUTILS.viewREST import helpers
# from YBLEGACY.FLUtil import FLUtil

# from models.fllogin import models as modelos
# from YBLEGACY import baseraw


# class mtd_aqn_user(baseraw):
#     idusuario = baseraw.AutoField(db_column="idusuario", verbose_name=FLUtil.translate(u"Identificador", u"MetaData"), primary_key=True)._miextend(visiblegrid=False, OLDTIPO="SERIAL")
#     password = baseraw.CharField(max_length=128)._miextend(OLDTIPO="STRING")
#     last_login = baseraw.DateTimeField(blank=True, null=True)._miextend(OLDTIPO="DATE")
#     usuario = baseraw.CharField(max_length=30, blank=True, null=True)._miextend(OLDTIPO="STRING")
#     nombre = baseraw.CharField(max_length=30, blank=True, null=True)._miextend(OLDTIPO="STRING")
#     apellidos = baseraw.CharField(max_length=30, blank=True, null=True)._miextend(OLDTIPO="STRING")
#     email = baseraw.CharField(unique=True, max_length=254)._miextend(OLDTIPO="STRING")
#     activo = models.BooleanField()._miextend(OLDTIPO="BOOL")
#     idcompany = baseraw.ForeignKey("mtd_aqn_companies", db_column="idcompany", verbose_name=FLUtil.translate(u"Compañia", u"MetaData"), blank=True, null=True, to_field="idcompany", on_delete=FLUtil.deleteCascade, related_name="aqn_user_idcompany__fk__aqn_companies_idcompany")._miextend(visiblegrid=False, OLDTIPO="UINT")

#     class Meta:
#         abstract = True


# class interna_aqn_user(mtd_aqn_user, helpers.MixinConAcciones):
#     pass

#     class Meta:
#         abstract = True


# # @class_declaration yblogin_aqn_user #
# class yblogin_aqn_user(interna_aqn_user, helpers.MixinConAcciones):
#     pass

#     class Meta:
#         abstract = True


# # @class_declaration aqn_user #
# class aqn_user(yblogin_aqn_user, helpers.MixinConAcciones):
#     pass

#     class Meta:
#         managed = True
#         verbose_name = "Usuarios"
#         db_table = 'aqn_user'

#     def getIface(self=None):
#         return form.iface


# definitions = importlib.import_module("models.fllogin.aqn_user_def")
# form = definitions.FormInternalObj()
# form._class_init()
# form.iface.ctx = form.iface
# form.iface.iface = form.iface
