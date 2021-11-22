# import sys

# def dfs(depth = 0, total = 0):
#     pass


# if __name__ == "__main__":
#     input = sys.stdin.readline

#     n = int(input())
#     nums = list(map(int, input().split()))
#     op_input = list(map(int, input().split()))
#     operators = ['+', '-', '*', '/']
#     op_list = []
#     for i in range(4):
#         for _ in range(op_input[i]):
#             op_list.append(operators[i])

#     # depth의 limit
#     max_length = len(nums) + len(op_list)

#     op_checklist = operators

import sys
input = sys.stdin.readline

def calc(num, idx, add, sub, mul, div):
    global max_val, min_val
    if idx == n:
        max_val = max(max_val, num)
        min_val = min(min_val, num)
        return

    if add:
        calc(num+nums[idx], idx+1, add-1, sub, mul, div)
    if sub:
        calc(num-nums[idx], idx+1, add, sub-1, mul, div)
    if mul:
        calc(num*nums[idx], idx+1, add, sub, mul-1, div)
    if div:     # // 과 int()가 왜 값이 다르지?
        calc(int(num/nums[idx]), idx+1, add, sub, mul, div-1)

if __name__ == "__main__":
    max_val = -float('inf')
    min_val = float('inf')
    
    n = int(input())
    nums = list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())

    calc(nums[0], 1, add, sub, mul, div)
    print(max_val)
    print(min_val)