# -*- coding: utf-8 -*-
import datetime

from datetime import timedelta, tzinfo
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


def add_data(user, Time):
    print user, Time
    utc_time = datetime.datetime.now(UTC())
    pek_time = datetime.datetime.now(LocalTimezone())
    #print pek_time
    return u"现在时间是" + str(pek_time.day) + ' ' + str(pek_time.month) + ' ' + str(pek_time.hour) + ' ' + str(pek_time.minute) + ' ' + str(pek_time.second)

