# Generated by Django 3.2.7 on 2021-10-06 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransmitData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.CharField(max_length=30, verbose_name='数据id')),
                ('data_x', models.CharField(max_length=30, verbose_name='数据x轴')),
                ('data_y', models.CharField(max_length=30, verbose_name='数据y轴')),
                ('labels', models.CharField(max_length=30, verbose_name='每条线的名称')),
                ('filename', models.CharField(max_length=30, verbose_name='文件名')),
                ('xticklabels', models.CharField(max_length=30, verbose_name='x轴文本替换')),
                ('nrows', models.CharField(max_length=30, verbose_name='几行')),
                ('ncpls', models.CharField(max_length=30, verbose_name='几列')),
                ('ticks', models.CharField(max_length=30, verbose_name='x轴显示数据y轴显示数据[]')),
                ('title', models.CharField(max_length=30, verbose_name='总名称坐标显示文字[x，y，title]，默认不显示')),
                ('figsize', models.CharField(max_length=30, verbose_name='幕布大小，默认5*5 800px*800px')),
                ('dpi', models.CharField(max_length=30, verbose_name='显示清晰度，默认80')),
                ('linestyle', models.CharField(max_length=30, verbose_name='网格线，默认"--"')),
                ('alpha', models.CharField(max_length=30, verbose_name='网格近明度，默认0.5')),
            ],
        ),
    ]
