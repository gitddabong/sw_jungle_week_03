import sys
from collections import deque

def bfs(x, y, maze, dist, visited):
    q = deque()
    q.append([x, y])
    # 시작점 설정
    while q:
        # 큐의 맨 앞에 있는 노드를 선택
        cur_x, cur_y = map(int, q.popleft())
        visited[cur_x][cur_y] = True
        cur_dist = dist[cur_x][cur_y]         # 시작점에서 현재위치까지의 거리
        for i in range(4):
            # 다음 경로가 방문하지 않았고 경로가 있는 경우 경로를 큐에 삽입, 리스트에 표시
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if maze[next_x][next_y] == '1' and visited[next_x][next_y] == False:
                if not [next_x, next_y] in q:
                    q.append([next_x, next_y])
                    dist[next_x][next_y] = cur_dist + 1

if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    maze = []
    maze.append(['0' for _ in range(M+2)])
    for _ in range(N):
        maze.append(list('0' + input().rstrip() + '0'))
    maze.append(['0' for _ in range(M+2)])
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dist = [[0 for _ in range(M+2)] for _ in range(N+2)]
    visited = [[False for _ in range(M+2)] for _ in range(N+2)]
    
    dist[1][1] = 1
    bfs(1, 1, maze, dist, visited)

    print(dist[N][M])