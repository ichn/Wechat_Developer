# -*- coding: utf-8 -*-
import Image

f = Image.open(u'C:\\Users\\胡志峰\\Pictures\\yande.re\\少女\\girl.png')

s = f.split()

for i in range(0, 3):
    s[i].save(u'C:\\Users\\胡志峰\\Pictures\\yande.re\\少女\\' + str(i) + u'.png')
