from django.db import models
#from django import forms #用于使用表单功能
# Create your models here.
# 用于创建数据库类型

#创建登录信息数据类型(包含用户名和密码)
class LoginInfo(models.Model):
    username = models.CharField(max_length=20 , primary_key=True) #设置主键
    password = models.CharField(max_length=30)


#注册信息数据库
class RegisterInfo(models.Model):
    username = models.CharField(max_length=20,primary_key=True) #用户名/手机号
    password = models.CharField(max_length=20) #密码
    gender_choice = (
        ('male', '男'),
        ('female', "女")
    )
    gender = models.CharField(max_length=6,choices=gender_choice)#性别
    identifyid = models.CharField(max_length=18)#身份证 18位
    address = models.CharField(max_length=30)#邮箱地址
    email = models.CharField(max_length=20)#email邮件
    phone = models.CharField(max_length=11)#联系电话






