# import sys
# from collections import deque

# def bfs(start):
#     q = deque()
#     q.append(start)
#     count = 0

#     while q:
#         node = q.popleft()
#         count += 1
#         for next in graph[node]:
#             if checklist[next] == 0:
#                 q.append(next)
#                 checklist[next] = count
#                 if count == dist:
#                     result.append(next)

# if __name__ == "__main__":
#     input = sys.stdin.readline
#     V, E, dist, start = map(int, input().split())

#     graph = [[] for _ in range(V+1)]
#     for i in range(1, E+1):
#         src, dst = map(int, input().split())
#         if not dst in graph[src]:
#             graph[src].append(dst)
#     checklist = [0 for _ in range(V+1)]
#     result = []

#     bfs(start)

#     result.sort()
#     for node in result:
#         print(node)

#     if not result:
#         print(-1)

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    deq = deque()
    deq.append(start)
    while deq:
        # 큐의 맨 앞에 있는 노드 선택(pop)
        v = deq.popleft()
        for next in graph[v]:
            if checklist[next] == 0:
                deq.append(next)
                checklist[next] = checklist[v] + 1

                if checklist[next] == target:
                    result.append(next)

if __name__ == "__main__":
    v, e, target, start = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        if b == start:
            continue
        graph[a].append(b)
        
    checklist = [0 for _ in range(v+1)]
    result = []

    bfs(start)

    if not result:
        print(-1)
        exit()

    result.sort()
    for node in result:
        print(node)