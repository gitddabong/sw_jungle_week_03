# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：2606_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-19 오후 5:46 
'''

import sys
from collections import deque

num_vertex = int(sys.stdin.readline())
num_edge = int(sys.stdin.readline())
graph = [[0]*(num_vertex+1) for _ in range(num_vertex+1)]

for _ in range(num_edge):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] =1

result = []

def bfs(start):
    visited = []
    queue = deque()
    queue.append(start)
    visited.append(start)

    while queue:
        now = queue.popleft()
        result.append(now)
        for i in range(len(graph[now])):
            if (i not in visited) and (graph[now][i] == 1):
                queue.append(i)
                visited.append(i)
bfs(1)
# print(result)
print(len(result)-1)
