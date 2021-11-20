# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：21606_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-20 오후 1:20 
'''

# # score : 98, time over
# import sys
# sys.setrecursionlimit(10**5)
#
# n = int(sys.stdin.readline())
# in_out = list(sys.stdin.readline().strip())
# arr_start = [[] for i in range(n+1)]
# for i in range(n-1):
#     a, b = map(int, sys.stdin.readline().split())
#     arr_start[a].append(b)
#     arr_start[b].append(a)
#
# # print(in_out)
# # print(arr_start)
#
# cnt = 0
# visited = []
# def dfs(v):
#     global cnt
#     visited.append(v)
#     for i in arr_start[v]:
#         if i not in visited:
#             if in_out[i-1] == "1":
#                 visited.append(i)
#                 cnt +=1
#             else:
#                 dfs(i)
#
# only_in = []
# for i in range(len(in_out)):
#     if in_out[i] == "1":
#         only_in.append(i+1)
# # print('only_in',only_in)
#
# for i in only_in:
#     dfs(i)
#     # print(visited)
#     visited=[]
#
# print(cnt)

# 실내 기준 dfs가 아니라, 실외 기준 dfs
# 만나는 실외마다 count
# 실내가 붙어있을 경우는 간선을 입력 받을 때 +2 처리
import sys
sys.setrecursionlimit(10**5)

cnt = 0
n = int(sys.stdin.readline())
in_out = list(sys.stdin.readline().strip())
arr_start = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    arr_start[a].append(b)
    arr_start[b].append(a)
    # 실내가 붙어 있을 경우
    if in_out[a-1] == 1 and in_out[b-1] == 1:
        cnt+=2

# print(in_out)
# print(arr_start)

visited = []
def dfs(v):
    global cnt
    visited.append(v)
    for i in arr_start[v]:
        if i not in visited:
            if in_out[i-1] == "1":
                visited.append(i)
                cnt +=1
            else:
                dfs(i)

only_in = []
for i in range(len(in_out)):
    if in_out[i] == "1":
        only_in.append(i+1)
# print('only_in',only_in)

if len(only_in) < 2:
    print(0)
    exit()

for i in only_in:
    dfs(i)
    # print(visited)
    visited=[]

print(cnt)