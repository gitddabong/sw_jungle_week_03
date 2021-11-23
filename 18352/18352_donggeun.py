# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：18352_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-21 오후 4:55 
'''

# wrong answer
# import sys
# from collections import deque
#
# num_city, num_road, target_value, start_city = map(int, sys.stdin.readline().split())
# arr_road = [[]for i in range(num_city+1)]
# for i in range(num_road):
#     a, b = map(int,sys.stdin.readline().split())
#     arr_road[a].append(b)
#
# def bfs(v):
#     global flag, ans
#     visited = [False for i in range(num_city+1)]
#     q = deque()
#
#     visited[v] =True
#     q.append(v)
#
#     cnt = 0
#     while q:
#         cnt += 1
#         now = q.popleft()
#         # print('now', now)
#         # print('cnt', cnt)
#         for i in range(len(arr_road[now])):
#             if visited[arr_road[now][i]] == False:
#                 # print(cnt == target_value)
#                 if cnt == target_value:
#                     # print('in')
#                     flag=False
#                     ans.append(arr_road[now][i])
#                 visited[arr_road[now][i]] = True
#                 q.append(arr_road[now][i])
#         # if cnt==target_value:
#         #     break
#
# flag = True
# ans =[]
# bfs(start_city)
#
# if flag:
#     print(-1)
#     exit()
#
# ans.sort()
# for i in ans:
#     print(i)

import sys
from collections import deque

n,m,k,x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
# 해당 노드까지 갔을 때, 거리의 수 저장
distance = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    # 방향 그래프
    graph[a].append(b)

def bfs(start):
    answer = []
    q = deque([start])
    visited[start] = True
    distance[start] = 0

    while q:
        now = q.popleft()

        # now와 인접한 모든 노드 탐색
        for i in graph[now]:
            if not visited[i] :
                visited[i] = True
                q.append(i)
                # 인접 노드 = 현재 노드 + 1
                distance[i] = distance[now] +1
                if distance[i] == k:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i)

bfs(x)