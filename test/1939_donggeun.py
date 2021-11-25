# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：1939_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-25 오전 10:38 
'''
"""
    최대 중량 찾기
    
    최소, 최대에서 가능한 이분탐색
    bfs에서 중간값을 기준으로 
    
    사냥꾼 : decision algorithm
    그래프 탐색을 하면서 찾음
"""
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
# arr = [[float('inf')]*(n+1) for _ in range(n+1)]
arr = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    arr[a][b] = cost # if arr[a][b] > cost else arr[a][b]
    arr[b][a] = cost # if arr[b][a] > cost else arr[b][a]

fact1, fact2 = map(int, sys.stdin.readline().split())


# def dfs(start, end, max_cost):
#     print(start, end, max_cost)
#     if start == end :
#         return max_cost
#     for i in range(len(arr[start])):
#         if arr[start][i] != 0:
#             max_cost = min(max_cost, arr[start][i])
#             arr[start][i] = arr[i][start] = 0
#             dfs(i, end, max_cost)
#
# print(dfs(fact1,fact2,float('inf')))

def bfs(v):
    max_cost = float('inf')
    q = deque()
    visited = []
    q.append(v)
    visited.append(v)

    while q:
        now = q.popleft()
        print(now)

        candidate = []
        for i in range(len(arr[now])):
            if i not in visited and arr[now][i] != 0:
                candidate.append(i)
        candidate.sort()

        if candidate:
            max_cost = min(max_cost,arr[now][candidate[-1]])
            print(max_cost)
            q.append(candidate[-1])
            visited.append(candidate[-1])

bfs(fact1)