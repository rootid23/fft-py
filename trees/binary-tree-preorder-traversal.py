#!/usr/bin/env python

#Given a binary tree, return the preorder traversal of its nodes' values.
#Example:
#Input: [1,null,2,3]
#   1
#    \
#     2
#    /
#   3
#Output: [1,2,3]
#Follow up: Recursive solution is trivial, could you do it iteratively?

from TreeNode import TreeNode
import unittest

#Iterative traversal

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        s, r = [], []
        if(not root) :
            return s
        s += [ root ]
        while (s) :
            root = s.pop()
            r += [ root.val ]
            if(root.right) :
                s += [ root.right ]
            if(root.left) :
                s += [ root.left ]
        return r

