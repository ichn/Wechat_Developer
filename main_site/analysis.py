
import time
import datetime
import ZaoqiNiao

class Analysis:
    def __init__(self):
        self.zqn = ZaoqiNiao.zqn()

    def to_dt(self, stamp):
        dt = datetime.datetime.fromtimestamp(stamp)
        return dt

    def to_delta(self, stamp):
        return stamp - 28800

    def GET(self, user):
        info = self.zqn.get_log(user)
        info.sort()
        info = map(self.to_delta, info)
        info = map(self.to_dt, info)

        ret = u""

        for s in info:
            ret += str(s) + "\n"

        return ret

