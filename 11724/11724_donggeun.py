# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：11724_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-19 오후 4:20 
'''


# import sys
#
# num_vertex, num_edge = map(int, sys.stdin.readline().split())
#
# edges = {}
#
# for i in range(num_edge):
#     start, end = map(int, sys.stdin.readline().split())
#
#     if start not in edges.keys():
#         edges[start] = [end]
#     else:
#         edges[start].append(end)
#         edges[start] = sorted(edges[start])
#
#     if end not in edges.keys():
#         edges[end] = [start]
#     else:
#         edges[end].append(start)
#         edges[end] = sorted(edges[end])
#
# def find(parent, x):
#     if parent[x] == x:
#         return x
#     else:
#         parent[x] = find(parent, parent[x])
#         return parent[x]
#
# def union(parent, x, y):
#     rootx = find(parent,x)
#     rooty = find(parent,y)
#
#     if rootx < rooty:
#         parent[rooty] = rootx
#     else:
#         parent[rootx] = rooty
#
# parent = [0] *(num_vertex+1)
#
# for i in range(1, num_vertex+1):
#     parent[i] = i
#
# # print(edges)
#
# visited =[]
# def dfs(v):
#     print(visited, v)
#     if v in visited:
#         return
#     else:
#         visited.append(v)
#         for destination in edges[v]:
#             if destination not in visited:
#                 dfs(destination)
#         visited.pop()
#
# for i in range(1, num_vertex+1):
#     dfs(i)

# # use union find
# import sys
#
# n, m = map(int, sys.stdin.readline().split())
#
# parent = [0] * (n+1)
# for i in range(1, n+1):
#     parent[i] = i
#
# def find(parent, x):
#     if parent[x] == x:
#         return x
#     return find(parent, parent[x])
#
# def union(parent, x, y):
#     x = find(parent, x)
#     y = find(parent, y)
#     if x < y:
#         parent[y] = x
#     else:
#         parent[x] = y
#
# for _ in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     union(parent,a, b)
#
# result = []
# for a in parent:
#     result.append(find(parent,a))
# # print(result)
#
# print(len(set(result[1:])))


# # use bfs
# import sys
# from collections import deque
#
# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
#
#     while queue:
#         v = queue.popleft()
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#
# n, m = map(int, sys.stdin.readline().split())
# graph = [[] for _ in range(n+1)]
# visited = [False] * (n+1)
#
# for i in range(m):
#     node1, node2 = map(int, sys.stdin.readline().split())
#     graph[node1].append(node2)
#     graph[node2].append(node1)
#
# cnt = 0
#
# for i in range(1, n+1):
#     if not visited[i]:
#         bfs(graph, i, visited)
#         cnt +=1
# print(cnt)

# use dfs
import sys

# 정점, 간선 입력
n,m = map(int, sys.stdin.readline().split())
# 2차원 배열 선언
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start, visited):
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            dfs(i, visited)

# 한 정점을 기준으로 dfs가 끝났을때,
# visited하지 않은 정점이 있을 경우 해당 정점을 기준으로 dfs 호출
cnt = 0
for i in range(1, n+1):
    if visited[i] == False:
        cnt+=1
        dfs(i, visited)

print(cnt)