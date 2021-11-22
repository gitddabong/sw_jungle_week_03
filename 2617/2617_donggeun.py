# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：2617_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-21 오전 4:32 
'''

import sys

n,m = map(int, sys.stdin.readline().split())
# 방향 그래프 두 개
big_arr = [[] for _ in range(n+1)]
small_arr = [[] for _ in range(n+1)]
for _ in range(m):
    big, small = map(int, sys.stdin.readline().split())
    big_arr[big].append(small)
    small_arr[small].append(big)


def dfs(arr, v, visited=[]):
    global cnt
    visited.append(v)
    for i in range(len(arr[v])):
        if arr[v][i] not in visited:
            cnt+=1
            dfs(arr, arr[v][i], visited)

# 같은 방향으로 dfs 할 경우, 만나는 노드의 수
cnt = 0
ans = 0
visited = []

# 모든 노드에 대해서 dfs
for i in range(1, n+1):
    dfs(big_arr, i,visited)
    # 무게가 중간이 될 수 없는 경우, 정답 추가
    if cnt >= (n+1)//2:
        ans+=1
    cnt=0
    visited=[]

# 모든 노드에 대해서 dfs
for i in range(1, n+1):
    dfs(small_arr, i,visited)
    # 무게가 중간이 될 수 없는 경우, 정답 추가
    if cnt >= (n+1)//2:
        ans+=1
    cnt=0
    visited=[]

print(ans)