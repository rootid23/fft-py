#Largest BST Subtree
#Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest
means subtree with
#largest number of nodes in it.
#Note:
#A subtree must include all of its descendants.
#Here's an example:
#    10
#    / \
#   5  15
#  / \   \
# 1   8   7
#The Largest BST Subtree in this case is the highlighted one. (5,1,8)
#The return value is the subtree's size, which is 3.
#Hint:
#You can recursively use algorithm similar to 98. Validate Binary Search Tree at each node of the
#tree, which will
#result in O(nlogn) time complexity.
#Follow up:
#Can you figure out ways to solve it with O(n) time complexity?

#TC - O(N^2)
def largestBST(self, root) :

  if(not root) : return 0

  def size(root) :
    if(not root) : return 0
    return 1 + size(root.left) + size(root.right)


   def isBST(root, maxE=sys.maxsize, minE=-sys.maxsize) :
       if(not root) : return True
       if(root.val > minE and root.val < maxE) :
           return isBST(root.left, root.val, minE) \
               and isBST(root.right, maxE ,root.val)
       return False

   return isBST(root)

  if(isBST(root)) :
    return size(root)

  return max(self.largestBST(root.left), self.largestBST(root.right))

#Bottomup approach
#TC - O(N)
def largestBSTIterative(root) :
  if(isBST(root.left) and isBST(root.right)) :
    return True

def __init__ == "main()" :




