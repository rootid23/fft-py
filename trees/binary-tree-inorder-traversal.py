#!/usr/bin/env python

#Given a binary tree, return the inorder traversal of its nodes' values.
#Example:
#Input: [1,null,2,3]
#   1
#    \
#     2
#    /
#   3
#Output: [1,3,2]
#Follow up: Recursive solution is trivial, could you do it iteratively?

from TreeNode import TreeNode
import unittest

#Iterative traversal
class Solution(object):
    def inorderTraversal(self, root):
        s, r = [], []
        while (s or root) :
            if(root) :
                s += [ root ]
                root = root.left
            else :
                root = s.pop()
                r += [ root.val ]
                root = root.right
        return r

#Recursive
class Solution(object):
  def __init__(self):
    self.lst = []
  """
    :type root: TreeNode
    :rtype: List[int]
  """
  def inorderTraversal(self, root):
    if not root:
      return self.lst
    self.lst = self.inorderTraversal(root.left)
    self.lst.append(root.val)
    self.lst = self.inorderTraversal(root.right)
    return self.lst

class Test(unittest.TestCase):
  def test_str_pal(self):
    s = Solution()
    t = TreeNode(10)
    t.left = TreeNode(12)
    t.right = TreeNode(19)
    print t
    self.assertEqual(s.inorderTraversal(None), [])
    self.assertEqual(s.inorderTraversal(t), [12, 10, 19])
if __name__ == '__main__':
  unittest.main()
# vim: ai ts=2 sts=2 et sw=2 tw=100 fdm=indent fdl=1
