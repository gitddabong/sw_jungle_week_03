import sys

def dfs(start):
    global count
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            count += 1
            dfs(i)

if __name__ == "__main__":
    input = sys.stdin.readline
    V = int(input())
    E = int(input())

    visited = [False] * (V+1)
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    count = 0
    
    dfs(1)
    print(count)