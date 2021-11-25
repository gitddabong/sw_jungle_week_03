# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：1707_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-19 오후 9:11 
'''

# # wrong answer
# import sys
#
# """
#     노드에 색칠
# """
#
# testCase = int(sys.stdin.readline())
#
# for _ in range(testCase):
#     num_vertex, num_edge = map(int, sys.stdin.readline().split())
#     graph = [[] for _ in range(num_vertex+1)]
#     for _ in range(num_edge):
#         a, b = map(int,sys.stdin.readline().split())
#         graph[a].append(b)
#         graph[b].append(a)
#     print(graph)
#
#     color = [0] * (num_vertex+1)
#     color_check = True
#     flag = True
#
#     visited = []
#     color[1]= 1
#
#     def dfs(v):
#         global color_check, flag
#
#         visited.append(v)
#
#         if color_check:
#             color_check =False
#             print(-1)
#         else:
#             color_check= True
#             print(1)
#
#         print('vertex :',v)
#
#         for i in graph[v]:
#
#             if color_check:
#                 if color[i] == -1:
#                     flag = False
#                 color[i] = 1
#             else:
#                 if color[i] == 1:
#                     flag = False
#                 color[i] = -1
#             print('vertex & i :', v, i)
#             print(color)
#
#             if i not in visited:
#                 dfs(i)
#
#     dfs(1)
#
#     if flag:
#         print('YES')
#     else:
#         print('NO')

import sys
sys.setrecursionlimit(10**5)

testCase = int(sys.stdin.readline())

for _ in range(testCase):
    v, e = map(int, sys.stdin.readline().split())

    # 그래프를 딕셔너리 타입으로 구현
    tree = {}
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        if a in tree.keys():
            tree[a].append(b)
        else:
            tree[a] = [b]

        if b in tree.keys():
            tree[b].append(a)
        else:
            tree[b] = [a]

    # 색 초기화
    color = [0] * (v+1)
    flag = True

    def dfs(v, chk):
        global flag

        # 인접한 노드가 있는지 판단
        if v in tree.keys():
            # 모든 인접한 노드 탐색
            for i in tree[v]:
                # 인접한 노드의 색이 0이면, 방문하지 않은 노드
                # 색을 칠하고, 해당 노드 방문
                if not color[i]: # not visited
                    color[i] = chk
                    dfs(i, -chk)
                # 인접한 노드가 색이 칠해져 있는데, 자신과 색이 똑같으면 false
                elif color[i] == color[v]:
                    flag = False

    # 모든 노드가 연결되어 있지 않은 경우 처리
    for i in range(1,len(color)):
        if color[i]  == 0:
            dfs(i,-1)

    if flag:
        print('YES')
    else:
        print('NO')

