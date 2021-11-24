# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：1948_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-23 오후 5:07 
'''

import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
in_degree = [0] * (n+1)
out_degree = [0] * (n+1)
arr = [[] for _ in range(n+1)]
revers_arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    in_degree[b]+=1
    out_degree[a]+=1
    arr[a].append([b,c])
    revers_arr[b].append([a,c])

start, end = map(int, sys.stdin.readline().split())

q = deque()
q.append(start)

cost = [0] * (n+1)
cost[start] = 0

while q:
    now = q.popleft()
    # print(now)
    # print('in', in_degree)
    # print('out', out_degree)
    # print(cost)
    for i in arr[now]:
        in_degree[i[0]] -= 1
        # print(now, i)
        if in_degree[i[0]] == 0 :
            q.append(i[0])
        if cost[i[0]] < (cost[now] + i[1]):
            cost[i[0]] = cost[now] + i[1]


print(cost[end])

q.append(end)
visited = [False] * (n+1)

cnt = 0
while q:
    now = q.popleft()
    visited[now]=True
    for i in revers_arr[now]:
        out_degree[i[0]] -= 1
        if cost[i[0]] == cost[now] - i[1]:
            # print(now, i)
            cnt+=1
            if visited[i[0]] == False:
                visited[i[0]] = True
                q.append(i[0])
    # print(q)
print(cnt)

"""
cnt = 0
while q:
    now = q.popleft()

    for i in revers_arr[now]:
        out_degree[i[0]] -= 1
        if cost[i[0]] == cost[now] - i[1]:
            # print(now, i)
            cnt+=1
            # 반례, 진출차수가 0이 아니여도 가능성 있는 간선이 있을 수 있음
            if out_degree[i[0]] == 0:
                q.append(i[0])
    # print(q)
print(cnt)

반례 : 
5
7
1 2 1
1 3 3
2 3 2
2 4 1
2 5 3
3 5 1
4 5 1
1 5


5
7
1 2 1
1 3 3
2 3 2
2 4 1
4 5 1
3 5 1
2 5 3
1 5
"""