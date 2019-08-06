# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Menu(models.Model):
    title=models.CharField(max_length=32)
    icon=models.CharField(max_length=32)
    weight=models.IntegerField(default=1)
    def __str__(self):
        return self.title

# Create your models here.
class Permission(models.Model):
    url=models.CharField('URL', max_length=128)
    title=models.CharField('TITLE', max_length=32, blank=True, null=True)
    name=models.CharField("urlbieming",max_length=32)
    menu=models.ForeignKey("Menu",blank=True,null=True)
    parent=models.ForeignKey("Permission",blank=True,null=True)
    def __str__(self):
        return self.title

class Role(models.Model):
    name = models.CharField('ROLENAME', max_length=32)
    permissions=models.ManyToManyField("Permission",verbose_name="ROLEandPER",blank=True)

    def __str__(self):
        return self.name


class RbacUser(models.Model):
    #kua biao de shihou   manytomany buneng jiayinghao
    roles = models.ManyToManyField(Role, verbose_name='yonghudejiaose', blank=True)

    class Meta:
        abstract = True