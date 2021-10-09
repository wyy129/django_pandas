# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Send_mail.py
# @Author: 石振飞
# @Date  : 2021/9/25# @Desc  :

import yagmail

from szf_wy.setting import MAILUSER, PASSWORD, HOST


class Mail(object):

    def __init__(self):
        self.mail = yagmail.SMTP(user=MAILUSER, password=PASSWORD, host=HOST)

    def send(self, addressee, title, content):
        self.mail.send(addressee, title, content)
