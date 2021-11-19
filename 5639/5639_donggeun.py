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

def getPostorder(nums):
    # print('nums', nums)
    length = len(nums)

    if length <= 1:
        return nums

    for i in range(1, length):
        if nums[i] > nums[0]:
            return getPostorder(nums[1:i]) + getPostorder(nums[i:]) + [nums[0]]

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