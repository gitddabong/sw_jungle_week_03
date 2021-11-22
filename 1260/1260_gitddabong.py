import sys
from collections import deque
input = sys.stdin.readline

# bfs
# 시작 노드에서 가장 가까운 노드들을 큐에 push
# 경로 선택과 동시에 큐에서 pop
# 예시 인풋 기준으로 1에서 시작해서 2까지 선택했음(현재 큐에 3,4)
# 이제 1,2가 한 덩어리라고 생각하고 큐를 다시 보면 3,4에 접근 가능. 3을 pop하면서 선택
# 123이 한 덩어리가 되었고 남은 노드는 4. 4를 pop하고 선택

def bfs(v):
    q = deque()
    q.append(v)
    # 시작점 설정
    visit_list1[v] = 1
    # 큐가 빌 때까지 수행
    while q:
        # 큐의 맨 앞에 있는 노드를 선택
        v = q.popleft()
        print(v, end = " ")
        for i in range(1, n+1):
            # 방문하지 않았고 경로가 있는 경우 경로를 큐에 삽입, 리스트에 표시
            if visit_list1[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visit_list1[i] = 1

def dfs(v):
    # 리스트에 현재 위치 방문 표시
    visit_list2[v] = 1
    print(v, end = " ")
    # 1부터 시작하는 건 인덱스 0은 안쓰고 1234만 쓸거라서.
    for i in range(1, n + 1):
        # 아직 방문하지 않았고, 그래프 안에 가려는 곳의 경로가 존재할 경우 재귀실행
        if visit_list2[i] == 0 and graph[v][i] == 1:
            dfs(i)

if __name__ == "__main__":
    n, m, v = map(int, input().split())
    graph = [[0] * (n+1) for _ in range(n+1)]
    visit_list1 = [0] * (n+1)
    visit_list2 = [0] * (n+1)

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x][y] = graph[y][x] = 1

    dfs(v)
    print()
    bfs(v)