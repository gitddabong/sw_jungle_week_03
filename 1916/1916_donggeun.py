# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：1916_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-21 오후 8:06 
'''

# import sys
# from collections import deque
#
# num_city = int(sys.stdin.readline())
# num_bus = int(sys.stdin.readline())
# # arr_bus = []
# graph = [[0] * (num_city+1) for _ in range(num_city+1)]
# for _ in range(num_bus):
#     a, b, cost = map(int, sys.stdin.readline().split())
#     # arr_bus.append([cost, a, b])
#     graph[a][b] = cost
# start, end = map(int, sys.stdin.readline().split())

import heapq
import sys

def dijkstra(start_cost, start_node):
    dist = [sys.maxsize] * (n+1)
    dist[start_node] = 0
    q = [ (start_cost, start_node)]

    while q:
        p = heapq.heappop(q)
        cur_cost, cur_node = p[0], p[1]

        # need to time reduce
        if dist[cur_node] < cur_cost:
            continue

        for next_cost, next_node in graph[cur_node]:
            if dist[next_node]>cur_cost+next_cost:
                dist[next_node] = cur_cost+next_cost
                heapq.heappush(q, (dist[next_node], next_node))

    return dist

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [ [] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((cost, end))

want1, want2 = map(int, sys.stdin.readline().split())

answer = dijkstra(0,want1)
print(answer[want2])