import sys

n,m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [False] *(n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for x in graph:
    print(x)

def DFS(start, visited):
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            DFS(i, visited)

cnt = 0
for i in range(1, n+1):
    if visited[i] == False:
        cnt+=1
        DFS(i, visited)

print(cnt)