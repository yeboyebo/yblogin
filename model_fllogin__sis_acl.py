# @class_declaration interna_sis_acl #
from YBUTILS.viewREST import helpers
from models.fllogin import models as loginmodels
import importlib


class interna_sis_acl(loginmodels.mtd_sis_acl, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration sis_acl #
class sis_acl(interna_sis_acl, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


definitions = importlib.import_module("models.fllogin.sis_acl_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
