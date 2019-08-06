# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from rbac import models
from crm.models import User
# Register your models here.
class PermissionAdmin(admin.ModelAdmin):
    list_display = ['title','url',"name","menu"]
    list_editable = ['url',"name","menu"]

admin.site.register(models.Permission,PermissionAdmin)
admin.site.register(models.Role)
admin.site.register(User)
admin.site.register(models.Menu)
