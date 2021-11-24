import sys
input = sys.stdin.readline
from collections import deque

Vn, En = map(int, input().split())
parent = [0 for i in range(Vn + 1)] # 자신에게로 들어오는 노드가 몇 개인지 저장하는 리스트
V = [[] for i in range(Vn + 1)]     # 인접 리스트(단방향)
for i in range(En) : 
    big, small = map(int, input().split())
    V[big].append(small)
    parent[small] = parent[small] + 1

que = deque()
for i in range(1, Vn + 1) : 
    if parent[i] == 0 : # 자신에게로 들어오는 노드가 없는 노드들은 큐에 삽입
        que.append(i)

# 여기가 메인.
while que : 
    now = que.popleft() # 큐에 있는 맨 앞의 값을 pop해서 정렬 시작
    print(now, end = ' ')
    for next in V[now] : 
        parent[next] = parent[next] - 1     # 현재 노드와 연결된 노드 제거
        if parent[next] == 0 : 
            que.append(next)    # 노드 제거하다보면 자기로 들어오는 노드가 0개가 되는 경우가 있는데, 이때 큐에 삽입