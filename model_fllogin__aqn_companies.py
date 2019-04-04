# @class_declaration interna_aqn_companies #
import importlib

from YBUTILS.viewREST import helpers

from models.fllogin import models as modelos


class interna_aqn_companies(modelos.mtd_aqn_companies, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration yblogin_aqn_companies #
class yblogin_aqn_companies(interna_aqn_companies, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration aqn_companies #
class aqn_companies(yblogin_aqn_companies, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.fllogin.aqn_companies_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
