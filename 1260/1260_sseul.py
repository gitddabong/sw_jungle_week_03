import sys
from collections import deque
input = sys.stdin.readline

def dfs(v):
    # 리스트에 현재 위치 방문 표시
    visit_list1[v] = 1
    print(v, end = " ")
    # 1부터 시작 : 인덱스 1부터 맞추기위해
    for i in range(1, n + 1):
        # 아직 방문하지 않았고, 그래프 안에 가려는 곳의 경로가 존재할 경우 재귀실행
        if visit_list1[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    q = deque()
    q.append(v)
    # 시작점 설정
    visit_list2[v] = 1
    # 큐가 빌 때까지 수행
    while q:
        # 큐의 맨 앞에 있는 노드를 선택
        v = q.popleft()
        print(v, end = " ")
        for i in range(1, n+1):
            # 방문하지 않았고 경로가 있는 경우 경로를 큐에 삽입, 리스트에 표시
            if visit_list2[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visit_list2[i] = 1



if __name__ == "__main__":
    n, m, v = map(int, input().split())
    graph = [[0] * (n+1) for _ in range(n+1)]
    visit_list1 = [0] * (n+1)
    visit_list2 = [0] * (n+1)

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x][y] = graph[y][x] = 1

    dfs(v)
    print()
    bfs(v)