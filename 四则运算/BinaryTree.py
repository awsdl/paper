# -*- coding=utf-8 -*-

import operator

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    treeStack = []  #二叉树
    expression = []  #表达式

    def __init__(self):
        #print("创建二叉树类")
        pass


    def shengcerchashu(self,exp):
        """生成"""
        self.expression  = exp
        for item in self.expression:
            #print(item)
            parent = Node(item)
            if not item in  ['+', '-', 'x', '÷']:
                #操作数
                self.treeStack.append(parent)
            else:
                #运算符
                right = self.treeStack.pop()
                left = self.treeStack.pop()
                parent.right = right
                parent.left = left
                self.treeStack.append(parent)


        #二叉树的根
        parent = self.treeStack[-1]

        return parent

    def treeIsSame(self,root):
        """判断是否相同"""
        if not root.left:
            if not root.right:
                return root.value
        elif root.value == '+' or root.value == 'x':
            left = self.treeIsSame(root.left)
            right = self.treeIsSame(root.right)
            if operator.le(left, right):
                #print(root.value + left + right)
                return root.value + left + right
            else:
                return root.value + right + left
        else:
            return root.value + self.treeIsSame(root.left) + self.treeIsSame(root.right)



