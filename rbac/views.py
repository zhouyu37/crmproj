# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from crm import models
# Create your views here.
import hashlib
from django.urls import reverse

def login(request):
    if request.method == "POST":
        name=request.POST.get("user")
        pwd=request.POST.get("pwd")
        md5 = hashlib.md5()
        md5.update(pwd.encode('utf-8'))
        pwd = md5.hexdigest()
        obj=models.User.objects.filter(name=name,password=pwd).first()
        if not obj:
            request.session['is_login'] = False
            return render(request,"login.html",{"error":"user or pwd is wrong!"})
        else:
            permission_qurey=obj.roles.filter(permissions__url__isnull=False).values("permissions__url",
                                                                                     "permissions__title",
                                                                                     "permissions__name",
                                                                                     "permissions__menu_id",
                                                                                     "permissions__menu__title",
                                                                                     "permissions__menu__icon",
                                                                                     "permissions__menu__weight",
                                                                                     "permissions__id",
                                                                                     "permissions__parent_id",
                                                                                     "permissions__parent__name",
                                                                                     ).distinct()
            # print(permission_qurey)
            permission_list={}
            # menu_list=[]
            menu_dict={}
            for i in permission_qurey:
                permission_list[i["permissions__name"]]={"url":i["permissions__url"],
                                                            "id":i["permissions__id"],
                                                            "pid":i["permissions__parent_id"],
                                                            "title":i["permissions__title"],
                                                            "pname":i["permissions__parent__name"],
                                                            }
                menu_id=i["permissions__menu_id"]
                if not menu_id:
                    continue
                if menu_id not in menu_dict:
                    menu_dict[menu_id]={
                        'title':i["permissions__menu__title"],
                        'icon':i["permissions__menu__icon"],
                        'weight':i["permissions__menu__weight"],
                        'class':"hide",
                        'children':[{"title":i["permissions__title"],'url':i["permissions__url"],'id':i["permissions__id"]}],
                    }
                else:
                    menu_dict[menu_id]['children'].append({"title":i["permissions__title"],'url':i["permissions__url"],'id':i["permissions__id"]})
                # if i["permissions__is_menu"]:
                #     menu_list.append({"title":i['permissions__title'],"url":i["permissions__url"]})
            request.session["permissions"]=permission_list
            # request.session["menu_list"] = menu_list
            request.session["menu_dict"] = menu_dict
            request.session['is_login']=True
            # print(permission_list.keys())
            print("zhoutest",request.session["menu_dict"])
            return redirect(reverse("index"))
    return render(request,"login.html")