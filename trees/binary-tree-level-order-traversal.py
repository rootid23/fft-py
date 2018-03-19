#Binary Tree Level Order Traversal
#Given a binary tree, return the level order traversal of its nodes' values.
#(ie, from left to right, level by level).
#For example:
#Given binary tree {3,9,20,#,#,15,7}
#
#    3
#   / \
#  9  20
#    /  \
#   15   7
#[
#  [3],
#  [9,20],
#  [15,7]
#]
#

#W/ deque - popleft,append
#https://stackoverflow.com/questions/1296511/efficiency-of-using-a-python-list-as-a-queue
from collections import deque


class Solution(object):

  def levelOrder(self, root):

    def levelOrderHelper(root):
      if (root == None):
        return
      self.q.append(root)
      lcnt = len(self.q)
      while (lcnt > 0):
        tmplst = []
        for _ in range(lcnt):
          tmp = self.q.popleft()
          if (tmp.left != None):
            self.q.append(tmp.left)
          if (tmp.right != None):
            self.q.append(tmp.right)
          tmplst.append(tmp.val)
        self.rst.append(tmplst)
        lcnt = len(self.q)

    self.rst = []
    self.q = deque()
    levelOrderHelper(root)
    return self.rst


#
#>>> from timeit import timeit
#>>> n = 1024 * 1024
#>>> while n > 1:
#...     print '-' * 30, n
#...     timeit('s.appendleft(37)', 'import collections; s = collections.deque()', number=n)
#...     timeit('s.insert(0,37)', 's = []', number=n)
#...     n >>= 1


#
def levelOrder(self, root):
  if not root:
    return []
  ans, level = [], [root]
  while level:
    ans.append([node.val for node in level])
    temp = []
    for node in level:
      temp.extend([node.left, node.right])
    level = [leaf for leaf in temp if leaf]
  return ans


#only one list comprehension in while loop to get the next level
def levelOrder(self, root):
  ans, level = [], [root]
  while root and level:
    ans.append([node.val for node in level])
    level = [kid for n in level for kid in (n.left, n.right) if kid]
  return ans


def levelOrder(self, root):
  ans, level = [], [root]
  while root and level:
    ans.append([node.val for node in level])
    LRpair = [(node.left, node.right) for node in level]
    level = [leaf for LR in LRpair for leaf in LR if leaf]
  return ans


#Recusrive solution
def helper(self, root, level):
  if not root:
    return []  # instead of None
  else:
    if level < len(self.l):
      self.l[level].append(root.val)
    else:
      self.l.append([root.val])
    self.helper(root.left, level + 1)
    self.helper(root.right, level + 1)
  return self.l


def levelOrder(self, root):
  """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
  return self.helper(root, 0)  #no
