# -*- coding: utf-8 -*-
import os, codecs
import jieba
import sys
import re
from collections import Counter
reload(sys)
sys.setdefaultencoding('utf8')

def get_keyword_context(keywordList, txt):
    seg_list = jieba.cut(txt)
    lenTxt = len(txt)
    for keyword in keywordList:
        print '\n' + '\n' + u'  关键字:   ' + keyword + u' 的上下文是：'
        count = 1
        for m in re.finditer(keyword, txt):
            beginIndex = 0
            if (m.start()-20) < 0:
                beginIndex = 0
            else :
                beginIndex = (m.start()-20)
            endIndex = lenTxt
            if (m.end()+20) > lenTxt:
                endIndex = lenTxt
            else :
                endIndex = (m.end()+20)
            print u'第' + str(count) + u'篇:   ' + txt[beginIndex:endIndex] + '\n'
            count = count+1

 
def get_keywords(txt):
    pattern = re.compile(u"[\u4e00-\u9fa5]+")
    keywordList = re.findall(pattern, txt)
    resultKeywordList = []
    for keyword in keywordList:
        if(keyword != u'出现频率' and keyword != u'词'):
            resultKeywordList.append(keyword)
    return resultKeywordList

if __name__ == '__main__':
    classifyingFilename = u'人教版诗词分类.txt'
    with codecs.open(classifyingFilename, 'r', 'utf8') as f:
        classifyingTxt = f.read()
    if classifyingTxt[:3] == codecs.BOM_UTF8:
        classifyingTxt = classifyingTxt[3:]
    keywordList = get_keywords(classifyingTxt)

    txtFilename = u'汉魏六朝诗选.txt'
    with codecs.open(txtFilename, 'r', 'utf8') as f:
        txt = f.read()
    if txt[:3] == codecs.BOM_UTF8:
        txt = txt[3:]
    get_keyword_context(keywordList, txt)

