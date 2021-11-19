# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：1260_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-19 오후 3:17 
'''

# only one edge for each vertex
# import sys
#
# num_vertex, num_edge, start_vertex = map(int, sys.stdin.readline().split())
#
# tree = {}
#
# for _ in range(num_edge):
#     start, end = map(int, sys.stdin.readline().split())
#     start, end = (start, end) if start < end else (end, start)
#
#     if start not in tree.keys():
#         tree[start] = [end]
#     else:
#         tree[start].append(end)
#         tree[start] = sorted(tree[start])
#
# print(tree)
#
# # dfs
# visited = []
#
# def dfs(v):
#     if v in visited:
#         return
#     if v in tree.keys():
#         for edge in tree[v]:
#             print('edge', edge)
#             visited.append(v)
#             print(v)
#             dfs(edge)
#             visited.pop()
#     else:
#         return
#
# dfs(start_vertex)
#


# import collections
# import sys
#
# num_vertex, num_edge, start_vertex = map(int, sys.stdin.readline().split())
#
# tree = {}
#
# for _ in range(num_edge):
#     start, end = map(int, sys.stdin.readline().split())
#
#     if start not in tree.keys():
#         tree[start] = [end]
#     else:
#         tree[start].append(end)
#         tree[start] = sorted(tree[start])
#
#     if end not in tree.keys():
#         tree[end] = [start]
#     else:
#         tree[end].append(start)
#         tree[end] = sorted(tree[end])
#
# # print(tree)
#
# # dfs
# visited = []
#
# def dfs(v):
#     # if v in visited:
#     #     return
#     print(v, end=' ')
#     # if len(visited) == num_vertex:
#     #     print(*visited)
#     if v in tree.keys():
#         for destination in tree[v]:
#             # print('edge', edge)
#             visited.append(v)
#             if destination in visited:
#                 continue
#             else:
#                 dfs(destination)
#             # visited.pop()
#     else:
#         return
#
# dfs(start_vertex)
#
# print()
#
# # bfs
# queue = collections.deque()
# visited = []
#
# def bfs(v):
#     queue.append(v)
#
#     while queue:
#         now = queue.popleft()
#         print(now,end=' ')
#         visited.append(now)
#         if now in tree.keys():
#             # print(tree[now])
#             for cardidate in tree[now]:
#                 # print('cardidate',cardidate)
#                 if cardidate not in visited:
#                     visited.append(cardidate)
#                     queue.append(cardidate)
#                 # print(queue)
#
# bfs(start_vertex)
#

import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

graph = [[0] *(N+1) for _ in range(N+1)]

for _ in range(M):
    m1, m2 = map(int, sys.stdin.readline().split())
    graph[m1][m2] = graph[m2][m1] = 1

def bfs(start_v):
    discoverd = [start_v]
    queue = deque()
    queue.append(start_v)

    while queue:
        v = queue.popleft()
        print(v,end=' ')

        for w in range(len(graph[start_v])):
            if graph[v][w] == 1 and (w not in discoverd):
                discoverd.append(w)
                queue.append(w)

def dfs(start_v, discoverd=[]):
    discoverd.append(start_v)
    print(start_v, end=' ')

    for w in range(len(graph[start_v])):
        if graph[start_v][w] == 1 and (w not in discoverd):
            dfs(w,discoverd)

dfs(V)
print()
bfs(V)