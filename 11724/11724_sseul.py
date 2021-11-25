# use dfs
import sys

# 정점, 간선 입력
n,m = map(int, sys.stdin.readline().split())
# 2차원 배열 선언
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start, visited):
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            dfs(i, visited)

# 한 정점을 기준으로 dfs가 끝났을때,
# visited하지 않은 정점이 있을 경우 해당 정점을 기준으로 dfs 호출
cnt = 0
for i in range(1, n+1):
    if visited[i] == False:
        cnt+=1
        dfs(i, visited)

print(cnt)

