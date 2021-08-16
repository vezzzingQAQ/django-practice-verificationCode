
from django.http.response import HttpResponse
from django.shortcuts import render

def verifyPage(request):
    return(render(request,"myapp/verify.html"))

def createVerifycode(request):
    from PIL import Image,ImageDraw,ImageFont
    import random

    bgcolor=(random.randrange(120,200),random.randrange(20,200),random.randrange(20,200))
    width=300
    height=75

    #画板对象
    im=Image.new("RGB",(width,height),bgcolor)
    #画笔对象
    painter=ImageDraw.Draw(im)

    #调用画笔的point函数画噪点
    for i in range(0,911):
        xy=(random.randrange(0,width),random.randrange(0,height))
        fill=(random.randrange(20,100),random.randrange(20,100),random.randrange(0,23))
        painter.point(xy,fill=fill)

    #验证码备选值
    strCode="ABCD2345EFGHIJKMNOPQRSTUVWXYZ6789"

    #随机取4个字符
    verifyCode=""
    for i in range(0,4):
        verifyCode+=strCode[random.randrange(0,len(strCode))]

    #默认字体
    font=ImageFont.truetype('static/ariali.ttf',69)
    #字体颜色
    fontcolor=(random.randrange(0,100),random.randrange(0,100),random.randrange(0,100))
    #绘制四个字
    painter.text((15,4),verifyCode[0],font=font,fill=fontcolor)
    painter.text((90,4),verifyCode[1],font=font,fill=fontcolor)
    painter.text((165,6),verifyCode[2],font=font,fill=fontcolor)
    painter.text((225,6),verifyCode[3],font=font,fill=fontcolor)

    #释放画笔
    del painter

    #存入session
    #request.session['verifyCode']=verifyCode

    #输出图像
    import io

    buf=io.BytesIO()
    im.save(buf,'png')

    #返回客户端
    return(HttpResponse(buf.getvalue(),'image/png'))
