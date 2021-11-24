import sys
from collections import deque
input = sys.stdin.readline

v = int(input())
e = int(input())
graph = [[] for _ in range(v+1)]
in_degree = [0 for _ in range(v+1)]     # 자신에게로 들어오는 노드의 개수
for _ in range(e):
    src, dst, cost = map(int, input().split())
    graph[src].append([dst, cost])
    in_degree[dst] += 1

start, end = map(int, input().split())
max_cost = [0 for _ in range(v+1)]
visit_cnt = [1 for _ in range(v+1)]


que = deque()
for i in range(1, v+1) : 
    if in_degree[i] == 0 : # 자신에게로 들어오는 노드가 없는 노드들은 큐에 삽입
        que.append(i)

# # 여기가 메인.
while que : 
    cur_node = que.popleft() # cur : 현재 방문중인 노드
    
    for next_node, cost in graph[cur_node] :     # 목적지의 노드번호와 거기까지의 코스트
        weight = max_cost[cur_node] + cost
        max_cost[cur_node] = max(max_cost[cur_node], weight) # 시작점에서 현재 노드까지의 최댓값 + 현재 노드에서 다음 노드까지의 거리
        visit_cnt[next_node] += 1
        in_degree[next_node] -= 1     # 현재 노드와 연결된 노드 제거

        if in_degree[next_node] == 0 : 
            que.append(next_node)    # 노드 제거하다보면 자기로 들어오는 노드가 0개가 되는 경우가 있는데, 이때 큐에 삽입

print(max_cost[end])
print(visit_cnt[end]) 