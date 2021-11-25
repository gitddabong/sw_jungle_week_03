# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：1432_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-23 오전 1:33 
'''

# wrong answer
import sys
from collections import deque

n = int(sys.stdin.readline())
arr = [[] for _ in range(n)]
out_degree = [0] * ( n+1)
for i in range(n):
    temp = list(map(int,sys.stdin.readline().strip()))
    for j in range(n):
        if temp[j] == 1:
            out_degree[i+1]+=1
    arr[i] = temp

# for i in arr:
#     print(i)
# print(out_degree)

q = deque()

candidate = []
for i in range(1, n+1):
    if out_degree[i] == 0:
        candidate.append(i)
candidate.sort(reverse=True)
# for i in range(len(candidate)):
#     q.append(candidate[i])
if candidate:
    q.append(candidate[0])

# 그래프 수정 할 수 없을 때
if not q:
    print(-1)
    exit()

result = [0] * (n+1)
cnt = n
while q:
    # print(q)
    now = q.popleft()
    result[now] = cnt
    cnt -= 1
    out_degree[now] = -1

    for i in range(n):
        if arr[i][now-1] == 1:
            # print(i,now-1)
            out_degree[i+1] -= 1
    # print(out_degree)

    candidate = []
    for i in range(1, n+1):
        if out_degree[i] == 0 and i not in q:
            candidate.append(i)
    candidate.sort()
    #
    # for i in candidate:
    if candidate:
        q.append(candidate[-1])

    # print(result)

print(*result[1:])

# import sys
# from collections import deque
#
# n = int(sys.stdin.readline())
# arr = [[] for _ in range(n)]
# out_degree = [0] * ( n+1)
# for i in range(n):
#     temp = list(map(int,sys.stdin.readline().strip()))
#     for j in range(n):
#         if temp[j] == 1:
#             out_degree[i+1]+=1
#     arr[i] = temp
#
# # for i in arr:
# #     print(i)
# # print(out_degree)
#
# q = []
#
# candidate = []
# for i in range(1, n+1):
#     if out_degree[i] == 0:
#        q.append(i)
#
# # 그래프 수정 할 수 없을 때
# if not q:
#     print(-1)
#     exit()
#
# result = [0] * (n+1)
# cnt = n
# while q:
#     q.sort()
#     now = q.pop()
#     result[now] = cnt
#     cnt -= 1
#     out_degree[now] = -1
#
#     for i in range(n):
#         if arr[i][now-1] == 1:
#             # print(i,now-1)
#             out_degree[i+1] -= 1
#     # print(out_degree)
#
#     candidate = []
#     for i in range(1, n+1):
#         if out_degree[i] == 0 and i not in q:
#             candidate.append(i)
#     candidate.sort()
#     #
#     # for i in candidate:
#     if candidate:
#         q.append(candidate[-1])
#
#     # print(result)
#
# print(*result[1:])