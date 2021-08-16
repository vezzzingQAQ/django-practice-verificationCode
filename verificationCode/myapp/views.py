from django.http import response
from django.http.response import HttpResponse, HttpResponseNotFound,JsonResponse
from django.shortcuts import redirect, render

from django.urls import reverse

from django.views import View

# Create your views here.
def index(request):
    #不return会报错2333
    return(render(request,"myapp/index.html"))

def simpleHttpResponse(request):
    return(HttpResponse("简单HttpResponse"))

def raise404(request):
    return HttpResponseNotFound("<h1>Page not found</h1>")

def raise403(request):
    return HttpResponse(status=403)

def redirectPage(request):
    #重定向
    return(redirect(reverse("simplehttpresponse")))

def jsJumpPage(request):
    #重定向
    return(HttpResponse("<script>location.href='/simpleHttpResponse';</script>"))

#基于类的视图
class MyView(View):
    def get(self,request,*args,**kwargs):
        return(HttpResponse("hello,Views"))

#JSON数据响应
def responseJason(request):
    data=[
        {'id':1001,'name':'vez','age':20},
        {'id':1002,'name':'mez','age':22},
        {'id':1003,'name':'ijh','age':12},
    ]
    return(JsonResponse({'data':data}))

#set_cookie方法;常用于登录,登录以后即记录在本地浏览器上
def useCookie(request):
    response=HttpResponse("cookie设置")
    response.set_cookie('a','abc')
    return(response)

#获取cookie
def getCookie(request):
    return(HttpResponse(request.COOKIES.get('a',None)))

#用cookie做页面访问次数记录器
def countAccess(request):
    countNumber=request.COOKIES.get("num",None)
    print(countNumber)
    if countNumber!='None':#大坑
        countNumber=int(countNumber)+1
    else:
        countNumber=1
    response=HttpResponse("cookie记录的访问次数记录器:"+str(countNumber))
    response.set_cookie("num",countNumber)
    return(response)


#request,path
def getPathMethodEncoding(request):
    tempStr="<p>请求路径:"+request.path+"</p>"
    tempStr+="<p>请求方法:"+request.method+"</p>"
    #tempStr+="<p>请求编码:"+request.encoding+"</p>"
    return(HttpResponse(tempStr))
