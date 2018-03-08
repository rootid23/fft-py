# Maximum Depth of Binary Tree
# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
#For example:
#Given binary tree [3,9,20,null,null,15,7],
#    3
#   / \
#  9  20
#    /  \
#   15   7
#return its depth = 3.

cnt = 0


# TC : O(n)
class Solution(object):

  def maxDepth(self, root):
    global cnt
    cnt += 1
    print cnt  # for debuggin
    if root is None:
      return 0
    lftHt = 1 + self.maxDepth(root.left)
    rtHt = 1 + self.maxDepth(root.right)
    return max(lftHt, rtHt)
