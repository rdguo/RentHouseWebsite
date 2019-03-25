from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login',views.loginSystem, name = 'loginSystem'),
    path('indexman',views.indexman,name = 'indexman'),
    path('register',views.registerSystem,name = 'registerSystem') #注册用户信息
]