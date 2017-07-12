#!/usr/bin/python3
# -*- coding:utf8 -*-
import re

OldTxt = open("../../全部消息记录.txt","r+",encoding="utf-8")
TargetStr = input()
ReTargetStr = re.compile(("消息对象:.*?"+TargetStr+".*?")+"\n")
Txt= OldTxt.read()
TargetNum = Txt.index(ReTargetStr.findall(Txt)[0])

if TargetNum < 0:
    print("不存在目标记录")
else:
    print("TargetNum:" + str(TargetNum))
    TargetTxt = Txt[TargetNum:]
    TargetStrEnd = "=" * 64
    TargetNumStart = TargetTxt.index(TargetStrEnd)
    TargetNumEnd = TargetTxt[TargetNumStart+64:].index(TargetStrEnd)
    print("TargetNumStart:" + str(TargetNumStart))
    print("TargetNumEnd:" + str(TargetNumEnd))
    print(type(TargetTxt))
    TargetLog = TargetTxt[TargetNumStart+64:TargetNumEnd+TargetNumStart+64]
    fo = open("example.txt", "w")
    fo.write(TargetLog.encode("gbk","replace").decode("gbk"))
    fo.close()
    # print(TargetTxt)
# print(Txt)
