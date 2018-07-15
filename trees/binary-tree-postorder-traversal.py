#!/usr/bin/env python

#Given a binary tree, return the postorder traversal of its nodes' values.
#Example:
#Input: [1,null,2,3]
#   1
#    \
#     2
#    /
#   3
#Output: [3,2,1]
#Follow up: Recursive solution is trivial, could you do it iteratively?

from TreeNode import TreeNode
import unittest


class Solution(object):

    def postorderTraversal(self, root):

        s, r = [], []
        lastNodeVisited, peekNode = None, None
        while(s or root) :
            if(root) :
                s += [ root ]
                root = root.left
            else :
                peekNode = s[-1]
                if(peekNode.right and lastNodeVisited != peekNode.right) :
                    root = peekNode.right
                else :
                    r += [ peekNode.val ]
                    lastNodeVisited = s.pop()
        return r
