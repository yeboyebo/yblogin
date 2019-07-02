# @class_declaration interna #
from YBLEGACY import qsatype


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def __init__(self, context=None):
        self.ctx = context


# @class_declaration yblogin #
from YBLEGACY.constantes import *


class yblogin(interna):

    def yblogin_getDesc(self):
        return None

    def yblogin_check_permissions(self, model, prefix, pk, template, acl, accion):
        usuario = qsatype.FLUtil.nameUser()
        isadmin = qsatype.FLUtil.sqlSelect(u"auth_user", u"is_superuser", ustr(u"username = '", str(usuario), u"'"))
        if pk == usuario:
            return True
        elif not isadmin:
            return False
        return True

    def __init__(self, context=None):
        super().__init__(context)

    def getDesc(self):
        return self.ctx.yblogin_getDesc()

    def check_permissions(self, model, prefix, pk, template, acl, accion=None):
        return self.ctx.yblogin_check_permissions(model, prefix, pk, template, acl, accion)

# @class_declaration head #
class head(yblogin):

    def __init__(self, context=None):
        super().__init__(context)


# @class_declaration ifaceCtx #
class ifaceCtx(head):

    def __init__(self, context=None):
        super().__init__(context)


# @class_declaration FormInternalObj #
class FormInternalObj(qsatype.FormDBWidget):
    def _class_init(self):
        self.iface = ifaceCtx(self)
