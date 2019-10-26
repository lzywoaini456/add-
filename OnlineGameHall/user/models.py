from django.db import models

# Create your models here.


class User(models.Model):
    u_name = models.CharField(max_length=20, verbose_name='用户名', unique=True)
    u_pass = models.CharField(max_length=40, verbose_name='密码')
    u_email = models.EmailField(max_length=20, verbose_name='邮箱')
    u_vip = models.BooleanField(default=False, verbose_name='会员')
    u_bank = models.DecimalField(max_digits=10, default=0, decimal_places=0, verbose_name='账户余额')
    u_create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    u_mod_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
