def dfs(cnt, res, add, sub, mul, div):
    global max_ans, min_ans
    #재귀 탈출조건!
    if cnt == N:
        max_ans = max(res, max_ans)
        min_ans = min(res, min_ans)
        return
    
    if add>0:
        dfs(cnt+1, res+num_list[cnt],add-1, sub, mul, div)
    if sub>0:
        dfs(cnt+1, res-num_list[cnt], add, sub-1, mul, div)
    if mul>0:
        dfs(cnt+1, res*num_list[cnt], add, sub, mul-1, div)
    if div>0:
        dfs(cnt+1, -((-res)//(num_list[cnt])) if res <0 else res //num_list[cnt], add, sub, mul, div-1)
#수의 개수
N = int(input())
#입력받은 수 리스트 
num_list = list(map(int, input().split())) 
#덧셈뺄샘곳셈나눗셈 개수
add, sub, mul, div = map(int, input().split()) 
#최댓값,최솟값 초기화
max_ans = float('-inf')
min_ans = float('inf')
#dfs함수부르기! 앞에서부터 계산하니까, cnt는 1을 시작으로 첫번째예제에서 숫자 2개 주어지고, 5,6 / 0 0 1 0 이면, 5 * 6 인데, 5를 부르고 시작하니 cnt는 1, res 는 아직까진 5 따라서 num_list[0]
dfs(1, num_list[0], add, sub, mul, div)
print(max_ans)
print(min_ans)