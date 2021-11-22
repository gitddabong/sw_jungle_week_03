# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：2573_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-20 오후 7:44 
'''

# # time over
# import sys
# sys.setrecursionlimit(10**5)
#
# """
#     바다를 dfs 할 경우
#     10^9 = 10억 >> 시간초과
#
#     빙산을 기준으로 dfs
#     dfs할때 한번으로 모든 노드를 방문할 수 없을 때 >> 두 덩어리로 분리될 때
#     count 출력
# """
#
# row, column = map(int, sys.stdin.readline().split())
# arr = [[] for _ in range(row)]
# ice = []
# for i in range(row):
#     temp = list(sys.stdin.readline().split())
#     temp = list(map(int, temp))
#     for j in range(len(temp)):
#         if temp[j] != 0:
#             ice.append([i,j])
#     arr[i] = temp
#
# ice.sort()
#
# # return right, down, left, up
# def check_direction(x, y):
#     return [[x, y+1], [x+1, y], [x, y-1], [x-1, y]]
#
#
# def dfs(point):
#     visited.append(point)
#     x, y = point[0], point[1]
#     # print(point, arr[x][y])
#
#     # 해당 포인트가 바다에 접한 만큼 value --
#     for i in check_direction(x, y):
#         # print(visited)
#         if i not in visited:
#             if arr[i[0]][i[1]] == 0:
#                 # print(i)
#                 if arr[x][y] > 0:
#                     arr[x][y]-=1
#                 else:
#                     arr[x][y] = 0
#
#     # dfs 재귀 호출, xy 좌표
#     for i in check_direction(x,y):
#         if i in ice:
#             if i not in visited:
#                 dfs(i)
#
#
# for trial in range(10001):
#     ice = []
#     for i in range(row):
#         for j in range(column):
#             if arr[i][j] != 0:
#                 ice.append([i,j])
#     visited = []
#
#     # print('ice',ice)
#
#     if len(ice) <= 1:
#         break
#     dfs(ice[0])
#
#     # for i in arr:
#     #     print(i)
#
#     if len(ice) != len(visited):
#         print(trial)
#         exit()
#
# print(0)

# test
# ice = []
# visited = []
#
# for i in range(row):
#     for j in range(column):
#         if arr[i][j] != 0:
#             ice.append([i,j])
# dfs(ice[0])
# for i in arr:
#     print(i)
#
# if len(ice) == len(visited):
#     print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
#
#
# ice = []
# visited = []
#
# for i in range(row):
#     for j in range(column):
#         if arr[i][j] != 0:
#             ice.append([i,j])
# dfs(ice[0])
# for i in arr:
#     print(i)
#
# if len(ice) == len(visited):
#     print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

# time over, if 298x298 ice,
# import sys
# sys.setrecursionlimit(10**5)
#
# """
#     바다를 dfs 할 경우
#     10^9 = 10억 >> 시간초과
#
#     빙산을 기준으로 dfs
#     dfs할때 한번으로 모든 노드를 방문할 수 없을 때 >> 두 덩어리로 분리될 때
#     count 출력
# """
#
# row, column = map(int, sys.stdin.readline().split())
# arr = [[] for _ in range(row)]
# ice = []
# for i in range(row):
#     temp = list(sys.stdin.readline().split())
#     temp = list(map(int, temp))
#     for j in range(len(temp)):
#         if temp[j] != 0:
#             ice.append([i,j])
#     arr[i] = temp
#
# ice.sort()
#
# # # return right, down, left, up
# # def check_direction(x, y):
# #     return [[x, y+1], [x+1, y], [x, y-1], [x-1, y]]
#
#
# def dfs(point):
#     visited.append(point)
#     x, y = point[0], point[1]
#     # print(point, arr[x][y])
#     # print(visited)
#
#     # for i in arr:
#     #     print(i)
#
#     # # 해당 포인트가 바다에 접한 만큼 value --
#     # for i in check_direction(x, y):
#     #     # print(visited)
#     #     if i not in visited:
#     #         if arr[i[0]][i[1]] == 0:
#     #             # print(i)
#     #             if arr[x][y] > 0:
#     #                 arr[x][y]-=1
#     #             else:
#     #                 arr[x][y] = 0
#
#     # improve time
#     # no use check_direction func and for loop
#     if y+1 < column:
#         if ([x,y+1] not in visited) and (arr[x][y+1] == 0):
#             if arr[x][y] > 0:
#                 arr[x][y] -= 1
#             else:
#                 arr[x][y] = 0
#         if [x,y+1] in ice:
#             if [x,y+1] not in visited:
#                 dfs([x,y+1])
#     if y-1 > -1:
#         if ([x,y-1] not in visited) and (arr[x][y-1] == 0):
#             if arr[x][y] > 0:
#                 arr[x][y] -= 1
#                 # dfs([x, y-1])
#             else:
#                 arr[x][y] = 0
#         if [x,y-1] in ice:
#             if [x,y-1] not in visited:
#                 dfs([x,y-1])
#     if x+1 < column:
#         if ([x+1,y] not in visited) and (arr[x+1][y] == 0):
#             if arr[x][y] > 0:
#                 arr[x][y] -= 1
#                 # dfs([x+1, y])
#             else:
#                 arr[x][y] = 0
#         if [x+1,y] in ice:
#             if [x+1,y] not in visited:
#                 dfs([x+1,y])
#     if x-1 > -1:
#         if ([x-1,y] not in visited) and (arr[x-1][y] == 0):
#             if arr[x][y] > 0:
#                 arr[x][y] -= 1
#                 # dfs([x-1, y])
#             else:
#                 arr[x][y] = 0
#         if [x-1,y] in ice:
#             if [x-1,y] not in visited:
#                 dfs([x-1,y])
#
#
#     # # dfs 재귀 호출, xy 좌표
#     # for i in check_direction(x,y):
#     #     if i in ice:
#     #         if i not in visited:
#     #             dfs(i)
#
#
# for trial in range(10001):
#     ice = []
#     for i in range(row):
#         for j in range(column):
#             if arr[i][j] != 0:
#                 ice.append([i,j])
#     visited = []
#
#     # print('ice',ice)
#
#     if len(ice) <= 1:
#         break
#     dfs(ice[0])
#
#     # print('visited', visited)
#     #
#     # for i in arr:
#     #     print(i)
#
#     if len(ice) != len(visited):
#         print(trial)
#         exit()
#
# print(0)


# no understand

def check(y, x):
    global N, M
    # 빙산, 자기 자신 카운트
    cnt = 1
    visited = [[False] * M for _ in range(N)]
    visited[y][x] = True

    s = [(y, x)]

    while s:
        y, x = s.pop()

        # 상하좌우에 대하여 탐색
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]

            if not visited[ny][nx] and arr[ny][nx] != 0:
                # 방문하지 않고 빙산이면 카운트 증가
                s.append((ny, nx))
                visited[ny][nx] = True
                cnt += 1

    # 총 연결된 빙산의 수
    return cnt

# 행, 열 입력
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 녹을 빙산 저장 리스트
melt = [[0] * M for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 빙산 인덱스 저장
ice = []
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if arr[i][j] != 0:
            ice.append((i, j))

ans = 0
cnt = 0

# 모든 빙산에 대해서 bfs?
while ice:
    # 모든 빙산의 개수랑 첫 번째 빙산에서 bfs한 빙산의 수가 다른 경우
    # 둘로 나누어짐
    if len(ice) != check(ice[0][0], ice[0][1]):
        ans = cnt
        break

    # 시간 증가
    cnt += 1

    # 녹을 빙산 저장
    melt_co = []
    # 모든 빙산 반복
    for i in range(len(ice) - 1, -1, -1):
        y, x = ice[i]

        # 인접한 노드의 모든 경우
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]

            # 인접한 노드가 바다일 경우, 빙산이 녹을 경우 증가
            if arr[ny][nx] == 0:
                melt[y][x] += 1

        # 녹을 경우가 있을 경우, 인덱스와 빙산 인덱스 추가
        if melt[y][x] > 0:
            melt_co.append((y, x, i))

    # 녹을 경우가 있는 모든 빙산
    for y, x, i in melt_co:
        # 빙산 녹음
        arr[y][x] -= melt[y][x]
        if arr[y][x] <= 0:
            arr[y][x] = 0
            ice.pop(i)
        # 초기와
        melt[y][x] = 0

print(ans)