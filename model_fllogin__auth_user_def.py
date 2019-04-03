# @class_declaration interna #
from django.contrib.auth.models import User, Group

from YBLEGACY import qsatype


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
        desc = "username"
        return desc

    def yblogin_queryGrid_usergroups(self, model):
        query = {}
        query["tablesList"] = u"auth_user_groups, auth_user, auth_group"
        query["select"] = u"auth_group.name"
        query["from"] = u"auth_group INNER JOIN auth_user_groups ON auth_group.id = auth_user_groups.group_id"
        query["where"] = u"auth_user_groups.user_id = " + str(model.pk)
        return query

    def yblogin_NuevoGrupo(self, model, oParam):
        if "data" not in oParam:
            response = {}
            response['status'] = -1
            response['data'] = {"selecteds": oParam['selecteds']}
            response['params'] = [
                {
                    "componente": "YBFieldDB",
                    "prefix": "otros",
                    "key": "name",
                    "desc": "name",
                    "disabled_name": "Grupo",
                    "auto_name": "Grupo",
                    "disabled_field": "name",
                    "auto_field": "name",
                    "tipo": "5",
                    "rel": "auth_group",
                    "relData": "false",
                    "className": "relatedField"
                }
            ]
            return response

        user = User.objects.get(id=model.pk)
        user.groups.add(Group.objects.get(name=str(oParam["data"]["name"])))
        user.save()
        return True

    def yblogin_salirGrupo(self, model, oParam):
        response = {}
        if "selecteds" not in oParam or not oParam['selecteds']:
            response['status'] = -1
            response['msg'] = "Debes seleccionar al menos un grupo"
            return response
        aChecked = oParam['selecteds'].split(u",")
        for g in aChecked:
            user = User.objects.get(id=model.pk)
            user.groups.remove(Group.objects.get(name=str(g)))
            user.save()
        return True

    def yblogin_changePermision(self, model, oParam):
        oParam["tipoAcl"] = "usuario"
        oParam["pk"] = model.pk
        return fllogin_def.iface.changePermision(model, oParam)

    def yblogin_accessControl(self, model):
        url = '/system/acl/auth_user/' + str(model.pk)
        return url

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

    def queryGrid_usergroups(self, model):
        return self.ctx.yblogin_queryGrid_usergroups(model)

    def salirGrupo(self, model, oParam):
        return self.ctx.yblogin_salirGrupo(model, oParam)

    def NuevoGrupo(self, model, oParam):
        return self.ctx.yblogin_NuevoGrupo(model, oParam)

    def changePermision(self, model, oParam):
        return self.ctx.yblogin_changePermision(model, oParam)

    def accessControl(self, model):
        return self.ctx.yblogin_accessControl(model)


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
