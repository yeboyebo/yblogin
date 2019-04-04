# @class_declaration interna_aqn_companias #
import importlib

from YBUTILS.viewREST import helpers

from models.fllogin import models as modelos


class interna_aqn_companias(modelos.mtd_aqn_companias, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration yblogin_aqn_companias #
class yblogin_aqn_companias(interna_aqn_companias, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration aqn_companias #
class aqn_companias(yblogin_aqn_companias, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.fllogin.aqn_companias_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
