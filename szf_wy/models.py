from django.db import models


# (self, username,
# x,
# y,
# Labels
# , filename,
# xticklabels = False
# , nrous-l
# , neplsl,
# ticks-false,
# title-False,
# figsize=(10, 10),
# dpi-80,
# grid-True,
# Linestye=".",
# alpha=-.5)

# Create your models here.

# 用户信息数据库
class UserInformation(models.Model):
    userid = models.CharField(max_length=30, verbose_name='用户id')
    username = models.CharField(max_length=100, verbose_name='用户名')
    password = models.CharField(max_length=100, verbose_name='密码')


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
