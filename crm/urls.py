"""crmproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from crm import views

urlpatterns = [

    url(r'^depart/list/',views.depart_list,name="departlist" ),
    url(r'^depart/add/',views.depart_add,name="departadd" ),
    url(r'^depart/edit/(\d+)/',views.depart_edit,name="departedit" ),
    url(r'^depart/del/(\d+)/',views.depart_del,name="departdel" ),
    url(r'^user/list/',views.user_list,name="userlist" ),
    url(r'^user/add/',views.user_add,name="useradd" ),
    url(r'^user/edit/(\d+)/',views.user_edit,name="useredit" ),
    url(r'^user/del/(\d+)/',views.user_del,name="userdel" ),
    url(r'^class/list/',views.class_list,name="classlist" ),
    url(r'^class/add/',views.class_change,name="classadd" ),
    url(r'^class/edit/(\d+)/',views.class_change,name="classedit" ),

]
