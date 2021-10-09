# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Line_chart.py
# @Author: 石振飞
# @Date  : 2021/9/25# @Desc  :


import os
import matplotlib.font_manager as mf  # 导入字体管理器
import matplotlib.pyplot as plt
from szf_wy.setting import PATH, ADDRESSEE
from szf_wy.Mailbox_package.Send_mail import Mail


class Broken_line(object):

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

    def Determine_operated(self):
        if os.path.exists(PATH + self.username):
            pass
        else:
            os.makedirs(PATH + self.username)

    def one_nrows(self):
        for i in range(0, len(self.data)):
            # 绘制图像
            self.axes.plot(self.data[i][0], self.data[i][1], label=self.data[i][2])

        # 显示图例
        self.axes.legend(loc=1)

        # xy轴显示文本设置
        if self.ticks:
            self.axes.set_xticks(self.ticks[0])
            if self.xticklabels:
                self.axes.set_xticklabels(self.xticklabels)
            self.axes.set_yticks(self.ticks[1])

        # 网格设置
        self.axes.grid(linestyle=self.linestyle, alpha=self.alpha)

        # 控制显示说明文本
        if self.title:
            self.axes.set_xlabel(self.title[0])
            self.axes.set_ylabel(self.title[1])
            self.axes.set_title(self.title[2])
        plt.savefig(PATH + self.username + "/" + self.filename + ".png")

    def run(self):
        self.Determine_operated()
        try:
            self.one_nrows()
            return True
        except Exception as e:
            # 如果错误则发送邮件
            content = str(e) + "\n" + """
                            username:{},
                            x={},
                            y={},
                            labels={},
                            filename={},
                            xticklabels={},
                            nrows={},
                            ncpls={},
                            ticks={},
                            title={},
                            figsize={},
                            dpi={},
                            grid={},
                            linestyle={},
                            alpha={}
                            """.format(
                self.username, self.x, self.y, self.labels, self.filename,
                self.xticklabels, self.nrows, self.ncols, self.ticks, self.title,
                self.figsize, self.dpi, self.grid, self.linestyle, self.alpha
            )
            self.mail.send(ADDRESSEE, "错误报告", content=content)
            return False
