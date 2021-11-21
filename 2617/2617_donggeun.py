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
big_arr = [[] for _ in range(n+1)]
small_arr = [[] for _ in range(n+1)]
for _ in range(m):
    big, small = map(int, sys.stdin.readline().split())
    big_arr[big].append(small)
    small_arr[small].append(big)

# print(big_arr)
# print(small_arr)

def dfs(arr, v, visited=[]):
    global cnt
    visited.append(v)
    for i in range(len(arr[v])):
        # print(v, i , arr[v][i])
        # print(type(arr[v][i]))
        # print(visited)
        # print(arr[v][i] not in visited)
        if arr[v][i] not in visited:
            cnt+=1
            dfs(arr, arr[v][i], visited)

cnt = 0
ans = 0
visited = []
for i in range(1, n+1):
    dfs(big_arr, i,visited)
    # print(i,cnt,ans,(n+1)//2)
    if cnt >= (n+1)//2:
        ans+=1
    cnt=0
    visited=[]
# dfs(big_arr,4)
# print(cnt)

for i in range(1, n+1):
    dfs(small_arr, i,visited)
    # print(i,cnt,ans,(n+1)//2)
    if cnt >= (n+1)//2:
        ans+=1
    cnt=0
    visited=[]

print(ans)