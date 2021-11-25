from collections import deque

#n=도시개수, m=도로개수, k=거리정보, x=출발도시번호
n,m,k,x = map(int,input().split())
graph = [ [] for _ in range(n+1)]

for i in range(m):
    a,b = list(map(int,input().split()))
    graph[a].append(b)
print(graph)

distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])

while q:
    tmp = q.popleft()
    for t in graph[tmp]:
        if distance[t] == -1:
            distance[t] = distance[tmp] + 1
            q.append(t)
    
check = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)

