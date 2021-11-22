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
# 트리 구조를 리스트로 구현
arr_start = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    arr_start[a].append(b)
    arr_start[b].append(a)
    # 실내가 붙어 있을 경우
    if int(in_out[a-1]) == 1 and int(in_out[b-1]) == 1:
        cnt+=2

# 방문 초기화
visited = [False] * (n+1)
visite_cnt = 0

# 실외 기준으로 dfs
def dfs(v):
    global cnt, visite_cnt
    visited[v] = True

    # 모든 인접한 노드 탐색
    for i in arr_start[v]:
        # 인접한 해당 노드가 실내이면 cnt 증가
        if in_out[i - 1] == "1":
            visite_cnt += 1
        # 인접한 해당 노드가 실내가 아니고, 방문도 하지 않으면 방문
        elif visited[i] == False:
            dfs(i)

# 실내가 1개일 경우, 0 출력
only_in = []
for i in range(len(in_out)):
    if in_out[i] == "1":
        # 실내일 경우, 해당 노드 추가
        only_in.append(i+1)
if len(only_in) < 2:
    print(0)
    exit()

# 실외이고, 방문하지 않았으면 해당 노드 탐색
# 실외끼리 연결이 안되어 있을 수 있음
for i in range(1, n+1):
    if in_out[i-1] == "0" and (visited[i] == False):
        # 해당 노드를 방문하고 모든 인접한 실외 노드까지 탐색
        dfs(i)
        # 해당 노드(인접한 실외 노드 포함)에서 인접한 실내 노드의 카운트를 가지고 산책 route 계산
        # 출발은 cnt개, 도착은 cnt-1개가 가능하므로 total += cnt(cnt-1)
        cnt += visite_cnt * visite_cnt - visite_cnt
    visite_cnt=0

print(cnt)