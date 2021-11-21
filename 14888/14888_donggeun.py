# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：14888_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-20 오후 6:54 
'''

import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())

max_ = float('-inf')
min_ = float('inf')
def dfs(i, res, add, sub, mul, div):
    global max_, min_

    if i == n:
        max_ = max(res, max_)
        min_ = min(res, min_)
        return
    else:
        if add:
            dfs(i+1, res+num_list[i], add-1, sub, mul, div)
        if sub:
            dfs(i + 1, res - num_list[i], add , sub- 1, mul, div)
        if mul:
            dfs(i + 1, res * num_list[i], add , sub, mul- 1, div)
        if div:
            dfs(i+1, int( res / num_list[i]), add, sub, mul, div-1)

dfs(1, num_list[0], add, sub, mul, div)
print(max_)
print(min_)