
# @class_declaration yblogin #
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.template.base import TemplateDoesNotExist

from YBUTILS.viewREST import accessControl
from YBUTILS.viewREST import cacheController
from YBUTILS.viewREST import helpers
from YBWEB.ctxJSON import templateCTX


def is_admin(user):
    return user.is_superuser


class yblogin(interna):

    def yblogin_forbiddenError(self, request):
        return render(request, "users/403.html")

    def yblogin_index(self, request):
        if request.GET:
            next_url = request.GET.get("next", None)
            if next_url:
                return HttpResponseRedirect(next_url)

        history = cacheController.addHistory(request, None, None)
        history = history["list"][history["pos"] - 1] if history["pos"] > 0 else history["list"][history["pos"]]
        usuario = request.user.username
        superuser = request.user.is_superuser

        dctMenu = templateCTX.cargaMenuJSON("portal/menu_portal.json")
        dctMenu = dctMenu["items"]
        miMenu = accessControl.accessControl.dameDashboard(request.user, dctMenu)

        # TODO
        if len(miMenu) == 1:
            return HttpResponseRedirect(miMenu[0]["NAME"])
        return render(request, "portal/index.html", {"aplic": "portal", "menuJson": miMenu, "usuario": usuario, "superuser": superuser, "history": history, "next": "/"})

    def yblogin_login(self, request, error=None):
        if not error:
            error = ""
        return render(request, "portal/login.html", {"error": error})

    def yblogin_signup(self, request, error):
        return render(request, "portal/signup.html", {"error": error})

    def yblogin_account(self, request, error):
        return render(request, "portal/account.html", {"error": error, "usuario": request.user})

    def yblogin_auth_login(self, request):
        if request.method == "POST":
            action = request.POST.get("action", None)
            username = request.POST.get("username", None).lower()
            password = request.POST.get("password", None)

            if action == "login":
                user = authenticate(username=username, password=password)
                if user is not None:
                    login_auth(request, user)
                else:
                    return self.iface.login(request, "Error de autentificación")
                accessControl.accessControl.registraAC()
                return HttpResponseRedirect("/")
        return self.iface.login(request)

    def yblogin_signup_request(self, request):
        if request.method == "POST":
            action = request.POST.get("action", None)
            username = request.POST.get("username", None)
            password = request.POST.get("password", None)
            password2 = request.POST.get("password2", None)

            if action == "signup":
                if password == password2:
                    try:
                        user = User.objects.create_user(username=username, password=password)
                        user.save()
                        return self.iface.signup(request, username + " Añadido")
                    except Exception as exc:
                        print(exc)
                        return self.iface.signup(request, "El usuario ya existe")
                else:
                    return self.iface.signup(request, "Las contraseñas no coinciden")
        return self.iface.signup(request, "")

    def yblogin_account_request(self, request):
        if request.method == "POST":
            action = request.POST.get("action", None)
            # username = request.POST.get("username", None)
            password = request.POST.get("password", None)
            password2 = request.POST.get("password2", None)

            if action == "account":
                if password == password2:
                    try:
                        usuario = str(request.user.username)
                        user = User.objects.get(username=usuario)
                        user.set_password(str(password))
                        user.save()
                        return HttpResponseRedirect("/login")
                    except Exception as exc:
                        print(exc)
                        return self.iface.account(request, "Error inesperado consulte administrador")
                else:
                    return self.iface.account(request, "Las contraseñas no coinciden")
        return self.iface.account(request, "")

    def yblogin_deleteUser(self, request, user):
        User.objects.filter(username=user).delete()
        return HttpResponseRedirect("/users")

    def yblogin_logout(self, *args, **kwargs):
        return auth_views.logout(*args, **kwargs)

    def __init__(self, context=None):
        super().__init__(context)

    def forbiddenError(self, request):
        return self.iface.yblogin_forbiddenError(request)

    @helpers.decoradores.check_authentication_iface
    def index(self, request):
        return self.iface.yblogin_index(request)

    def login(self, request, error=None):
        return self.iface.yblogin_login(request, error)

    def signup(self, request, error):
        return self.iface.yblogin_signup(request, error)

    def account(self, request, error):
        return self.iface.yblogin_account(request, error)

    def auth_login(self, request):
        return self.iface.yblogin_auth_login(request)

    @helpers.decoradores.check_authentication_iface
    @helpers.decoradores.check_system_authentication_iface
    def signup_request(self, request):
        return self.iface.yblogin_signup_request(request)

    @helpers.decoradores.check_authentication_iface
    def account_request(self, request):
        return self.iface.yblogin_account_request(request)

    @helpers.decoradores.check_authentication_iface
    @helpers.decoradores.check_system_authentication_iface
    def deleteUser(self, request, user):
        return self.iface.yblogin_deleteUser(request, user)

    def logout(self, *args, **kwargs):
        return self.iface.yblogin_logout(*args, **kwargs)

