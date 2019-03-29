from django.contrib import admin
from .models import LoginInfo,RegisterInfo

# Register your models here.
# 注册数据模型
admin.site.register(LoginInfo)
admin.site.register(RegisterInfo)