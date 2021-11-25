# use dfs
import sys

n=int(sys.stdin.readline())#노드의 갯수
# 2차원 배열 선언
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
parents = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)  
    graph[b].append(a) #방향성을 안나타내기위해 ! 그래프와 트리의 차이지!
print(graph)

def dfs(start, visited):
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            # print(f'start:{start}  i:{i}')
            parents[i] = start
            dfs(i, visited)


dfs(1, visited)

for i in range(2, n+1):
    print(parents[i])