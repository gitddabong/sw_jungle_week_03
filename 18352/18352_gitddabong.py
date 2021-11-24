# Wrong Answer

# 4 1 2 1
# 1 2


import sys
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    count = 0
    
    while q:
        node = q.popleft()
        count += 1
        for next in graph[node]:
            if checklist[next] == 0:
                q.append(next)
                checklist[next] = count
                if count == dist:
                    result.append(next)

if __name__ == "__main__":
    input = sys.stdin.readline
    V, E, dist, start = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    for i in range(1, E+1):
        src, dst = map(int, input().split())
        if not dst in graph[src]:
            graph[src].append(dst)
    checklist = [0 for _ in range(V+1)]
    result = []

    bfs(start)
    
    for node in result:
        print(node)
    
    if not result:
        print(-1)