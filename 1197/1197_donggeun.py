# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：1197_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-19 오후 1:27 
'''

# wrong answer
# import sys
#
# v, e = map(int, sys.stdin.readline().split())
#
# arr = []
# for i in range(e):
#     a, b, c = map(int, sys.stdin.readline().split())
#     arr.append([c] +sorted([a,b]))
#
# # cost 기준, 정렬
# arr.sort()
#
# start_v = []
# end_v = []
# cost_sum = 0
#
# for edge in arr:
#     cost = edge[0]
#     start = edge[1]
#     end = edge[2]
#
#     if ((start not in start_v) and (end not in end_v)) or\
#             ((start not in start_v) and (end not in start_v)) or\
#             ((start not in end_v) and (end not in end_v)):
#         if start not in start_v:
#             start_v.append(start)
#         if end not in end_v:
#             end_v.append(end)
#         cost_sum+=cost
#
#     # print(cost, start, end, start_v, end_v)
#
#     if len(start_v) == v-1 or len(end_v) == v-1:
#         break
#
# print(cost_sum)



# 특정 원소가 속한 집합을 찾기

# 부모 찾기, 속한 집합?
def find(parent, x):
    # print('in', parent, x)
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    # print('resutl' , parent[x])
    return parent[x]

# 두 노드 연결
def union(parent, a,b):
    rootA = find(parent,a)
    rootB = find(parent,b)

    # 최고 높은 부모에서 연결
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

import sys

v, e = map(int, sys.stdin.readline().split())

arr = []
for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    arr.append([c] +sorted([a,b]))
# cost 기준, 정렬(크루스칼)
arr.sort()

# 테이블 초기화
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

cost_sum = 0

# print(parent)

for edge in arr:
    cost = edge[0]
    start = edge[1]
    end = edge[2]

    if find(parent, start) != find(parent, end):
        # print('start union', start, end)
        union(parent, start, end)
        cost_sum+=cost
        # print()

    # print(parent)

print(cost_sum)