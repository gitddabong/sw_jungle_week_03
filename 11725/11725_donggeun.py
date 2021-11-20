# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：11725_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-19 오후 6:51 
'''

# # memory over
# import sys
#
# num_node = int(sys.stdin.readline())
#
# graph = [[0] * (num_node+1) for _ in range(num_node+1)]
#
# while True:
#     try:
#         a, b = map(int, sys.stdin.readline().split())
#         graph[a][b] = graph[b][a] = 1
#     except:
#         break
#
# # print([0] +list(range(8)))
# # c = 0
# # for i in graph:
# #     print([c] + i)
# #     c+=1
#
# visited = []
# def dfs(v, target):
#     # print(v, visited)
#     visited.append(v)
#     for i in range(len(graph[v])):
#         if (i not in visited) and (graph[v][i] == 1):
#             if i == target:
#                 print(v,end=' ')
#             else:
#                 dfs(i, target)
#
# for i in range(1, num_node+1):
#     dfs(1, i)
#     visited=[]

# # time over
# import sys
#
# num_node = int(sys.stdin.readline())
# tree = {}
# while True:
#     try:
#         a, b = map(int, sys.stdin.readline().split())
#         if a not in tree.keys():
#             tree[a] = [b]
#         else:
#             tree[a].append(b)
#         if b not in tree.keys():
#             tree[b] = [a]
#         else:
#             tree[b].append(a)
#     except:
#         break
#
# # print(tree)
#
# visited = []
# def dfs(v, target):
#     visited.append(v)
#     for i in tree[v]:
#         if i not in visited:
#             if i == target:
#                 print(v, end=' ')
#             else:
#                 dfs(i, target)
#
# for i in range(2, num_node+1):
#     dfs(1, i)
#     visited=[]
#
# # print(visited)

# # time over
# import sys
# sys.setrecursionlimit(10**5)
#
# num_node = int(sys.stdin.readline())
# tree = {}
# while True:
#     try:
#         a, b = map(int, sys.stdin.readline().split())
#         if a not in tree.keys():
#             tree[a] = [b]
#         else:
#             tree[a] = tree[a] + [b]
#         if b not in tree.keys():
#             tree[b] = [a]
#         else:
#             tree[b] = tree[b] + [a]
#     except:
#         break
#
# # print(tree)
#
# parent = [0] * (num_node+1)
# for i in range(1, num_node+1):
#     parent[i]=i
#
# visited = []
# def dfs(v):
#     visited.append(v)
#     for i in tree[v]:
#         if i not in visited:
#             parent[i] = v
#             dfs(i)
#
# dfs(1)
#
# s=''
# for i in parent[2:]:
#     s+=str(i)+'\n'
# print(s)

# import sys
# sys.setrecursionlimit(300000)
#
# def dfs(v):
#     for i in graph[v]:
#         if p[i] == 0:
#             p[i] = v
#             dfs(i)
#
# n = int(sys.stdin.readline())
# graph = [[] for _ in range(n+1)]
#
# for _ in range(n-1):
#     u, v = map(int, sys.stdin.readline().split())
#     graph[u].append(v)
#     graph[v].append(u)
# p = [0]*(n+1)
# dfs(1)
# for i in range(2, n+1):
#     print(p[i])
#


import sys
sys.setrecursionlimit(10**5)

num_node = int(sys.stdin.readline())
tree = {}
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        if a not in tree.keys():
            tree[a] = [b]
        else:
            tree[a] = tree[a] + [b]
        if b not in tree.keys():
            tree[b] = [a]
        else:
            tree[b] = tree[b] + [a]
    except:
        break

# print(tree)

parent = [0] * (num_node+1)

def dfs(v):
    for i in tree[v]:
        if parent[i] == 0:
            parent[i] = v
            dfs(i)

dfs(1)

s=''
for i in parent[2:]:
    s+=str(i)+'\n'
print(s)