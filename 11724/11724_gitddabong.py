# 이 그래프에서 덩어리 그래프가 몇갠지 출력

import sys
sys.setrecursionlimit(10 ** 8)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    visited = [False] * (n+1)

    cnt = 0
    for i in range(1, n+1):
        if visited[i] == False:
            cnt += 1
            dfs(i)
    print(cnt)