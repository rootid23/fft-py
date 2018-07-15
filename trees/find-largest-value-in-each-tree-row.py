#Find Largest Value in Each Tree Row
#You need to find the largest value in each row of a binary tree.
#Example:
#Input:
#          1
#         / \
#        3   2
#       / \   \
#      5   3   9
#Output: [1, 3, 9]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
import sys


class Solution(object):

  def largestValues(self, root):
    """
        :type root: TreeNode
        :rtype: List[int]
        """
    rst = []

    if (root == None):
      return rst

    #traverse row
    q = deque()
    q.append(root)

    while len(q) != 0:
      tmpQ = deque()
      maxV = -sys.maxsize
      for tmp in q:
        maxV = max(tmp.val, maxV)
        if (tmp.left):
          tmpQ.append(tmp.left)
        if (tmp.right):
          tmpQ.append(tmp.right)
      q = tmpQ
      rst.append(maxV)
    return rst
