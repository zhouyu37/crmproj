from django.utils import reverse
def reverse_url(request,url_name,*args,**kwargs):
    paras = request.GET.urlencode()
    url = reverse(urlname, args=args, kwargs=kwargs)
    if paras:
        return "{}?{}".format(url, paras)
    return url