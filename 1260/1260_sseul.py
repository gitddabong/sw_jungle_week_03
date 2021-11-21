import sys
from collections import deque

# 노드와, 간선, 시작 정점 입력
N, M, V = map(int, sys.stdin.readline().split())

# 2차원 배열 생성
graph = [[0] *(N+1) for _ in range(N+1)]
for _ in range(M):
    m1, m2 = map(int, sys.stdin.readline().split())
    graph[m1][m2] = graph[m2][m1] = 1

def bfs(start_v):
    discoverd = [start_v]
    queue = deque()
    queue.append(start_v)

    while queue:
        v = queue.popleft()
        print(v,end=' ')

        for w in range(len(graph[start_v])):
            if graph[v][w] == 1 and (w not in discoverd):
                discoverd.append(w)
                queue.append(w)

def dfs(start_v, discoverd=[]):
    discoverd.append(start_v)
    print(start_v, end=' ')

    for w in range(len(graph[start_v])):
        if graph[start_v][w] == 1 and (w not in discoverd):
            dfs(w,discoverd)

dfs(V)
print()
bfs(V)