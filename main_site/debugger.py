from wechatInterface import WechatInterface

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
