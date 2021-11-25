# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：binaryTree.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-19 오전 10:48 
'''

class Node :
    def __init__(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree :
    def __init__(self):
        self.root = None

    def search(self, key):
        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.value
            elif p < p.key:
                p = p.left
            else:
                p = p.right

    def add(self, key, value):
        def add_node(node, key, value):
            if key ==node:
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True
        if self.root is None:
            self.root = Node(key, value, None,None)
        else:
            return add_node(self.root, key, value)

    def remove(self, key):
        p = self.root
        parent = None
        is_left_child = True

        while True:
            if p is None:
                return False

            if key == p.key:
                break

            else:
                parent = p
                if key < p.key:
                    is_left_child = True
                    p = p.left
                else:
                    is_left_child = False
                    p = p.right

        if p.left is None:
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right
            else:
                parent.rigth = p.right
        elif p.right is None:
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.left
        else:
            parent = p
            left = p.left
            is_left_child = True
            while left.right is not None:
                parent=left
                left=left.right
                is_left_child=False
            p.key = left.key
            p.value = left.value
            if is_left_child:
                parent.left = left.left
            else:
                parent.right = left.right

        return True
