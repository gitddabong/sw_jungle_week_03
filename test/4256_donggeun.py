# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03
@File ：4256_donggeun.py
@IDE  ：PyCharm
@Author ： Hwang
@Date ：2021-11-25 오전 10:17
'''

def divideAndConquer(preOrder, inOrder):
    if len(preOrder) == 1:
        return  preOrder
    elif len(preOrder) == 0:
        return []
    elif len(inOrder) == 1:
        return inOrder[0]
    elif len(inOrder) == 0:
        return []
    root = preOrder[0]
    idx = inOrder.index(root)
    in_left = inOrder[:idx]
    in_right = inOrder[idx+1:]
    pre_left= preOrder[1:len(in_left)+1]
    pre_right= preOrder[len(pre_left)+1:]
    left = divideAndConquer(pre_left, in_left)
    right = divideAndConquer(pre_right, in_right)

    tree = left+right+[root]

    return tree

import sys

testCase = int(sys.stdin.readline())

for _ in range(testCase):

    n = int(sys.stdin.readline())
    # root + left + right
    preOrder = list(map(int, sys.stdin.readline().split()))
    # left + root + right
    inOrder = list(map(int, sys.stdin.readline().split()))

    tree =divideAndConquer(preOrder,inOrder)
    print(*tree)
