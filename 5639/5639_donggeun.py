# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：5639_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-19 오전 11:23 
'''

import sys

sys.setrecursionlimit(10**5)

# 후위 순회로 만들기
def getPostorder(nums):
    # print('nums', nums)
    # 리스트 길이
    length = len(nums)
    if length <= 1:
        return nums

    # 제일 앞에 있는것(루트)보다 큰 값이 나오면,
    # 그 값을 기준으로 왼쪽자식과 오른쪽 자식으로 나눈 후
    # 루트를 맨 뒤로 보냄
    for i in range(1, length):
        if nums[i] > nums[0]:
            return getPostorder(nums[1:i]) + getPostorder(nums[i:]) + [nums[0]]

    # 루트보다 큰 값이 없을 경우
    # 어쨌든 루트를 맨 뒤로 보내야 하니 하는듯?
    # 정확히 이해하지 못했지만, 비슷한 느낌
    # !!!!!!오른쪽 자식 없을 경우 호출!!!!!!!
    return getPostorder(nums[1:]) + [nums[0]]

arr = []
while True:
    try:
        arr.append(int(sys.stdin.readline()))
    except:
        break

arr = getPostorder(arr)

for i in arr:
    print(i)