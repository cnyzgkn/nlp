# -*- coding: utf-8 -*-
import os, codecs
import jieba
import sys
import re
from collections import Counter
reload(sys)
sys.setdefaultencoding('utf8')
 
def get_words(txt):
    seg_list = jieba.cut(txt)
    c = Counter()
    for x in seg_list:
        if len(x)>1 and x != '\r\n': #词汇
            c[x] += 1
        else:
            if len(x) == 1: #单个汉字
                pattern = re.compile(u"[\u4e00-\u9fa5]+")
                resultWord = re.search(pattern, x)
                if resultWord != None:
                    c[x] += 1
    print('常用词频度统计结果')
    for (k,v) in c.most_common(1000):
        #print('%s%s %s  %d' % ('  '*(5-len(k)), k, '*'*int(v/3), v))
        print('词：' + k + ' 出现频率: ' + str(v))
 

if __name__ == '__main__':
    filename = u'唐宋汉魏六朝全诗词.txt'
    with codecs.open(filename, 'r', 'utf8') as f:
        txt = f.read()
    if txt[:3] == codecs.BOM_UTF8:
        txt = txt[3:]
    get_words(txt)