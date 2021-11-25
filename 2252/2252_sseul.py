# import sys
# from collections import deque
# input = sys.stdin.readline

# #n=노드 m=간선
# n,m = map(int,input().split())

# #nxn그래프 (인덱스번호 1부터하기위해 n+1)
# graph = [[0]*(n+1) for _ in range(n+1)]
# degree = [0]*(n+1) 
# dq = deque()

# for i in range(m):
#     a,b = map(int,input().split())
#     graph[a][b] = 1 
#     degree[b] += 1 # 진입차수 1증가

# for i in range(1, n+1):
#     if degree[i] == 0:
#         dq.append(i)

# while dq:
#     x = dq.popleft()
#     print(x, end=' ')
#     for i in range(1, n+1):
#         if graph[x][i]==1:
#             degree[i]-=1 # i=도착점
#             if degree[i]==0:
#                 dq.append(i)


import sys
from collections import deque
input = sys.stdin.readline

n,m= map(int,input().split()) 

degree = [0]*(n+1)
direct = [[] for _ in range(n+1)]
dq = deque()

for i in range(m):
    a,b = map(int, input().split())
    direct[a].append(b)
    degree[b] += 1

for i in range(1, n+1):
    if degree[i] == 0:
        dq.append(i)

while dq:
    cur = dq.popleft()
    print(cur, end=' ')
    for d in direct[cur]:
        degree[d] -= 1
        if degree[d] == 0:
            dq.append(d)
