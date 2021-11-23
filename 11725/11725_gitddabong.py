import sys
sys.setrecursionlimit(10**8)

def dfs(start):
    for node in tree[start]:
        # 부모 노드가 설정되지 않았다면 현재 확인하고 있는 노드의 부모를 현재 루트노드로 설정
        if parent[node] == 0:
            parent[node] = start
            dfs(node)

if __name__ == "__main__":
    input = sys.stdin.readline

    V = int(input())
    # 부모 노드를 저장하는 리스트
    parent = [0] * (V+1)
    parent[1] = 1
    
    # 각 노드에 인접한 노드를 저장한 리스트
    tree = [[] for _ in range(V+1)]
    for _ in range(V-1):
        x, y = map(int, input().split())
        tree[x].append(y)
        tree[y].append(x)
        
    dfs(1)
    for i in range(2, V+1):
        print(parent[i])