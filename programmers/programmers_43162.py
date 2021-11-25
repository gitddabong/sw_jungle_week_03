# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：programmers_43162.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-24 오후 3:30 
'''

# from collections import deque
#
# # def bfs(point, visited, computers):
# #     q = deque()
# #     visited[point[0]][point[1]] = True
# #     q.append([point[0], point[1]])
# #     dx= [-1,1,0,0]
# #     dy= [0,0,-1,1]
# #
# #     while q:
# #         now = q.popleft()
# #         x, y = now[0], now[1]
# #
# #         for i in range(4):
# #             nx = x+dx[i]
# #             ny = y+dy[i]
# #             if 0<= nx < len(visited) and 0<=ny < len(visited):
# #                 if visited[nx][ny] ==False and computers[nx][ny] == 1:
# #                     q.append([nx,ny])
# #                     visited[nx][ny] = True
# #
# #     return visited
#
# def bfs(point, visited, computers):
#     q = deque()
#     visited[point[0]][point[1]] = True
#     q.append([point[0], point[1]])
#
#     while q:
#         now = q.popleft()
#         x, y = now[0], now[1]
#
#         for i in range(len(computers[x])):
#             if computers[x][i] == 1 and visited[x][i] == False:
#                 visited[x][i] = True
#                 visited[i][x] = True
#                 q.append([x,i])
#
#     return visited
#
# def solution(n, computers):
#     answer = 0
#
#     visited = [[False]*(n) for _ in range(n)]
#
#     for i in range(n):
#         for j in range(n):
#             if computers[i][j] == 1 and visited[i][j] == False and i != j:
#                 print(i,j)
#                 visited = bfs([i,j], visited, computers)
#                 answer+=1
#
#     return answer
#
# # print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 1, 1]]))
# print(solution(4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]), 1)

from collections import deque

def bfs(point, computer):
    x, y = point[0], point[1]
    q = deque()
    q.append([x,y])
    computer[x][y] = 0

    while q:
        x,y = q.popleft()
        for i in range(len(computer[x])):
            if computer[x][i] == 1:
                # print(x,i)
                computer[x][i] = 0
                computer[i][x] = 0
                q.append([i,x])
        # print(q)

    return computer

def solution(n, computers):
    answer = 0
    # computers = bfs([0,0], computers)
    # print(type(computers))
    # print(computers)

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                computers = bfs([i, j], computers)
                # print(type(computers))
                # print(computers)
                # for i in computers:
                #     print(i)
                answer+=1

    return answer

print(solution(4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]))