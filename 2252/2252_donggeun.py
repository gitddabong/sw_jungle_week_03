# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：2252_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-22 오후 5:09 
'''

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    # a->b
    arr[a].append(b)
    # indegree of b ++
    indegree[b] +=1

queue = deque()

for i in range(1, len(indegree)):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    if arr[now]:
        for i in range(len(arr[now])):
            indegree[arr[now][i]] -=1
            if indegree[arr[now][i]] == 0:
                queue.append(arr[now][i])

    print(now, end=' ')