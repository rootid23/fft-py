#Binary Search Tree Iterator
#Implement an iterator over a binary search tree (BST). Your iterator will be
#initialized with the root node of a BST.
#Calling next() will return the next smallest number in the BST.
#Note: next() and hasNext() should run in average O(1) time and uses O(h)
#memory, where h is the height of the tree.


#Push left recursively and during pop steer the traverse direction
class BSTIterator(object):

  def __init__(self, root):
    self.stk = []
    self.pushLeft(root)

  def hasNext(self):
    return len(self.stk) != 0

  def next(self):
    nxtVal = -1
    if (self.hasNext()):
      nxtNode = self.stk.pop()
      nxtVal = nxtNode.val
      self.pushLeft(nxtNode.right)
    return nxtVal

  def pushLeft(self, root):
    if (root != None):
      self.stk.append(root)
      self.pushLeft(root.left)


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
