#이진검색 트리의 전위 순회가 주어졌을 때 후위순회를 구하는 문제
#아이디어 : 어떤 트리의 전위 순회에서 맨 첫번째 방문 노드는 루트노드!
#이진 트리에서 나머지 노드 리스트를 특정 기준으로 자르면 됨.
#자른 각각의 리스트에 대해 첫번째 노드가 해당 리스트로 구성된 서브트리의 루트노드.
#자르는 기준 : 루트노드 아래 딸린 노드들 중 루트 노드보다 큰지 작은지를 기준으로 자름!!
# start, end지점을 받은 후 스타트 지점의 노드값을 루트노트(기준값)으로 한다. 루트노드 보다 작으면 왼쪽 서브트리에 있는것, 루트노드보다 크면 오른쪽 서브트리에 있는것.



import sys
sys.setrecursionlimit(10 ** 6) #파이썬 재귀 최대 깊이의 설정!
input = sys.stdin.readline

def post_order(start, end):
    if start > end:
        return

    root = pre_order[start] # 루트 노드
    idx = start + 1

    # root보다 커지는 지점을 찾기   
    while idx <= end:
        if pre_order[idx] > root:
            break
        idx += 1

    post_order(start + 1, idx - 1) # 왼쪽     
    post_order(idx, end) # 오른쪽
#어차피 이미 루트노드를 기준으로 왼쪽은 모두 루트노드보다 작고, 오른쪽은 모두 루트노드보다 크다. 
# 따라서 루트노드보다 작은 값이 나오는 마지막 인덱스와 루트노드보다 큰 값이 나오는 첫 인덱스 이 경계인덱스를 찾기만 하면 나머지는 구할 필요가없음.
# 그 경계값을 찾아 break!

#이부분이 가장 이해가 잘안됨... 왼쪽까지 오케이 근데 오른쪽으로 어떻게 바로 넘어가지????

    print(root) # 후위 순회 root 마지막 출력


pre_order = []
while True:
    try:
        pre_order.append(int(input()))
    # 예외 발생시 break
    except:
        break

post_order(0, len(pre_order) - 1)