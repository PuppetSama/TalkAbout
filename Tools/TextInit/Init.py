#!/usr/bin/python3
#-*- coding:utf-8 -*-

import re
import csv

OldText = open("../TIMMessage/example.txt", "r+", encoding="gbk")
log = re.compile("(.*? .*?) (.*?)\\((.*?)\\)\n(.*?)\n")
NewText = log.findall(OldText.read())
# for NewLog in NewText:
#     print(NewLog[0]+NewLog[1]+NewLog[2]+NewLog[3])

Headers = ['Time', 'name', 'id', 'text']
Rows = NewText

with open('message.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(Headers)
    f_csv.writerows(Rows)
# print(OldText.read())