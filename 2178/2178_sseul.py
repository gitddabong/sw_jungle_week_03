#첫번째 시도 1,1 로 시작하는것으로!

# import sys
# from collections import deque
# #상하좌우
# dx = [-1, 0, 1, 0] #12시방향, 3시방향, 6시방향, 9시방향
# dy = [0, 1, 0, -1]
# #배열의크기 n*m
# n,m = map(int,input().split())
# maze = [list(map(int,input())) for _ in range(n)]
# visited = [[0]*(m) for _ in range(n)] #0으로 초기화 무조건 n,m로 들어온댓으니까!
# q = deque()
# q.append((1,1))
# visited[1][1]=1 #한번 방문한곳은 1로 벽으로 만들기

# # for x in visited:
# #     print(x) #격자판 모양으로 나옴

# while q: # Q가 비면 거짓이되어서 멈추도록!
#     tmp = q.popleft()
#     for i in range(4): #하나가 나오면 무조건 네방향 탐색해야하니까
#         x = tmp[0] + dx[i]
#         y = tmp[1] + dy[i]
#         if  1 <= x <= n   and  1<= y <=m and maze[x-1][y-1]==1: #통로여야 가지!
#             visited[x][y]=1 #벽으로 만드는것
#             maze[x-1][y-1] = maze[x-1][y-1]+maze[tmp[0]-1][tmp[1]-1]
#             q.append((x,y))
# for i in maze:
#     print(i)

# print(maze[n-1][m-1])

#두번째 시도
import sys
from collections import deque
#상하좌우
dx = [-1, 0, 1, 0] #12시방향, 3시방향, 6시방향, 9시방향
dy = [0, 1, 0, -1]
#배열의크기 n*m
n,m = map(int,input().split())
maze = [list(map(int,input())) for _ in range(n)]
print(f'maze')
for x in maze:
    print(x)
visited = [[0]*(m) for _ in range(n)] #0으로 초기화 무조건 n,m로 들어온댓으니까!
q = deque()
q.append((0,0))
print(q)
visited[0][0]=1 #한번 방문한곳은 1로 벽으로 만들기
print(f'visited')
for x in visited:
    print(x) #격자판 모양으로 나옴

while q: # q가 비면 거짓이되어서 멈추도록!
    tmp = q.popleft()
    for i in range(4): #하나가 나오면 무조건 네방향 탐색해야하니까
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        print(f'x:{x} y:{y}')
        if  0 <= x <= n-1   and  0<= y <=m-1 and maze[x][y]==1: #통로여야 가지!
            visited[x][y]=1 #벽으로 만드는것
            maze[x][y] = maze[x][y]+maze[tmp[0]][tmp[1]]
            q.append((x,y))
# # for i in maze:
# #     print(i)

print(maze[n-1][m-1])