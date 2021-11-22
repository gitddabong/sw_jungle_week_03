# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：2637_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-22 오후 5:27 
'''

"""
    기본 부품 1~N-1 중 여러 개 일 수 있음
"""


import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = [{} for _ in range(n+1)]
for _ in range(m):
    x,y,k = map(int, sys.stdin.readline().split())
    arr[x][y] = k
print(arr)

# total = [0 for _ in range(n+1)]
# total[n] = 1
# print(total)
primary = [0,0,0,0,0]

queue = deque()
queue.append(n)

while queue:
    now = queue.popleft()

    # key is parts
    for key in arr[now].keys():
        if key < 5:
            primary[key]+=arr[now][key]
        else:
            for i in range(arr[now][key]):
                queue.append(key)


for i in range(1, len(primary)):
    print(i, primary[i])