from django.shortcuts import render,redirect
from .models import LoginInfo
from django.http import HttpResponse

#测试用例
def index(request):
    return HttpResponse("Hello, world. ") #test

def indexman(request):
    return render(request,"login/register.html")

'''登录系统功能'''
def loginSystem(request):
    userinfoList = LoginInfo.objects.all() #得到用户信息数据库列表  就是包含所有用户信息
    if request.method == "POST": #当传递参数后 submit
        user_name = request.POST.get("username",None) #获得输入的用户名
        pass_word = request.POST.get("password",None)  #获得输入的密码
        search_obj = LoginInfo.objects.get(username=user_name,password=pass_word) #判断数据库当中是否存在
        search_count = len(search_obj)
        if search_count == 1: #说明找到
            return redirect('indexman') #重定向到登录成功页面
        else:
            print("当前密码或用户名输错")
            return render(request, 'login/login.html', {'modellist': userinfoList})
    return render(request,'login/login.html',{'modellist':userinfoList})

'''注册界面功能'''
def registerSystem(request):
    return render(request,'login/regist.html')
