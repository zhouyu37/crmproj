from django import template
import re
from  collections import OrderedDict
register=template.Library()

@register.filter
def add_sb(value,arg):
    return '{}-{}-sb'.format(value,arg)

@register.simple_tag
def str_join(*args,**kwargs):
    return "{}--{}".format('*'.join(args),"**".join(kwargs.values()))

@register.inclusion_tag("li.html")
def show_li(num):
    return {"number":range(num)}

@register.inclusion_tag("tmp.html")
def displaymenu(request):
    url=request.path_info
    menu_list=request.session['menu_list']
    for i in menu_list:
        if re.match('^{}$'.format(i['url']),url):
            i["class"]="active"
    return {"menulist":menu_list}

@register.inclusion_tag("menu.html")
def menu(request):
    url=request.path_info
    menus_dict=request.session["menu_dict"]
    ordered_dict=OrderedDict()
    for key in  sorted(menus_dict,key=lambda x:menus_dict[x]['weight'],reverse=True):
        i=ordered_dict[key]=menus_dict[key]
        i["class"]="hide"
        for child in i['children']:
            # if re.match("^{}$".format(child['url']),url):
            if child['id'] == request.current_id:
                 child['class']="active"
                 i['class']=""

    return {"menus_list":ordered_dict.values()}



@register.inclusion_tag("breadcrumb.html")
def breadcrumb(request):
    breadcrumb_list=request.breadcrumb_list
    return {"breadcrumb_list":breadcrumb_list}



@register.filter
def has_permission(request,name):
    if name in request.session["permissions"]:
        return True




from django.urls import reverse
@register.simple_tag
def  reverse_url(request,urlname,*args,**kwargs):
    paras=request.GET.urlencode()
    url=reverse(urlname,args=args,kwargs=kwargs)
    return "{}?{}".format(url,paras)
