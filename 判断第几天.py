#!/usr/bin/python3
# 输入某年某月某日，判断这一天是这一年的第几天？
import time

year = input('year:\n')
month = input('month:\n')
day = input('day:\n')
print(time.strptime(year + '-' + month + '-' + day, '%Y-%m-%d')[7])
