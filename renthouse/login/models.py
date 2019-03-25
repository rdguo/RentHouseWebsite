from django.db import models
# Create your models here.
# 用于创建数据库类型

#创建登录信息数据类型(包含用户名和密码)
class LoginInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
