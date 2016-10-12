# coding: UTF-8
import os
import web
from wechatInterface import WechatInterface
from index import Index
from analysis import Analysis

urls = (
    '/', 'Index',
    '/wechat-ichn', 'WechatInterface',
    '/report/([a-zA-Z0-9\-\_]+)', 'Analysis'
)


if __name__ == "__main__":
    app_root = os.path.dirname(__file__)
    templates_root = os.path.join(app_root, 'templates')
    render = web.template.render(templates_root)

    app = web.application(urls, globals())
    #web.httpserver.runsimple(app.wsgifunc(), ('127.0.0.1', 8000))


    app.run()
