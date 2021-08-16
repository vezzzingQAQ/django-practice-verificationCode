from django.http.response import JsonResponse
from django.urls import path
from myapp import views

from myapp.views import MyView
from myapp import verify

urlpatterns=[#小写！！！
    path('',views.index,name="index"),#首页
    path('verifyPage',verify.verifyPage,name="verifypage"),#验证码页面

    path('simpleHttpResponse',views.simpleHttpResponse,name="simplehttpresponse"),
    path('raise404',views.raise404,name="raise404"),
    path('raise403',views.raise403,name="raise403"),
    path('redirectPage',views.redirectPage,name="redirectpage"),
    path('jsJumpPage',views.jsJumpPage,name="jsjumppage"),
    path('basedOnClass',MyView.as_view(),name="basedonclass"),
    path('responseJson',views.responseJason,name="responsejson"),
    path('useCookie',views.useCookie,name="usecookie"),
    path('getCookie',views.getCookie,name="getcookie"),
    path('countAccess',views.countAccess,name="countaccess"),

    path('getPathMethodEncoding',views.getPathMethodEncoding,name="getpathmethodencoding"),
    path('processUrlPara',views.processUrlPara,name="processurlpara"),

    path('verify',verify.createVerifycode,name="verify"),
]