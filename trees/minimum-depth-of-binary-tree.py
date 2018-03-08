# Minimum Depth of Binary Tree
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the
# nearest leaf node.


# BFS
# Return level once leaf node found
# TC : optimized O(n)
class Solution(object):

  def minDepth(self, root):
    if root is None:
      return 0
    q = []
    q.append(root)
    lvl = 1
    while q:
      for _ in range(len(q)):
        tmp = q.pop(0)
        if (tmp.left == None and tmp.right == None):
          return lvl
        if (tmp.left):
          q.append(tmp.left)
        if (tmp.right):
          q.append(tmp.right)
      lvl += 1
    return lvl

# DFS
#TC : O(n)
#Minimize the height when leaf node found
def minDepth(self, root):
  if root is None:
    return 0
  lft = self.minDepth(root.left) + 1
  rt = self.minDepth(root.right) + 1
  if (root.left != None and root.right != None):
    return min(lft, rt)  #
  return max(lft, rt)
