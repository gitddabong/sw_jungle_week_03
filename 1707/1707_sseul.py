# use dfs
import sys
sys.setrecursionlimit(10 ** 6)

t=int(sys.stdin.readline())#테스트케이스 갯수

def dfs(start, group):
    visited[start] = group # 방문한 노드에 group 할당
    for i in graph[start]:
        if visited[i] == 0: # 아직 안 가본 곳이면 방문
            if not dfs(i, -group): #이부분?
                return False
        elif visited[i] == visited[start]: # 방문한 곳인데, 그룹이 동일하면 False
            return False
    return True

for _ in range(t):
    #노드 갯수 v개 간선갯수 e개
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    #2차원 배열 선언
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a) #방향성을 안나타내기위해 ! 그래프와 트리의 차이지!

    bipatite = True

    for i in range(1, v+1):
        if visited[i] == 0: #방문한 정점 아니면 dfs수행
            bipatite = dfs(i,1)
            if not bipatite:
                break
    print('YES' if bipatite else 'NO')
