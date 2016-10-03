# -*- coding: utf-8 -*-
import datetime
import time
import ZQN_db

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



class zqn:
    def __init__(self):
        self.zqn_db = ZQN_db.zqn_db()

    def has_log(self, user, Time):
        dt = datetime.datetime.fromtimestamp(Time)
        at = datetime.datetime(dt.year, dt.month, dt.day, 3, 59, 0, 0)
        bt = datetime.datetime(dt.year, dt.month, dt.day, 10, 1, 0, 0)
        a = int(time.mktime(at.timetuple()))
        b = int(time.mktime(bt.timetuple()))
        log = self.zqn_db.q_by_id_itv(user, a, b)
        if len(log) == 0:
            return False
        return True

    def num_log(self, Time):
        dt = datetime.datetime.fromtimestamp(Time)
        at = datetime.datetime(dt.year, dt.month, dt.day, 4, 29, 0, 0)
        bt = datetime.datetime(dt.year, dt.month, dt.day, 10, 1, 0, 0)
        a = int(time.mktime(at.timetuple()))
        b = int(time.mktime(bt.timetuple()))
        res = self.zqn_db.q_by_itv(a, b)
        return len(res)

    def get_url(self, user):
        return u"嘛，这个还在开发，请关注开发日志http://wechat-ichn.eu-gb.mybluemix.net/"

    def get_log(self, user):
        res = self.zqn_db.q_by_id(user)
        return res

    def add_data(self, user):
        # print user, Time
        #utc_time = datetime.datetime.now(UTC())
        pek_time = datetime.datetime.now(LocalTimezone())
        pek_stamp = int(time.mktime(pek_time.timetuple()))

        if pek_time.hour < 4:
            return u"这么早就来了？你还没睡吧魂淡！！怎么可以这样伤害自己的身体，宝宝心疼你啊\n"
        if pek_time.hour > 8:
            return u"喂，一觉睡到这个时候你也敢说早上好？？明天早点来吧\n^_^"
        if self.has_log(user, pek_stamp):
            return u"似乎你今天已经问安过了呢，我可以把这视为调戏吗？\nQwQ"
        #print pek_time

        num = self.num_log(pek_stamp) + 1
        self.zqn_db.add_eve("noname", user, "morning", pek_stamp, num)
        return u"早上好哇^*^\n你是今天第"+str(num)+u"个签到的哦，厉害呢，继续保持，早早起床哦\n现在时间是"\
                + str(pek_time.month) + u'月 ' + str(pek_time.day) + u'日 '\
                + str(pek_time.hour) + u'时 '\
                + str(pek_time.minute) + u'分 '\
                + str(pek_time.second) + u'秒' + u"\n去开始你新的一天吧！\n查看我的签到记录：" + self.get_url(user)

