# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：programmers_43165.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-24 오후 2:56 
'''
import sys

sys.setrecursionlimit(10**9)

def dfs(arr, n, sum, target):
    cnt = 0
    if n == len(arr):
        if sum == target:
            return 1
        return 0
    cnt += dfs(arr, n+1, sum+arr[n], target)
    cnt += dfs(arr, n+1, sum-arr[n], target)
    return cnt

def solution(numbers, target):
    answer = 0
    answer += dfs(numbers, 0, 0, target)
    return answer

print(solution([1,1,1,1,1], 3))
