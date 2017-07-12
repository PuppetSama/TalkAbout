#!/usr/bin/python3
#-*- coding:utf-8 -*-

from wordcloud import WordCloud
import csv
import matplotlib.pyplot as plt
import jieba
from os import path
import numpy as np
from PIL import Image

allText = ''
with open("../TextInit/message.csv","r") as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        if row:
            text = ''.join(row[3])
            allText = text + allText
        else:
            continue
allText = allText.replace("表情", " ")
allText = allText.replace("图片", " ")
# print(type(allText))
# allText = allText.encode("gbk", "ignore").decode("utf-8")
d = path.dirname(__file__)
cut_text = " ".join(jieba.cut(allText))
# color_mask = plt.imread("sphx_glr_masked_002.png") # 读取背景图片
alice_mask = np.array(Image.open(path.join(d, "sphx_glr_masked_002.png")))
wordCloud = WordCloud(#设置字体，不指定就会出现乱码
        font_path="HYQiHei-25J.ttf",
        #font_path=path.join(d,'simsun.ttc'),
        #设置背景色
        background_color='white',
        #词云形状
        mask=alice_mask,
        #允许最大词汇
        max_words=200,
        #最大号字体
        max_font_size=40).generate(cut_text)
plt.imshow(wordCloud, interpolation='bilinear')
plt.axis("off")

wordcloud = WordCloud(font_path="HYQiHei-25J.ttf",max_font_size=40).generate(cut_text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


