from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
import re

class RbacMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.current_id=None
        request.breadcrumb_list=[{"url":'/index/',"title":"shouye"}]
        url=request.path_info
        for i in ["^/rbac/login/","/admin.*","/test/"]:
            if re.match(i,url):
                return

        is_login=request.session.get('is_login')


        if not is_login:
            return HttpResponse("weidenglu")

        for i in ["/index/","/crm/class/add/"]:
            if re.match(i, url):
                return

        permission_list=request.session["permissions"]
        for i in permission_list.values():
            if re.match("^{}$".format(i['url']),url):
                pid=i.get("pid")
                id=i.get("id")
                pname=i.get("pname")
                if pid:
                    request.current_id=pid
                    request.breadcrumb_list.append({"url": permission_list[pname]["url"], 'title': permission_list[pname]["title"]})
                    request.breadcrumb_list.append({"url": i["url"], 'title': i["title"]})
                else:
                    request.current_id=id
                    request.breadcrumb_list.append({"url":i["url"],'title':i["title"]})
                return

        return HttpResponse("no permissions")