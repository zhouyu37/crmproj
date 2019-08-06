# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from crm import models
# Create your views here.
from utils import pagination
import hashlib


def depart_list(request):
    # change the request.py  zhong de  mutable
    # from django.http.request import  QueryDict
    # qd=request.GET.copy()  #deepcopy
    # qd['xxx']=1
    print("zhou11",request.GET,type(request.GET))
    print("zhou22",request.GET.urlencode())
    departs=models.Depart.objects.all()
    # depart_list=[]
    # for i in range(2,302):
    #     obj=models.Depart(name="bumen-{}".format(i))
    #     depart_list.append(obj)
    # models.Depart.objects.bulk_create(depart_list)
    # #begin
    # try:
    #     page_num=int(request.GET.get("page",1))
    # except Exception as e:
    #     page_num=1
    page_num=request.GET.get("page",1)
    #
    # start=(page_num-1)*10
    # end=page_num*10
    all_count=departs.count()
    per_num=10
    max_show=11
    objpag=pagination.Pagination(page_num,all_count,per_num,max_show)
    start=objpag.start()
    end=objpag.end()
    page_html=objpag.page_html()

    # half_show=max_show//2
    #
    # total_num,more =divmod(all_count,per_num)
    # if more:
    #     total_num+=1
    #
    # if total_num < max_show:
    #     page_start =1
    #     page_end =total_num
    # else:
    #     if page_num < half_show:
    #         page_start = 1
    #         page_end=page_num + half_show
    #     elif page_num + half_show > total_num:
    #         page_start=page_num-half_show
    #         page_end=total_num
    #     else:
    #         page_start = page_num - half_show
    #         page_end = page_num + half_show
    # #end

    # page_list=[]
    # for i in range(page_start,page_end+1):
    #     if  i == page_num:
    #         page_list.append("<li class='active'><a  href='?page={}'>{}</a></li>".format(i,i))
    #
    #     else:
    #         page_list.append("<li><a  href='?page={}'>{}</a></li>".format(i, i))
    #
    # page_html=''.join(page_list)
    # print(page_html)

    return render(request,"index.html",{"departs":departs[start:end],"page_html":page_html})


from django import forms
class DepartForm(forms.ModelForm):
    # name=forms.CharField(validators=[])
    class Meta:
        model=models.Depart
        fields="__all__"
#        exclude=['desc']
        widgets ={
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'})
        }
        error_messages ={
            'name':{
                'required':"cannot be none"
            }
        }

#the following  method can not run
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         for field in self.fields.values():
#             field.widget.attrs.update({'class':'form-control'})

def depart_add(request):
    formobj=DepartForm()
    if request.method == "POST":
        formobj=DepartForm(request.POST)
        if formobj.is_valid():
            print(formobj.cleaned_data)
            #models.Depart.objects.create(**formobj.cleaned_data)
            formobj.save()
            return redirect(reverse("crm:departlist"))

    return render(request,"depart_add.html",{"formobj":formobj})

def depart_edit(request,id):
    obj=models.Depart.objects.filter(id=id).first()
    formobj=DepartForm(instance=obj)
    if request.method == "POST":
        formobj = DepartForm(request.POST,instance=obj)
        if formobj.is_valid():
            formobj.save()
            paras=request.GET.urlencode()
            url=reverse("crm:departlist")
            if paras:
                url="{}?{}".format(url,paras)
                return redirect(url)
            return redirect(url)
    return render(request,"depart_edit.html",{"formobj":formobj})

def depart_del(request,id):
    models.Depart.objects.filter(id=id).delete()
    return redirect(reverse("crm:departlist"))

def user_list(request):
    users = models.User.objects.all()
    return render(request, "user_list.html", {"users": users})

from django.core.exceptions import ValidationError
class UserForm(forms.ModelForm):
    password=forms.CharField(
        label="password",
        min_length=6,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    re_password=forms.CharField(
        label="re_password",
        min_length=6,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = models.User
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'depart': forms.Select(attrs={'class': 'form-control'}),
        }


    def clean(self):
        pwd=self.cleaned_data.get("password")
        re_pwd=self.cleaned_data.get("re_password")
        if pwd==re_pwd:
            md5=hashlib.md5()
            print("zhou",md5)
            md5.update(pwd.encode('utf-8'))
            self.cleaned_data['password']=md5.hexdigest()
            return self.cleaned_data
        self.add_error("re_password","the pass is different twice")
        raise ValidationError("the pass is different twice")

def user_add(request):
    formobj=UserForm()
    if request.method == "POST":
        formobj = UserForm(request.POST)
        if formobj.is_valid():
            print(formobj.cleaned_data)
            formobj.save()
            return redirect(reverse("crm:userlist"))
    return render(request, "user_add.html", {"formobj": formobj})

def user_edit(request,id):
    obj = models.User.objects.filter(id=id).first()
    formobj = UserForm(instance=obj)
    if request.method == "POST":
        formobj = UserForm(request.POST,instance=obj)
        if formobj.is_valid():
            formobj.save()
            return redirect(reverse("crm:userlist"))
    return render(request,"user_edit.html",{"formobj":formobj})

def user_del(request,id):
    models.User.objects.filter(id=id).delete()
    return redirect(reverse("crm:userlist"))


def class_list(request):
    classes = models.ClassList.objects.all()
    return render(request, "class_list.html", {"classes": classes})

class ClassForm(forms.ModelForm):
    class Meta:
        model = models.ClassList
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ClassForm,self).__init__(*args, **kwargs)
        # for name, field in self.fields.items():
        #     print(name, field)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs.update({'class': 'form-control'})

def class_add(request):
    formobj=ClassForm()
    if request.method == "POST":
        formobj = ClassForm(request.POST)
        if formobj.is_valid():
            print(formobj.cleaned_data)
            formobj.save()
            return redirect(reverse("crm:classlist"))
    return render(request, "class_add.html", {"formobj": formobj})

def class_edit(request,id):
    obj = models.ClassList.objects.filter(id=id).first()
    formobj = ClassForm(instance=obj)
    if request.method == "POST":
        formobj = ClassForm(request.POST,instance=obj)
        if formobj.is_valid():
            formobj.save()
            return redirect(reverse("crm:classlist"))
    return render(request,"class_edit.html",{"formobj":formobj})

def class_change(request,id=None):
    obj = models.ClassList.objects.filter(id=id).first()
    formobj = ClassForm(instance=obj)
    if request.method == "POST":
        formobj = ClassForm(request.POST,instance=obj)
        if formobj.is_valid():
            formobj.save()
            return redirect(reverse("crm:classlist"))
    return render(request,"class_edit.html",{"formobj":formobj})

def index(request):
    return render(request,"indexnew.html")

def test(request):
    return render(request,"test.html",{"name":"alex"})