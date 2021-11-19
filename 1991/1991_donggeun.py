# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：1991_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-19 오전 11:08 
'''

import sys

n = int(sys.stdin.readline())
tree = {}

for i in range(n):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

def preOrder(root):
    if root != '.':
        print(root, end='')
        preOrder(tree[root][0])
        preOrder(tree[root][1])

def inOrder(root):
    if root != '.':
        inOrder(tree[root][0])
        print(root,end='')
        inOrder(tree[root][1])

def postOrder(root):
    if root != '.':
        postOrder(tree[root][0])
        postOrder(tree[root][1])
        print(root,end='')

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
