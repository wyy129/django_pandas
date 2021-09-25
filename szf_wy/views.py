import json
import os

import matplotlib.font_manager as mf  # 导入字体管理器
import matplotlib.pyplot as plt
import yagmail
from django.http import HttpResponse


# from setting import MAIL_USER, MAIL_PASSWORD, HOST


class mail():

    def __init__(self):
        self.mail = yagmail.SMTP(user="1104774861@qq.com", password="zvwdvlyatexqjaah", host="imap.qq.com")

    def send(self, addressee, title, content):
        self.mail.send(addressee, title, content)


class Broken_line(object):

    def __init__(self, username, x, y, labels, filename, xticklabels=False, nrows=1, ncpls=1, ticks=False, title=False,
                 figsize=(10, 10), dpi=80, grid=True, linestyle="--", alpha=0.5):
        """
        :param username: 用户名
        :param x: x轴数据 [[], []]
        :param y: y轴数据 [[],[]]
        :param labels: 每条线的名称[[[],[]],[[],[]]]
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
        self.mail = mail()
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        my_font = mf.FontProperties(fname='C:\\Windows\\Fonts\\simkai.ttf')
        self.username = username
        self.x = x
        self.y = y
        self.labels = labels
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
        if os.path.exists("./static/" + self.username):
            pass
        else:
            os.makedirs("./static/" + self.username)

    def one_nrows(self):
        for i in range(0, len(self.x)):
            # 绘制图像
            self.axes.plot(self.x[i], self.y[i], label=self.labels[i])

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
        plt.savefig("./static/" + self.username + "/" + self.filename + ".png")

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
            self.mail.send("291882490@qq.com", "错误报告", content=content)
            return False


# Create your views here.

def transmit_data(request):
    # B = Broken_line(username="2919390584",
    #                 x= [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59],[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59],[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]],
    #                 y=[[2.1716765124419353, 1.2753878665548566, 1.664349215451173, 2.8722178908537757, 1.1712986065080178, 1.2362492358733252, 1.315869572506008, 2.643535982827691, 2.980558398305921, 1.4039643318061001, 2.4429603978822385, 2.44240834786157, 2.0906080644534795, 1.369232352454059, 2.100606884384744, 2.784385764797928, 1.1329178418839407, 2.760800770153545, 2.638141718870503, 2.620904252521685, 2.4389215739505614, 1.6960975603285686, 2.3208680765549885, 2.2999912679334242, 1.6387491359581443, 2.623554528611743, 1.7275062884967507, 2.4269440160210127, 1.4412760715692097, 2.205190363880507, 1.6315854166696644, 1.6818850138880048, 2.030033038538186, 1.1980187307924928, 1.7919857494782163, 2.2606397244546006, 2.9224459880377918, 1.4124970606514902, 2.3521380700389845, 2.287381075198042, 1.8601442142668962, 1.5933032813023693, 1.0520027101152676, 2.050305701506441, 2.454258031468626, 2.641629685114168, 1.7582308594186973, 2.5008125339768124, 1.3296540206756198, 1.3541369608022145, 2.501813689727544, 1.0166863599887876, 2.9849511545439853, 2.601624352195212, 2.057231673962829, 1.1632774976917646, 2.56446021506952, 2.111391772326219, 2.4262888449599744, 2.836985658238297],[17.361770236629074, 15.383372791196544, 15.946680326412645, 17.44732020886358, 16.9445377518053, 16.73344916288427, 17.05256923068533, 15.435679968142866, 17.340717439142278, 15.71642407499532, 17.04713978624761, 17.17378823734204, 15.085902049936625, 15.988959446173892, 15.090166882425612, 16.985566779605204, 15.347373650936778, 15.023832923087348, 15.712110804686144, 16.49079274972557, 15.034186112810906, 16.955459190251855, 16.6583382371455, 15.186105824283661, 16.728796984702896, 16.438052372656678, 16.123447274625715, 16.07958442048081, 16.181167936899968, 16.45969240349799, 16.563603134991727, 16.209734446709422, 16.440787251668432, 16.913586073158843, 16.24655059321099, 17.990180068458322, 15.846959184329453, 16.46862656085146, 16.242009702118832, 17.91483375988142, 16.94901148721644, 16.292724265499537, 16.692653859564874, 16.75371974805062, 15.575154385402897, 15.575930875442534, 17.74296202886289, 17.67933660872911, 16.91241425854377, 15.502114955389404, 15.172262707927887, 15.927318858438111, 16.08679489188968, 16.644157051476682, 15.139543662620436, 15.237426144863788, 16.9398648560103, 16.070009229035193, 17.826229585065345, 17.876228363539674],[31.986167446224226, 34.09861567417831, 31.55325504667923, 31.42856637956291, 34.26383420325176, 30.250628857335798, 34.034369161230984, 34.081405901586756, 33.758572728875016, 34.63503846155025, 30.928322537028286, 31.401408204243992, 33.94926979671511, 34.01392052946498, 30.915417786933098, 33.28208311796832, 30.192065699445227, 30.189468227255425, 33.62653014493876, 32.60673996858919, 33.53438943389118, 34.516435999416146, 32.88204593592504, 34.570754040447845, 32.786809786793434, 32.91272786724007, 31.506205860594253, 33.82914230874799, 34.877874201403316, 32.59135823771614, 31.185180802090514, 31.6219064928731, 31.41670054608206, 34.29156868065555, 30.562602387696376, 32.346091774444, 30.23751025724763, 30.68508333805951, 32.52054855338396, 30.68412748750813, 30.517866457727912, 31.14152379284141, 34.64161490635494, 34.894140986492324, 31.87003704067456, 31.009677185681337, 34.699810712631624, 30.279589475726215, 31.732083812884966, 32.60468748546401, 32.15329073334478, 33.614143297295, 33.185842884310674, 31.67444738286974, 33.90685987272336, 33.747033605556084, 31.825361811748042, 34.137647935579416, 32.803905206581, 31.336016721395744]],
    #                 labels=["北京", "上海", "石家庄"],
    #                 filename="石振飞",
    #                 title=["时间变化", "温度变化", "北京,上海,石家庄温度变化图"]
    #                 )
    # json_data = json.loads(request.body)
    # print(json_data)
    # username = "username"
    # username = json_data[username]
    # print(username)

    json_data = json.loads(request.body.decode('utf-8'))
    print(json_data)
    return HttpResponse('{"name":"ok"}')


def login(request):
    "你好 szf"
    pass
