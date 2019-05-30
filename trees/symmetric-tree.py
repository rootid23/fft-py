
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # binary tree - each node w've at most 2 childern
        # at least 2 nodes

        # left subtree = right subtree
        # top-down traversal and comapre the right and left subtree

        # perfect BT , Tc ? O(n)
        if(not root) : return True
        return self.isSymmetricHelper(root.left, root.right)

    def isSymmetricHelper(self, lt, rt) :

        if(not lt and not rt) : return True
        if(not lt and rt or not rt and lt) : return False
        if(lt and rt and lt.val == rt.val) :
            return self.isSymmetricHelper(lt.left, rt.right) and self.isSymmetricHelper(lt.right, rt.left)
        return False


#Recursive solution
def isSymmetric(self, root):

    #top - down
    #structure and value
    def isSHelper(lt, rt) :
        if(not lt and not rt) :
            return True
        if(lt and rt and lt.val == rt.val) :
            return isSHelper(lt.left, rt.right) and isSHelper(lt.right, rt.left)
        return False

    if(not root) : return True
    return isSHelper(root.left, root.right)

#Iterative solution
import collections
class Solution:
    def isSymmetric(self, root):
        if not root :
            return True
        q = collections.deque([root.left, root.right])

        while q :
            t1, t2 = q.popleft(), q.popleft()
            if not t1 and not t2 :
                continue
            if not t1 or not t2 or (t1.val != t2.val) : return False

            q += [t1.left, t2.right, t1.right, t2.left]
        return True

#101. Symmetric Tree
#Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#    1
#   / \
#  2   2
# / \ / \
#3  4 4  3
#But the following [1,2,2,null,3,null,3] is not:
#    1
#   / \
#  2   2
#   \   \
#   3    3
