# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：2178_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-21 오후 3:02 
'''

# # time over
# import sys
# from collections import deque
#
# row, column = map(int, sys.stdin.readline().split())
# arr = [[] for _ in range(row)]
# for i in range(row):
#     temp = sys.stdin.readline().strip()
#     arr[i] = list(map(int, list(temp)))
#
# dy=[-1,0,1,0]
# dx=[0,-1,0,1]
#
# def bfs(point):
#     q = deque()
#     visited = []
#
#     q.append(point)
#     visited.append(point)
#
#     while q:
#         now = q.popleft()
#         x = now[0]
#         y = now[1]
#
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#
#             if nx < 0 or ny < 0 or nx >= row or ny >= column:
#                 continue
#
#             if arr[nx][ny] != 0:
#                 if [nx, ny] not in visited:
#                     arr[nx][ny] += arr[x][y]
#
#                     if nx == row-1 and ny == column-1:
#                         visited.append([nx, ny])
#                         print(arr[row-1][column-1])
#                     else:
#                         visited.append([nx,ny])
#                         q.append([nx,ny])
#
#
# bfs([0,0])

import sys
from collections import deque

# 입력 처리
row, column = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(row)]
for i in range(row):
    temp = sys.stdin.readline().strip()
    arr[i] = list(map(int, list(temp)))

dy=[-1,0,1,0]
dx=[0,-1,0,1]

# bfs
def bfs(point):
    q = deque()
    # 2차원 리스트
    visited = [[0] * column for i in range(row)]

    q.append(point)
    visited[point[0]][point[1]] = 1
    # visited.append(point)

    while q:
        now = q.popleft()
        x = now[0]
        y = now[1]

        # 인접한 노드 탐색
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            # 행렬 범위 체크
            if nx < 0 or ny < 0 or nx >= row or ny >= column:
                continue

            # 이동할 수 있는 경우
            if arr[nx][ny] != 0:
                # 방문을 안했을 경우
                if visited[nx][ny] == 0 :
                    # 현재 노드 값을 인접 노드에 더함
                    arr[nx][ny] += arr[x][y]

                    # 인접 노드가 도착했을 경우
                    if nx == row-1 and ny == column-1:
                        visited[nx][ny] = 1
                        print(arr[row-1][column-1])
                    # 아니면 큐에 추가
                    else:
                        visited[nx][ny] = 1
                        q.append([nx,ny])


bfs([0,0])