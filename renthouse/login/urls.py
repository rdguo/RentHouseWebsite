from django.urls import path
from . import views

urlpatterns = [
    path('login',views.loginSystem, name = 'loginSystem'), #登录界面
    path('register',views.registerSystem,name = 'registerSystem'), #注册用户信息
    path('mainPageSystem',views.mainPageSystem,name='mainPageSystem'), #主界面
]