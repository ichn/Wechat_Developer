# -*- coding: utf-8 -*-
import time
import datetime
import ZaoqiNiao

class Analysis:
    def __init__(self):
        self.zqn = ZaoqiNiao.zqn()
        self.daytime = datetime.datetime.fromtimestamp

    def to_dt(self, stamp):
        dt = datetime.datetime.fromtimestamp(stamp)
        return dt

    def to_delta(self, stamp):
        return stamp


    def is_next(self, a, b):
        a = a + datetime.timedelta(days=1)
        #print a,b
        if a.year == b.year and a.month == b.month and a.day == b.day:
            return True
        return False


    def GET(self, user):
        info = self.zqn.get_log(user)
        info.sort()
        info = map(self.to_delta, info)
        info = map(self.to_dt, info)

        k = 1

        for i in range(1, len(info)):
            if self.is_next(info[i-1], info[i]):
                k = k + 1
            else:
                break

        ret = u"您已经连续签到：" + str(k) + u"天\n以下是具体记录：\n"

        for s in info:
            ret += str(s) + "\n"

        return ret

