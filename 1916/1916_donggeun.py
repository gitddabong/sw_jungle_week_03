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

# 최단 경로 탐색 알고리즘
# bfs 확장, 경로를 갱신하면서 비용 갱신
def dijkstra(start_cost, start_node):
    # 큰 값으로 초기화
    dist = [sys.maxsize] * (n+1)
    # 자기 자신의 비용은 0
    dist[start_node] = 0
    # queue = [cost, node]
    q = [ (start_cost, start_node)]

    while q:
        p = heapq.heappop(q)
        print('now',p)
        # 현재 비용, 현재 노드
        cur_cost, cur_node = p[0], p[1]

        # need to time reduce
        if dist[cur_node] < cur_cost:
            continue

        # 인접한 모든 노드 탐색
        for next_cost, next_node in graph[cur_node]:
            # 만약 인접한 노드의 비용이 현재비용+노드로 향하는 비용이 크면
            if dist[next_node]>cur_cost+next_cost:
                dist[next_node] = cur_cost+next_cost
                # 힙큐
                heapq.heappush(q, (dist[next_node], next_node))

        print(q)
    return dist

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [ [] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((cost, end))

want1, want2 = map(int, sys.stdin.readline().split())

# print('graph')
# for i in graph:
#     print(i)

answer = dijkstra(0,want1)
print(answer[want2])