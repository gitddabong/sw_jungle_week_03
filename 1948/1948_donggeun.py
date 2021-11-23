# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：1948_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-23 오후 5:07 
'''

import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
in_degree = [0] * (n+1)
out_degree = [0] * (n+1)
arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    in_degree[b]+=1
    out_degree[a]+=1
    arr[a].append([b,c])

start, end = map(int, sys.stdin.readline().split())

for i in arr:
    print(i)
print('in', in_degree)
print('out',out_degree)

q = deque()
q.append(start)

while q:
    now = q.popleft()

    for i in arr[now]:
        print(i[0])
        in_degree[i[0]] -= 1
print(in_degree)