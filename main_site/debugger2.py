# -*- coding: utf-8 -*-

import wechatInterface
import time
import ZaoqiNiao

A = wechatInterface.WechatInterface()

A.deal_morning('user', 'fwq', time.time(), 'good morning')
