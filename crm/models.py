# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.safestring import mark_safe
from django.db import models
from rbac.models import RbacUser
# Create your models here.

class Depart(models.Model):
    name=models.CharField(max_length=32,verbose_name="depart_name")
    desc=models.TextField(verbose_name="depart_desc")
    def __str__(self):
        return self.name

class User(RbacUser,models.Model):
    name=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    gender=models.IntegerField(choices=((0,"man"),(1,"woman")),verbose_name="xingbie")
    depart=models.ForeignKey("Depart",on_delete=models.CASCADE,verbose_name="departname")
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(verbose_name='coursename', max_length=32)
    def __str__(self):
        return self.name

class School(models.Model):
    title = models.CharField(verbose_name='schoolname', max_length=32)
    def __str__(self):
        return self.title

class ClassList(models.Model):
    school = models.ForeignKey(verbose_name='xiaoqu', to='School')
    course = models.ForeignKey(verbose_name='kecheng', to='Course')
    semester = models.IntegerField(verbose_name="grade(qi)")
    price = models.IntegerField(verbose_name="xuefei")
    start_date = models.DateField(verbose_name="kaipanriqi")
    graduate_date = models.DateField(verbose_name="jieyeriqi", null=True, blank=True)
    tutor = models.ForeignKey(verbose_name='banzhuren', to='User', related_name='classes')
    teachers = models.ManyToManyField(verbose_name='renkelaoshi', to='User', related_name='teach_classes')
    memo = models.CharField(verbose_name='shuoming', max_length=255, blank=True, null=True)
    def show_teachers(self):
        # return ' | '.join([ i.name for i in self.teachers.all()])
        return mark_safe('<a href="https://v3.bootcss.com/components/#pagination">tiaozhuan</a>')



