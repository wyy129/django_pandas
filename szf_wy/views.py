import json
import re

from django import http
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect


# 类视图完成登录功能
# class LoginClassViews(View):
#     def get(self, request):
#         return render(request, 'login.html')
#
#     def post(self, request):
#         """
#                         实现登录逻辑
#                         :param request: 请求对象
#                         :return: 登录结果
#                         """
#         # 接受参数
#         # username = request.POST.get('username')
#         # password = request.POST.get('password')
#         # 接受json
#         json_data = json.loads(request.body)
#         username = json_data['username']
#         password = json_data['password']
#
#         # remembered = request.POST.get('remembered')
#
#         # 校验参数
#         # 判断参数是否齐全
#         if not all([username, password]):
#             return http.HttpResponseForbidden('缺少必传参数')
#
#         # 判断用户名是否是5-20个字符
#         if not re.match(r'^[a-zA-Z0-9_-]{5,20}$', username):
#             return http.HttpResponseForbidden('请输入正确的用户名或手机号')
#
#         # 判断密码是否是8-20个数字
#         if not re.match(r'^[0-9A-Za-z]{8,20}$', password):
#             return http.HttpResponseForbidden('密码最少8位，最长20位')
#
#         # 认证登录用户
#         user = authenticate(username=username, password=password)
#         if user is None:
#             # 登录失败 返回错误信息
#             return JsonResponse({"msg": 0})
#
#         # 实现状态保持
#         # login(request, user)
#         # 设置状态保持的周期
#         # if remembered != 'on':
#         #     # 没有记住用户：浏览器会话结束就过期
#         #     request.session.set_expiry(0)
#         # else:
#         #     # 记住用户：None表示两周后过期
#         #     request.session.set_expiry(None)
#
#         # 响应登录结果
#         return JsonResponse({"msg": 1, "url": "http://127.0.0.1:8000/index"})
from django.urls import reverse


def transmit_data(request):
    json_data = json.loads(request.body.decode('utf-8'))
    print(json_data)
    return HttpResponse('{"name":"ok"}')


def index(request):
    if request.method == "GET":
        # try:
        #     user.is_authenticated
        # except Exception as e:
        #     print(e)
        #     return HttpResponseRedirect("/login")
        try:
            username = request.session.get("username")
        except:
            username=None
        if username == None:
            return HttpResponseRedirect("login")
        else:
            return render(request,"index.html")

        # return HttpResponse("hello world")


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
        # return render(request, "注册界面")
    elif request.method == "POST":

        # 前端可以利用ajax异步请求 判断用户名字是否被注册过
        # -------------------注册查询--------------------
        json_data = json.loads(request.body)
        username = json_data['username']
        password = json_data['password']
        again = json_data['again']

        if username == "":
            return JsonResponse({"msg": 0})
        if password == again:
            user = User.objects.create_user(username=username, password=password)
            login(request, user, backend=None)
            return JsonResponse({"msg": 1, "url": "http://127.0.0.1:8000/index"})


def login_in(request):
    if request.method == "GET":
        return render(request, 'login.html')
        # return render(request, "注册界面")
    elif request.method == "POST":
        """
                实现登录逻辑
                :param request: 请求对象
                :return: 登录结果
                """
        # 接受json
        json_data = json.loads(request.body)
        username = json_data['username']
        password = json_data['password']
        # remembered = json_data['remembered']
        # 校验参数
        # 判断参数是否齐全
        if not all([username, password]):
            return http.HttpResponseForbidden('缺少必传参数')

        # 判断用户名是否是5-20个字符
        if not re.match(r'^[a-zA-Z0-9_-]{5,20}$', username):
            return http.HttpResponseForbidden('请输入正确的用户名或手机号')

        # 判断密码是否是8-20个数字
        if not re.match(r'^[0-9A-Za-z]{8,20}$', password):
            return http.HttpResponseForbidden('密码最少8位，最长20位')

        # 认证登录用户
        user = authenticate(username=username, password=password)
        if user is None:
            # 登录失败 返回错误信息
            return JsonResponse({"msg": 0})

        # 实现状态保持
        # login(request, user)
        # 设置状态保持的周期
        # if remembered != 'on':
        #     # 没有记住用户：浏览器会话结束就过期
        #     request.session.set_expiry(0)
        # else:
        #     # 记住用户：None表示两周后过期
        #     request.session.set_expiry(None)

        # 响应登录结果
        request.session['username'] = username
        return JsonResponse({"msg": 1, "url": "http://127.0.0.1:8000/index"})
