from django.shortcuts import render,redirect
from .models import LoginInfo
# Create your views here.
from django.http import HttpResponse

#测试用例
def index(request):
    return HttpResponse("Hello, world. ") #test

def indexman(request):
    return HttpResponse("Hello, world. ss") #test

def loginSystem(request):
    modellist = LoginInfo.objects.all()
    if request.method == "POST":
        user_name = request.POST.get("login_name",None) #获得用户名
        pass_word = request.POST.get("login_pwd",None)  #获得密码
        save_obj = LoginInfo(username = user_name,password= pass_word) #添加到数据库当中
        save_obj.save()
        if user_name == "123" and pass_word == "123":
            return redirect('index',{'modellist':modellist})
        else:
            return redirect("indexman")
    return render(request,'login/login.html',{'modellist':modellist})
