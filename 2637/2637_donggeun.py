# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：2637_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-22 오후 5:27 
'''

# """
#     기본 부품 1~N-1 중 여러 개 일 수 있음
# """
#
#
# import sys
# from collections import deque
#
# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())
# arr = [{} for _ in range(n+1)]
# middle = []
# for _ in range(m):
#     x,y,k = map(int, sys.stdin.readline().split())
#     middle.append(x)
#     arr[x][y] = k
# # print(arr)
#
# # total = [0 for _ in range(n+1)]
# # total[n] = 1
# # print(total)
#
#
# queue = deque()
# queue.append(n)
#
# primary = [ 0 for _ in range(n+1)]
# middle_cnt = [ 0 for _ in range(n+1)]
# middle_cnt[n] = 1
#
# while queue:
#     now = queue.popleft()
#
#     # key is parts
#     for key in arr[now].keys():
#         print(now, key)
#         print(middle_cnt, primary)
#         if key not in middle:
#             primary[key]+= middle_cnt[now] * arr[now][key]
#         else:
#             middle_cnt[key] += middle_cnt[now] * arr[now][key]
#             queue.append(key)
#
# # print(primary)
#
# for i in range(1, len(primary)):
#     if primary[i] != 0:
#         print(i, primary[i])

import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
connect = [[] for _ in range(n+1)]
needs =  [ [0] * (n+1) for _ in range(n+1)]
q = deque()
degree = [0] * (n+1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    # 기본 부품에서 중간 또는 완제품으로 가는 간선 생성
    # 기본 = (중간 또는 완제품, 비용)
    connect[b].append((a,c))
    degree[a] +=1

# 진입 차수가 0인, 기본 부품을 큐에 추가
for i in range(1, n+1):
    if degree[i] == 0 :
        q.append(i)

while q:
    now = q.popleft()
    for next, next_need in connect[now]:
        # 기본 부품에 추가
        if needs[now].count(0) == n+1:
            needs[next][now] += next_need
        # 필요한만큼 곱해서 추가
        else:
            for i in range(1, n+1):
                needs[next][i] += needs[now][i] * next_need
        degree[next] -= 1
        if degree[next] == 0:
            q.append(next)

for x in enumerate(needs[n]):
    if x[1] > 0:
        print(*x)
