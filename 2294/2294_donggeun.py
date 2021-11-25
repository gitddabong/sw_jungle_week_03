# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：2294_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-22 오후 2:24 
'''

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
coins = set(int(sys.stdin.readline()) for _ in range(n))
check = [0 for _ in range(k+1)]

queue = deque()
for coin in coins:
    if coin > k:
        continue
    # queue : [coin, count]
    queue.append([coin, 1])
    check[coin]=1

flag = True
while queue:
    val , cnt = queue.popleft()
    if val == k:
        print(cnt)
        flag = False
        break

    for coin in coins:
        if val+coin > k:
            continue

        # print('val, coin, cnt', val,coin,cnt)
        # for i in range(k + 1):
        #     print('{0:02d}'.format(i), end=' ')
        # print()
        # for i in check:
        #     print('{0:02d}'.format(i), end=' ')
        # print()

        if check[val+coin] == 0:
            check[val+coin] = 1
            queue.append([val+coin, cnt+1])
