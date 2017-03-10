# coding = utf-8
from django.shortcuts import render_to_response
from models import *


def register(request):
    if request.method == "POST" and request.POST:
        u = User()
        u.username = request.POST["username"]
        u.name = request.POST["name"]
        u.password = request.POST["password"]
        u.delete_flag = 'N'
        u.save()
    all_user = User.objects.filter(delete_flag='N')
    return render_to_response("register.html",locals())



def deleteData(request,userId):
    user = User.objects.get(id = int(userId))
    user.delete_flag = "Y"
    user.save()
    all_user = User.objects.filter(delete_flag='N')
    if request.method == "GET" and request.GET:
        user_id = request.GET["userId"]
        user = User.objects.get(id = int(user_id))
        # user.delete_flag = "Y"
        user.delete()
        # user.save()
    return render_to_response("register.html",locals())

def registerPrivilege(request):
    if request.method == "POST" and request.POST:
        # name = request.POST["name"]
        privilege = Privileges()
        privilege.pri_name = request.POST["pri_name"]
        privilege.delete_flag = "N"
        privilege.save()

        all_privilege = Privileges.objects.filter(delete_flag="N")
        all_user = User.objects.filter(delete_flag='N')

    return render_to_response("register.html",locals())


def userPrivilege(request):
    if request.method == "POST" and request.POST:
        userId = request.POST.get("userId")
        privilegeId = request.POST.get("privilegeId")
        up = UserPrivileges()
        up.userId = int(userId)
        up.privilegesId = int(privilegeId)
        up.delete_flag = "N"
        up.save()


    all_privilege = Privileges.objects.filter(delete_flag="N")
    all_user = User.objects.filter(delete_flag='N')
    all_privilege = UserPrivileges.objects.filter(delete_flag = "N")
    return render_to_response("register.html",locals())


def uprivilege(request):
    if request.method == "POST" and request.POST:
        user_id = request.POST.get("userId")
        sql = """

        """
        pass