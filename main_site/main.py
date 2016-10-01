# coding: UTF-8
import os
import web
from wechatInterface import WechatInterface
from index import Index

urls = (
    '/', 'Index',
    '/wechat-ichn', 'WechatInterface'
)


if __name__ == "__main__":
    app_root = os.path.dirname(__file__)
    templates_root = os.path.join(app_root, 'templates')
    render = web.template.render(templates_root)

    app = web.application(urls, globals())
    app.run()
