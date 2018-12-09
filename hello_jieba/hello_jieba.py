# encoding=utf-8
import jieba

sentance = "看了那篇报道我感觉到不明觉厉"

seg_list = jieba.cut(sentance, cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut(sentance, cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut_for_search(sentance)  # 搜索引擎模式
print("Default Mode: " + "/ ".join(seg_list))

