# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：7569_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-21 오후 10:49 
'''

# import sys
# from collections import deque
#
# width, depth, height = map(int, sys.stdin.readline().split())
#
# arr = [[[-1] * width for _ in range(depth)] for _ in range(height)]
#
# good_tomato = 0
# bad_tomato = 0
# empty_tomato = 0
# for h in range(height):
#     for d in range(depth):
#         temp = list(map(int, sys.stdin.readline().split()))
#         for w in range(width):
#             if temp[w] == 1:
#                 good_tomato+=1
#             elif temp[w] == 0:
#                 bad_tomato+=1
#             else:
#                 empty_tomato+=1
#             arr[h][d][w] = temp[w]
# print('1 : ',good_tomato)
# print('0 : ',bad_tomato)
# print('-1 : ', empty_tomato)
# print()
#
# dx = [1,0,-1,0,0,0]
# dy = [0,1,0,-1,0,0]
# dz = [0,0,0,0,1,-1]
#
# # for i in range(6):
# #     print(dx[i], dy[i], dz[i])
#
# def bfs():
#     global cnt
#     visited = [[[False] * (width) for _ in range(depth)] for _ in range(height)]
#     q = deque()
#     q.append([0,0,0])
#     visited[0][0][0] = True
#
#     while q:
#         x, y, z = q.popleft()
#
#         for i in range(6):
#             nx= x+dx[i]
#             ny= y+dy[i]
#             nz= z+dz[i]
#
#             if width <= nx or nx < 0 or \
#                 depth <= ny or ny < 0 or \
#                 height <= nz or nz < 0:
#                 continue
#
#             # if arr[nz][ny][nx] == 1 and visited[nz][ny][nx] == False:
#             #     arr[z][y][x] = 1
#             #     q.append([nx, ny, nz])
#             #     visited[nz][ny][nx] = True
#             if arr[nz][ny][nx] == 0 and visited[nz][ny][nx] == False:
#                 cnt+=1
#                 arr[z][y][x] =+ arr[nz][ny][nx]
#                 q.append([nx,ny,nz])
#                 visited[nz][ny][nx] = True
#
# # case 1, 토마도가 모두 익어있는 상태
# # print(good_tomato+empty_tomato)
# # print(width*depth*height)
# # print(good_tomato+empty_tomato == width*depth*height)
#
# # case 2, 토마도가 모두 익지는 못하는 상황
# # cnt = 0
# # if arr[0][0][0] == 0:
# #         cnt = 1
# # bfs()
# # print(cnt)
# # print(bad_tomato)
# # print(cnt == bad_tomato)
#
# for i in range(height):
#     for j in range(depth):
#         print(arr[i][j])
#     print()
#
# # case 1
# if (good_tomato+empty_tomato) == (width*depth*height):
#     print(0)
#     exit()
#
# cnt = 0
# if arr[0][0][0] == 0:
#     cnt = 1
# bfs()
#
# print(cnt)
#
# for i in range(height):
#     for j in range(depth):
#         print(arr[i][j])
#     print()
#
# # case 2
# if cnt != bad_tomato:
#     print(-1)
#     exit()
#
# cnt = 0
# if arr[0][0][0] == 0:
#     cnt = 1
# bfs()
#
# print(cnt)
#
# for i in range(height):
#     for j in range(depth):
#         print(arr[i][j])
#     print()
#
# cnt = 0
# if arr[0][0][0] == 0:
#     cnt = 1
# bfs()
#
# print(cnt)
#
# for i in range(height):
#     for j in range(depth):
#         print(arr[i][j])
#     print()
#
# cnt = 0
# if arr[0][0][0] == 0:
#     cnt = 1
# bfs()
#
# print(cnt)
#
# for i in range(height):
#     for j in range(depth):
#         print(arr[i][j])
#     print()
#
# # before = cnt
# # for i in range(51):
# #     cnt = 0
# #     if arr[0][0][0] == 0:
# #         cnt = 1
# #     bfs()
# #
# #     if cnt == 0 and before==cnt:
# #         print(i)
# #         break
# #     else:
# #         before=cnt


import sys
from collections import deque

m,n,h = map(int, sys.stdin.readline().split())
graph = []
queue = deque([])

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                queue.append([i,j,k])
    graph.append(tmp)

# for i in graph:
#     for j in i:
#         print(j)

dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]

while queue:
    x,y,z = queue.popleft()

    for i in range(6):
        a = x +dx[i]
        b = y +dy[i]
        c = z +dz[i]

        if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c] == 0:
            queue.append([a,b,c])
            graph[a][b][c] = graph[x][y][z] +1

# for i in graph:
#     for j in i:
#         print(j)

day = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()
        day = max(day, max(j))
print(day-1)