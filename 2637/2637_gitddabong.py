import sys
from collections import deque
input = sys.stdin.readline

v = int(input())
e = int(input())
graph = [[] for _ in range(v+1)]
in_degree = [0 for i in range(v+1)]
for _ in range(1, e+1):
    target, src, cnt = map(int, input().split())
    graph[target].append([src, cnt])
    in_degree[src] += 1

# 모든 부품들의 필요한 개수 저장하는 리스트
parts = [0 for _ in range(v+1)]

# 기본 부품만 담아놓은 리스트
based_parts = []
for i in range(1,v+1):
    if not graph[i]:
        based_parts.append(i)

que = deque()
for i in range(1, v+1):
    if in_degree[i] == 0:
        que.append(i)
        parts[i] = 1

while que:
    cur_node = que.popleft()    # 방문할 노드 pop
    for next_node in graph[cur_node]:   # 인접 노드 돌면서 부품 개수추가
        # 
        target, cost = next_node
        parts[target] += parts[cur_node] * cost

        in_degree[target] -= 1
        
        if in_degree[target] == 0:
            que.append(target)

for idx in based_parts:
    print(idx, parts[idx])

# print(graph)
# print(in_degree)
# print(based_parts)

