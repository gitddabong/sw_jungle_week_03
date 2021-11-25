# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：18405_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-25 오전 10:00 
'''

import heapq
import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())
arr = []
q = []
result = [[0] * (n) for _ in range(n)]

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if temp[j] != 0:
            result[i][j] = temp[j]
            heapq.heappush(q, [temp[j], i, j])

seconds, target_x, target_y = map(int, sys.stdin.readline().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(seconds):
    virus_arr = []
    while q :
        now = heapq.heappop(q)
        virus ,x,y = now[0],now[1],now[2]

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0<= nx < n and 0<=ny < n:
                if result[nx][ny] == 0:
                    result[nx][ny] = virus
                    virus_arr.append([virus,nx,ny])
                    # heapq.heappush(q,)
    for i in virus_arr:
        heapq.heappush(q, i)

print(result[target_x-1][target_y-1])
#     print(i)
# for i in result: