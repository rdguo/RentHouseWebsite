from django.shortcuts import render,redirect
from .models import LoginInfo,RegisterInfo
from django.http import HttpResponse
import json #用于数据交互

'''登录系统界面'''
def loginSystem(request):
    login_form = LoginInfo()
    if request.method == "POST": #当传递参数后 submit
        user_name = request.POST.get("username",None) #获得输入的用户名
        pass_word = request.POST.get("password",None)  #获得输入的密码
        if user_name and pass_word: #检查用户名和密码是否为空 (注册界面通过前端js来判断)
            try:  #要加try，不然查不到数据会报404错误
                user = LoginInfo.objects.get(username=user_name)
            except:
                flag_judge = "密码错误"
                return render(request,"register.html",{'errorinfo':flag_judge}) #查不到数据时候返回用户名不存在提示
            if user.password == pass_word:
                return redirect(mainPageSystem) #映射到登录成功界面
            else:#查不到数据时候返回密码错误提示
                return redirect(registerSystem)
    return render(request, 'login.html',{"login_form":login_form})

'''注册界面'''
def registerSystem(request):
    #先查数据库当中是否有数据、然后没有数据后再添加
    if request.method == "POST":
        ''' 获得相关数据 '''
        user_name = request.POST.get("username",None)
        pass_word = request.POST.get("password",None)
        gender = request.POST.get("gender",None)
        identify_number = request.POST.get("Id",None)
        address = request.POST.get("address",None)
        email = request.POST.get("Email",None)
        phone = request.POST.get("Phone",None)
        try:
            search_List = RegisterInfo.objects.get(username=user_name)
        except:
            #当没查到数据时.自动添加数据
            obj = RegisterInfo(username=user_name, password=pass_word, gender=gender, identifyid=identify_number,
                               address=address, email=email, phone=phone)
            obj.save()
            obj_Login = LoginInfo(username=user_name,password=pass_word)
            obj_Login.save()
            #返回注册成功界面
            return render(request, 'login.html')
        return HttpResponse(request,"注册失败提醒 当前存在该用户")
    return render(request, 'register.html')

'''主页面'''
def mainPageSystem(request):
    return render(request,'main.html')
