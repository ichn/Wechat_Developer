# 公众号开发日志

---

## 09.30

BlueMix大法吼！

转投IBM BlueMix，免费6个月，用了再说吧，到时不行了再迁移orz。

还真是蛋疼极了，延迟感人肺腑，BlueMix的console根本卡的不能用啊啊啊啊啊！！

使用python做后端理，本来打算上pHp，太懒orz。。

争取赶完工时，国庆后上线。

需要使用CloudFoundry和Bluemix CLI做command line interface

妈蛋，这什么龟速啊，2k/s，抓狂

妈蛋，连上vpn了，300k/s，爽啊，可惜只有后半夜可以连接，什么鬼免费方案啊。。

## 10.01

国庆节喵

<del>好想和妹子出去玩</del>

### 添加Token，通过接入验证

* 安装`web.py`
* 修改`server.py`
* 重写`main.py`
* 添加`index`做日志主页
* Token认证成功，成功接入

### 调戏(添加各种彩蛋)

* 添加沉默（不响应）
* 尝试“班对”有惊喜

## 10.02

### 添加数据库

* 如何使用MySQL进行管理？
* 如何设计数据库？迭代？是否能一步到位？
* 如何进行数据可视化？
  * 设计报表网页附在返回结果的后面
    * 连续早起多少日。。
    * 起床时间分析（折线图）

表单设计：

* `_id` 
* `name` 用户名，不知道支不支持unicode字符串，其实不是必要的，如果不直接人和人比较的话，只需要返回是早上第几个签到的即可，最多返回最早什么时候起床
* `wechat_id` 用户唯一标识符，由`POST`中过来的`fromUser`指定
* `eve_type` 先支持`morning`，即起床哒
* `eve_time` 签到时间，用整形存储

查询的JSON表单设计

* 查询一个用户所有的早起签到时间信息

  ```json
  {
    "selector": {
      "wechat_id": "sdfxcsdf2sdf1",
      "eve_type": "morning"
    },
    "fields": [
      "eve_time"
    ]
  }
  ```

* 没了。。就这么一个功能orz

* 其实还是有的，查询区间内的早起签到时间信息

  ```json
  {
    "selector": {
      "wechat_id": "sdfxcsdf2sdf1",
      "eve_type": "morning",
      "eve_time": {
        "$gt": 1475383784,
        "$lt": 1475383788
      }
    },
    "fields": [
      "eve_time"
    ]
  }
  ```

#### 发送POST请求，进行查询

放弃使用POST

询问了IBM的技术人员，直接使用`cloudant`模块中的`get_query_result`





### 解决时区问题

直接在UTC时间上加8个小时即可

datetime、time（时间戳）之间的互相转换

datetime用于表示时间，time用于存放在数据库中用于查询（可以方便地指定区间）

时间格式是`%Y-%m-%d %H:%M:%S`

```py
tstp = int(time.time())
# 获取时间戳
# 不需要毫秒的处理

dt = datetime.datetime.fromtimestamp(tstp)
# 时间戳转datetime

n_tstp = int(time.mktime(dt.timetuple()))
# datetime转时间戳
```

## 10.03

### 添加报表主页

## 10.12

发烧好些了，再来写代码。

## Reference

[Python学习之微信公众号接入 一 验证](https://my.oschina.net/bxxfighting/blog/388996)

[基于 IBM Bluemix 开发微信公共账号应用](http://www.ibm.com/developerworks/cn/cloud/library/cl-bluemix-weixin/)

[webpy新生指南](http://webpy.org/docs/0.3/tutorial.zh-cn)

[python time\datatime\string直接转换](http://blog.sina.com.cn/s/blog_684ae1750101kkid.html)

[Python时间，日期，时间戳之间转换](http://www.2cto.com/kf/201401/276088.html)

[Cloudant Documentation](https://docs.cloudant.com/index.html)