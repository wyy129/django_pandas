# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Histogram.py
# @Author: 石振飞
# @Date  : 2021/9/26# @Desc  :


from szf_wy.Visualization_package.Line_chart import Broken_line
from szf_wy.Mailbox_package.Send_mail import Mail
import matplotlib.font_manager as mf  # 导入字体管理器
import matplotlib.pyplot as plt
from szf_wy.setting import PATH


class Histogram(Broken_line):

    def __init__(self, username, data, filename, xticklabels=False, nrows=1, ncpls=1, ticks=False, title=False,
                 figsize=(10, 10), dpi=80, grid=True, linestyle="--", alpha=0.5):
        """
        :param username: 用户名
        :param data: data轴数据 [[], []]
        :param xticklabels: x轴文本替换
        :param filename: 文件名
        :param nrows: 几行
        :param ncpls: 几列
        :param ticks: x轴显示数据 y轴显示数据 []
        :param title: 总名称 坐标显示文字 [x , y, title], 默认不显示
        :param figsize: 幕布大小, 默认5 * 5   800px * 800px
        :param dpi: 显示清晰度, 默认80
        :param grid: 图像网格, 默认显示
        :param linestyle: 网格线, 默认"--"
        :param alpha: 网格透明度, 默认0.5
        """
        # 创建邮箱对象
        self.mail = Mail()
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        my_font = mf.FontProperties(fname='C:\\Windows\\Fonts\\simkai.ttf')
        self.username = username
        self.data = data
        self.title = title
        self.filename = filename
        self.xticklabels = xticklabels
        self.ticks = ticks
        self.title = title
        self.figsize = figsize
        self.dpi = dpi
        self.grid = grid
        self.linestyle = linestyle
        self.alpha = alpha
        self.nrows = nrows
        self.ncols = ncpls
        # 创建画布
        self.figure, self.axes = plt.subplots(nrows=self.nrows, ncols=self.ncols, figsize=self.figsize, dpi=self.dpi)

    def one_nrows(self):
        n = 0
        for i in range(0, len(self.data)):
            print(i)
            print(self.data[i][0])
            if n == 0:
                self.axes.bar([n+1 - 0.1 for n in range(len(self.data[i])+1)], self.data[i][0], width=0.2, label=self.data[i][1])
            else:
                self.axes.bar([n + 1 + 0.1 for n in range(len(self.data[i]) + 1)], self.data[i][0], width=0.2,
                              label=self.data[i][1])
            n += 1

        # 显示图例
        self.axes.legend(loc=1)
        if self.xticklabels:
            self.axes.set_xticks([i for i in range(1, len(self.xticklabels) + 1)])
            self.axes.set_xticklabels(self.xticklabels)


        self.axes.grid(linestyle=self.linestyle, alpha=self.alpha)
        if self.title:
            self.axes.set_xlabel(self.title[0])
            self.axes.set_ylabel(self.title[1])
            self.axes.set_title(self.title[2])

        plt.savefig(PATH + self.username + "/" + self.filename + ".png")

    def run(self):
        self.Determine_operated()
        self.one_nrows()

if __name__ == '__main__':
    username = "2919390584"
    movie_name = ['雷神3：诸神黄昏', '正义联盟', '寻梦环游记']

    first_day = [10587.6, 10062.5, 1275.7]
    first_weekend = [36224.9, 34479.6, 11830]
    data = [[first_day, "首日票房"], [first_weekend, "首周票房"]]
    print(data)

    filename = "石振飞柱状图"
    xticklabels = movie_name
    H = Histogram(username=username, data=data, filename=filename, xticklabels=xticklabels)
    H.run()
