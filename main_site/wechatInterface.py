# -*- coding: utf-8 -*-
import hashlib
import os
import time

import web
from lxml import etree


class WechatInterface:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        # 获取输入参数
        data = web.input()
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        return echostr
        # 自己的token
        token = "TokenizerIchn"  # 这里改写你在微信公众平台里输入的token
        # 字典序排序
        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        # sha1加密算法

        # 如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr

    def chk_man(self, content):
        if u"manual" in content:
            return True
        if u"help" == content:
            return True
        if u"会些什么" in content:
            return True
        if u"man" == content:
            return True
        if u"有些什么功能" in content:
            return True
        if u"功能" in content:
            return True
        return False

    def deal_man(self, fromUser, toUser, time, content):
        reply = u"欢迎使用本公众号的服务功能！\n我们已有的服务有：\n1. 早起鸟(under developing)\n2. 各种彩蛋(如吃狗粮)"
        return self.render.reply_text(fromUser, toUser, time, reply)

    def chk_dogfood(self, content):
        if u"狗粮" in content:
            return True
        return False

    def deal_dogfood(self, fromUser, toUser, time, content):
        dogfood_list = []

    def chk_music(self, content):
        if u"听歌" in content:
            return True
        if u"音乐" in content:
            return True
        return False

    def chk_my_lover(self, content):
        if u"最爱的钢琴曲" in content:
            return True

    def chk_morning(self, content):
        if u"早上好" in content:
            return True
        if u"早安" in content:
            return True
        return False

    def deal_morning(self, content, msgType, fromUser, toUser, msgTime):


    def chk_tiaoxi(self, content):
        if u"调戏" in content:
            return True
        return False

    def getReply(self, content, msgType, fromUser, toUser, msgTime):
        if self.chk_tiaoxi(content=content):
            return u"讨厌嘛，别调戏人家啦，看看坏叔叔在干什么吧：http://wechat-ichn.eu-gb.mybluemix.net/"
        if self.chk_morning(content=content):
            self.deal_morning(self, content, msgType, fromUser, toUser, msgTime)
        return u"此功能还在开发中，对不起，你刚才说的是\n" + content + u"\n发送时间是：" + str(time.asctime( time.localtime(time.time()) ))


    def POST(self):
        str_xml = web.data()  # 获得post来的数据
        xml = etree.fromstring(str_xml)  # 进行XML解析
        content = xml.find("Content").text  # 获得用户所输入的内容
        msgType = xml.find("MsgType").text # 目前只处理text消息
        fromUser = xml.find("FromUserName").text
        toUser = xml.find("ToUserName").text
        msgTime = xml.find("CreateTime").text

        if self.chk_man(self, content):
            return self.deal_man(self, fromUser, toUser, int(time.time()), content)

        if self.chk_dogfood(self, content):
            return self.deal_dogfood(self, fromUser, toUser, int(time.time()), content)

        return "success"


        return self.render.reply_text(fromUser, toUser, int(time.time()), self.getReply(content, msgType, fromUser, toUser, msgTime))
