# @class_declaration interna #
from YBLEGACY import qsatype
from django.contrib.auth.models import User, Group


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def __init__(self, context=None):
        self.ctx = context


# @class_declaration yblogin #
from YBLEGACY.constantes import *


class yblogin(interna):

    def yblogin_initValidation(self, name, data=None):
        response = True
        return response

    def yblogin_iniciaValoresLabel(self, model=None, template=None, cursor=None):
        labels = {}
        return labels

    def yblogin_bChLabel(self, fN=None, cursor=None):
        labels = {}
        return labels

    def yblogin_getFilters(self, model, name, template=None):
        filters = []
        return filters

    def yblogin_getForeignFields(self, model, template=None):
        fields = []
        return fields

    def yblogin_getDesc(self):
        desc = "name"
        return desc

    def yblogin_queryGrid_usergroups(self, model, filters):
        query = {}
        query["tablesList"] = u"auth_user_groups, auth_user"
        query["select"] = u"auth_user.username"
        query["from"] = u"auth_user INNER JOIN auth_user_groups ON auth_user.id = auth_user_groups.user_id"
        query["where"] = u"auth_user_groups.group_id = " + str(model.pk)
        # query["orderby"] = ""
        return query

    def yblogin_eliminarUsuario(self, model, oParam):
        response = {}
        if "selecteds" not in oParam or not oParam['selecteds']:
            response['status'] = -1
            response['msg'] = "Debes seleccionar al menos un usuario"
            return response
        aChecked = oParam['selecteds'].split(u",")
        for u in aChecked:
            user = User.objects.get(username=u)
            user.groups.remove(Group.objects.get(id=model.pk))
            user.save()
        return True

    def yblogin_accessControl(self, model):
        url = '/system/acl/auth_group/' + str(model.pk)
        return url

    def yblogin_changePermision(self, model, oParam):
        oParam["tipoAcl"] = "grupo"
        oParam["pk"] = model.pk
        return fllogin_def.iface.changePermision(model, oParam)

    def __init__(self, context=None):
        super().__init__(context)

    def initValidation(self, name, data=None):
        return self.ctx.yblogin_initValidation(name, data=None)

    def iniciaValoresLabel(self, model=None, template=None, cursor=None):
        return self.ctx.yblogin_iniciaValoresLabel(model, template, cursor)

    def bChLabel(self, fN=None, cursor=None):
        return self.ctx.yblogin_bChLabel(fN, cursor)

    def getFilters(self, model, name, template=None):
        return self.ctx.yblogin_getFilters(model, name, template)

    def getForeignFields(self, model, template=None):
        return self.ctx.yblogin_getForeignFields(model, template)

    def getDesc(self):
        return self.ctx.yblogin_getDesc()

    def queryGrid_usergroups(self, model, filters):
        return self.ctx.yblogin_queryGrid_usergroups(model, filters)

    def eliminarUsuario(self, model, oParam):
        return self.ctx.yblogin_eliminarUsuario(model, oParam)

    def accessControl(self, model):
        return self.ctx.yblogin_accessControl(model)

    def changePermision(self, model, oParam):
        return self.ctx.yblogin_changePermision(model, oParam)


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
