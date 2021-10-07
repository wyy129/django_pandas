from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

# 用户信息数据库

# class UserInformation(models.Model):
#     userid = models.CharField(max_length=30, verbose_name='用户id', primary_key=True)
#     username = models.CharField(max_length=100, verbose_name='用户名')
#     password = models.CharField(max_length=100, verbose_name='密码')


# class User(AbstractUser):
#     '''定义用户模型类'''
#     mobile = models.CharField(max_length=11, unique=True, verbose_name="手机号")
#
#     class Meta:
#         db_table = 'tb_users'
#         verbose_name = '用户'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.username


# 传输信息数据库
class TransmitData(models.Model):
    data_id = models.CharField(max_length=30, verbose_name='数据id')
    data_x = models.CharField(max_length=30, verbose_name='数据x轴')
    data_y = models.CharField(max_length=30, verbose_name='数据y轴')
    labels = models.CharField(max_length=30, verbose_name='每条线的名称')
    filename = models.CharField(max_length=30, verbose_name='文件名')
    xticklabels = models.CharField(max_length=30, verbose_name='x轴文本替换')
    nrows = models.CharField(max_length=30, verbose_name='几行')
    ncpls = models.CharField(max_length=30, verbose_name='几列')
    ticks = models.CharField(max_length=30, verbose_name='x轴显示数据y轴显示数据[]')
    title = models.CharField(max_length=30, verbose_name='总名称坐标显示文字[x，y，title]，默认不显示')
    figsize = models.CharField(max_length=30, verbose_name='幕布大小，默认5*5 800px*800px')
    dpi = models.CharField(max_length=30, verbose_name='显示清晰度，默认80')
    linestyle = models.CharField(max_length=30, verbose_name='网格线，默认"--"')
    alpha = models.CharField(max_length=30, verbose_name='网格近明度，默认0.5')
