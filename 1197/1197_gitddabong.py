import sys

# 노드들 합치기
def union(x, y):
    # 부모 노드 찾기
    x = find(x)
    y = find(y)

    # 어떤 수에 넣든 상관은 없는데
    # 보통 그 그룹 중 가장 작은 수를 부모 노드로 쓰더라
    # 그래서 둘 중 작은 수를 찾아서 부모노드로 갱신
    if y < x:
        parent[x] = y
    else:
        parent[y] = x

# 부모 노드 찾는 함수
def find(x):
    # 자기가 부모노드이거나 혼자 있는 경우
    if x == parent[x]:
        return x

    # 부모 노드가 존재하는 경우에는 재귀를 통해 부모 노드를 찾아가서 갱신
    # 예를 들어서 1은 2의 부모, 2는 3의 부모, 3은 4의 부모라고 했을 때
    # 4에서 시작한다고 치면 1~4까지는 이어져 있고 부모노드는 1이니까
    # 거기까지 쭉 찾아가야됨.
    else:
        parent[x] = find(parent[x])
        return parent[x]

if __name__ == "__main__":
    input = sys.stdin.readline

    V, E = map(int, input().split())

    edge = []
    for _ in range(E):
        x, y, cost = map(int, input().split())
        edge.append((cost,x,y))

    # cost가 가장 작은 것부터 오름차순
    edge.sort(key = lambda x : x[0])
    parent = list(range(V + 1))

    # 가중치가 최솟값인것만 고르기
    # 다 고르고나니 트리가 이어지지 않는 경우도 있다
    # 그럼 합치기
    sum = 0
    for cost, x, y in edge:
        if find(x) != find(y):
            union(x, y)
            sum += cost

    print(sum)