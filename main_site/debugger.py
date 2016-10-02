# -*- coding: utf-8 -*-

import time
import datetime
from wechatInterface import WechatInterface

from datetime import timedelta, tzinfo

a = WechatInterface()

print a.deal_dogfood("b", "c", 'D', "E")

print a.deal_man("b", "c", 'D', "E")
print a.deal_morning("b", "c", 'D', "E")
print a.deal_tiaoxi("b", "c", 'D', "E")

class temp:
    def rock(self, music):
        return music

    def prin(self):
        return self.rock("sdf")

app = temp()

print app.prin()

print datetime.datetime.now()


ZERO_TIME_DELTA = timedelta(0)
LOCAL_TIME_DELTA = timedelta(hours=8)  # 本地时区偏差


class UTC(tzinfo):
    """实现了格林威治的tzinfo类"""

    def utcoffset(self, dt):
        return ZERO_TIME_DELTA

    def dst(self, dt):
        return ZERO_TIME_DELTA


class LocalTimezone(tzinfo):
    """实现北京时间的类"""

    def utcoffset(self, dt):
        return LOCAL_TIME_DELTA

    def dst(self, dt):
        return ZERO_TIME_DELTA

    def tzname(self, dt):  # tzname需要返回时区名
        return '+08:00'


print datetime.datetime.now(UTC())  # UTC时间  差八个小时
print datetime.datetime.now(LocalTimezone())  # 根据本地  时区 生成offset-aware类的datetime对象
print type(datetime.datetime.now(LocalTimezone()))

print datetime.datetime.now()  # 北京时间       一旦生成了一个offset-naive类型的datetime对象
print datetime.datetime.now().replace(tzinfo=UTC())  # 调用replace(tzinfo=UTC())即可转换成offset-aware类型

print datetime.datetime.now().replace(tzinfo=LocalTimezone()).astimezone(UTC())  # 时区转换，

print '----------------------------------------------'
print datetime.datetime.utcnow()
# 讲一个 已知时区的datetime类转换成UTC()的日期
datetime_test = datetime.datetime(2013, 10, 23, 20, 44, 11).replace(tzinfo=LocalTimezone()).astimezone(UTC())
print datetime_test
print '---------------------------------'
